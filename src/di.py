from typing import Any, Dict, Type, TypeVar

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.product.app.queries import ProductQueries
from src.product.domain.repositories import ProductRepository
from src.product.infra.controllers import ProductController
from src.product.infra.repositories import ProductRepositoryImpl

# Tipo genérico para el contenedor
T = TypeVar("T")


class DependencyContainer:
    """Contenedor de inyección de dependencias para la aplicación."""

    def __init__(self):
        self._dependencies: Dict[Type, Any] = {}
        self._session_factory = None

    def configure_db(self, connection_string: str) -> None:
        """Configura la conexión a la base de datos."""
        engine = create_engine(connection_string)
        self._session_factory = sessionmaker(
            autocommit=False, autoflush=False, bind=engine
        )

    def get_db_session(self) -> Session:
        """Obtiene una sesión de base de datos."""
        if not self._session_factory:
            raise Exception("Database not configured. Call configure_db first.")
        return self._session_factory()

    def register(self, interface_type: Type[T], implementation: T) -> None:
        """Registra una implementación para una interfaz."""
        self._dependencies[interface_type] = implementation

    def resolve(self, interface_type: Type[T]) -> T:
        """Resuelve una dependencia por su tipo."""
        if interface_type not in self._dependencies:
            raise Exception(
                f"No implementation registered for {interface_type.__name__}"
            )
        return self._dependencies[interface_type]


# Instancia global del contenedor
container = DependencyContainer()


def initialize_dependencies(db_connection_string: str) -> None:
    """Inicializa todas las dependencias de la aplicación."""
    # Configurar la base de datos
    container.configure_db(db_connection_string)

    # Crear una sesión para inicializar los repositorios
    session = container.get_db_session()

    # Registrar repositorios
    product_repository = ProductRepositoryImpl(session)
    container.register(ProductRepository, product_repository)

    # Registrar servicios de aplicación
    product_queries = ProductQueries(product_repository)
    container.register(ProductQueries, product_queries)

    # Registrar controladores
    product_controller = ProductController(product_queries)
    container.register(ProductController, product_controller)


def get_product_controller() -> ProductController:
    """Helper para obtener el controlador de productos."""
    return container.resolve(ProductController)
