from fastapi import APIRouter, Depends

from src import get_product_controller
from src.product.domain.entities import Product
from src.product.infra.validators import ProductSchema

from .controllers import ProductController


class ProductRouter:
    def __init__(self):
        self.router = APIRouter()
        self._setup_routes()

    def _setup_routes(self):
        """Sets up all the routes for the router."""
        self.router.post("", response_model=Product, summary="Save product")(
            self.create
        )
        self.router.put("/{id}", response_model=Product, summary="Update product")(
            self.update
        )
        self.router.delete("/{id}", summary="Delete product")(self.delete)
        self.router.get("", summary="Get all products")(self.get_all)
        self.router.get("/{id}", summary="Get product by ID")(self.get_by_id)

    def create(
        self,
        new_product: ProductSchema,
        controller: ProductController = Depends(get_product_controller),
    ):
        """Saves a product."""
        return controller.create(new_product)

    def update(
        self,
        id: int,
        product: ProductSchema,
        controller: ProductController = Depends(get_product_controller),
    ):
        """Updates a product."""
        return controller.update(id, product)

    def delete(
        self, id: int, controller: ProductController = Depends(get_product_controller)
    ):
        """Deletes a product."""
        return controller.delete(id)

    def get_all(self, controller: ProductController = Depends(get_product_controller)):
        """Retrieves all products."""
        return controller.get_all()

    def get_by_id(
        self, id: int, controller: ProductController = Depends(get_product_controller)
    ):
        """Retrieves a specific product by its ID."""
        return controller.get_by_id(id)
