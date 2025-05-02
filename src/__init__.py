import uuid

from fastapi import Depends

from config import config
from src.core.infra.di import DependencyContainer, LifetimeScope
from src.movement.app.repositories import MovementRepository
from src.movement.app.use_cases import CreateMovementUseCase, FilterMovementsUseCase
from src.movement.infra.controllers import MovementController
from src.movement.infra.repositories import MovementRepositoryImpl
from src.product.app.queries import ProductQueries
from src.product.app.repositories import ProductRepository
from src.product.app.use_cases import (
    CreateProductUseCase,
    DeleteProductUseCase,
    UpdateProductUseCase,
)
from src.product.infra.controllers import ProductController
from src.product.infra.repositories import ProductRepositoryImpl
from src.stock.app.queries import StockQueries
from src.stock.app.repositories import StockRepository
from src.stock.infra.controllers import StockController
from src.stock.infra.repositories import StockRepositoryImpl

container = DependencyContainer()


def init_repositories() -> None:
    """Initializes all repositories."""
    # Register the product repository
    container.register(
        ProductRepository,
        factory=lambda c, scope_id=None: ProductRepositoryImpl(
            c.get_scoped_db_session(scope_id) if scope_id else c.get_db_session()
        ),
        scope=LifetimeScope.SCOPED,
    )
    # Register the stock repository
    container.register(
        StockRepository,
        factory=lambda c, scope_id=None: StockRepositoryImpl(
            c.get_scoped_db_session(scope_id) if scope_id else c.get_db_session()
        ),
        scope=LifetimeScope.SCOPED,
    )
    # Register the movement repository
    container.register(
        MovementRepository,
        factory=lambda c, scope_id=None: MovementRepositoryImpl(
            c.get_scoped_db_session(scope_id) if scope_id else c.get_db_session()
        ),
        scope=LifetimeScope.SCOPED,
    )


def init_use_cases() -> None:
    """Initializes all use cases."""
    # Register the product use cases
    container.register(
        CreateProductUseCase,
        factory=lambda c, scope_id=None: CreateProductUseCase(
            c.resolve_scoped(ProductRepository, scope_id)
            if scope_id
            else c.resolve(ProductRepository)
        ),
    )
    container.register(
        UpdateProductUseCase,
        factory=lambda c, scope_id=None: UpdateProductUseCase(
            c.resolve_scoped(ProductRepository, scope_id)
            if scope_id
            else c.resolve(ProductRepository)
        ),
        scope=LifetimeScope.SCOPED,
    )
    container.register(
        DeleteProductUseCase,
        factory=lambda c, scope_id=None: DeleteProductUseCase(
            c.resolve_scoped(ProductRepository, scope_id)
            if scope_id
            else c.resolve(ProductRepository)
        ),
        scope=LifetimeScope.SCOPED,
    )
    # Register movement use cases
    container.register(
        CreateMovementUseCase,
        factory=lambda c, scope_id=None: CreateMovementUseCase(
            c.resolve_scoped(MovementRepository, scope_id)
            if scope_id
            else c.resolve(MovementRepository),
            c.resolve_scoped(StockRepository, scope_id)
            if scope_id
            else c.resolve(StockRepository),
        ),
        scope=LifetimeScope.SCOPED,
    )
    container.register(
        FilterMovementsUseCase,
        factory=lambda c, scope_id=None: FilterMovementsUseCase(
            c.resolve_scoped(MovementRepository, scope_id)
            if scope_id
            else c.resolve(MovementRepository)
        ),
        scope=LifetimeScope.SCOPED,
    )


def init_queries() -> None:
    """Initializes all queries."""
    # Register the product queries
    container.register(
        ProductQueries,
        factory=lambda c, scope_id=None: ProductQueries(
            c.resolve_scoped(ProductRepository, scope_id)
            if scope_id
            else c.resolve(ProductRepository)
        ),
        scope=LifetimeScope.SCOPED,
    )
    # Register the stock queries
    container.register(
        StockQueries,
        factory=lambda c, scope_id=None: StockQueries(
            c.resolve_scoped(StockRepository, scope_id)
            if scope_id
            else c.resolve(StockRepository)
        ),
        scope=LifetimeScope.SCOPED,
    )


def init_controllers() -> None:
    """Initializes all controllers."""
    # Register the product controller
    container.register(
        ProductController,
        factory=lambda c, scope_id=None: ProductController(
            c.resolve_scoped(CreateProductUseCase, scope_id)
            if scope_id
            else c.resolve(CreateProductUseCase),
            c.resolve_scoped(UpdateProductUseCase, scope_id)
            if scope_id
            else c.resolve(UpdateProductUseCase),
            c.resolve_scoped(DeleteProductUseCase, scope_id)
            if scope_id
            else c.resolve(DeleteProductUseCase),
            c.resolve_scoped(ProductQueries, scope_id)
            if scope_id
            else c.resolve(ProductQueries),
        ),
        scope=LifetimeScope.SCOPED,
    )
    # Register the stock controller
    container.register(
        StockController,
        factory=lambda c, scope_id=None: StockController(
            c.resolve_scoped(StockQueries, scope_id)
            if scope_id
            else c.resolve(StockQueries)
        ),
        scope=LifetimeScope.SCOPED,
    )
    # Register the movement controller
    container.register(
        MovementController,
        factory=lambda c, scope_id=None: MovementController(
            c.resolve_scoped(CreateMovementUseCase, scope_id)
            if scope_id
            else c.resolve(CreateMovementUseCase),
            c.resolve_scoped(FilterMovementsUseCase, scope_id)
            if scope_id
            else c.resolve(FilterMovementsUseCase),
        ),
        scope=LifetimeScope.SCOPED,
    )


def initialize() -> None:
    """Initializes all application dependencies."""

    db_connection_string = config.DB_CONNECTION_STRING
    if not db_connection_string:
        raise ValueError("Database connection string not found in environment")
    container.configure_db(db_connection_string)

    init_repositories()
    init_use_cases()
    init_queries()
    init_controllers()


# Function to generate a unique scope ID for each request
def get_request_scope_id():
    return str(uuid.uuid4())


# Dependency to get the product controller in a request scope
def get_product_controller(
    scope_id: str = Depends(get_request_scope_id),
) -> ProductController:
    """Gets the product controller for a specific request."""
    controller = container.resolve_scoped(ProductController, scope_id)
    try:
        yield controller
    finally:
        # Close the scope when the request ends
        container.close_scope(scope_id)


# Dependency to get the stock controller in a request scope
def get_stock_controller(
    scope_id: str = Depends(get_request_scope_id),
) -> StockController:
    """Gets the stock controller for a specific request."""
    controller = container.resolve_scoped(StockController, scope_id)
    try:
        yield controller
    finally:
        # Close the scope when the request ends
        container.close_scope(scope_id)


# Dependency to get the movement controller in a request scope
def get_movement_controller(
    scope_id: str = Depends(get_request_scope_id),
) -> MovementController:
    """Gets the movement controller for a specific request."""
    controller = container.resolve_scoped(MovementController, scope_id)
    try:
        yield controller
    finally:
        # Close the scope when the request ends
        container.close_scope(scope_id)
