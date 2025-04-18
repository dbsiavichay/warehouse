from fastapi import APIRouter

from src.product.infra.controllers import ProductController

router = APIRouter()


@router.get("/")
def get_all():
    return ProductController().get_all()


@router.get("/{id}")
def get_by_id(id: int):
    return ProductController().get_by_id(id)
