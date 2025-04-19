from fastapi import APIRouter

from src.di import get_product_controller

router = APIRouter()


@router.get("")
def get_all():
    controller = get_product_controller()
    return controller.get_all()


@router.get("/{id}")
def get_by_id(id: int):
    controller = get_product_controller()
    return controller.get_by_id(id)
