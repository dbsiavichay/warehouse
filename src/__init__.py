import uuid

from fastapi import Depends

from config import config
from src.core.infra.di import DependencyContainer, LifetimeScope
from src.product.app.commands import SaveProductCommand
from src.product.app.queries import ProductQueries
from src.product.domain.repositories import ProductRepository
from src.product.infra.controllers import ProductController
from src.product.infra.repositories import ProductRepositoryImpl

container = DependencyContainer()


def initialize_dependencies() -> None:
    """Initializes all application dependencies."""

    db_connection_string = config.DB_CONNECTION_STRING
    if not db_connection_string:
        raise ValueError("Database connection string not found in environment")
    container.configure_db(db_connection_string)

    # Register the product repository
    container.register(
        ProductRepository,
        factory=lambda c, scope_id=None: ProductRepositoryImpl(
            c.get_scoped_db_session(scope_id) if scope_id else c.get_db_session()
        ),
        scope=LifetimeScope.SCOPED,
    )

    # Register the product commands
    container.register(
        SaveProductCommand,
        factory=lambda c, scope_id=None: SaveProductCommand(
            c.resolve_scoped(ProductRepository, scope_id)
            if scope_id
            else c.resolve(ProductRepository)
        ),
        scope=LifetimeScope.SCOPED,
    )

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

    # Register the product controller
    container.register(
        ProductController,
        factory=lambda c, scope_id=None: ProductController(
            c.resolve_scoped(SaveProductCommand, scope_id)
            if scope_id
            else c.resolve(SaveProductCommand),
            c.resolve_scoped(ProductQueries, scope_id)
            if scope_id
            else c.resolve(ProductQueries),
        ),
        scope=LifetimeScope.SCOPED,
    )


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
