from fastapi import APIRouter, Depends

from src import get_product_controller

from .controllers import ProductController

router = APIRouter()


@router.get("", summary="Get all products")
def get_all(controller: ProductController = Depends(get_product_controller)):
    """Retrieves all products."""
    return controller.get_all()


@router.get("/{id}", summary="Get product by ID")
def get_by_id(id: int, controller: ProductController = Depends(get_product_controller)):
    """Retrieves a specific product by its ID."""
    return controller.get_by_id(id)
