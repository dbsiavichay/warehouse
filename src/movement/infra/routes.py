from fastapi import APIRouter, Depends

from src import get_movement_controller
from src.movement.infra.validators import MovementInput, MovementResponse

from .controllers import MovementController


class MovementRouter:
    def __init__(self):
        self.router = APIRouter()
        self._setup_routes()

    def _setup_routes(self):
        """Sets up all the routes for the router."""
        self.router.post("", response_model=MovementResponse, summary="Save movement")(
            self.create
        )

    def create(
        self,
        new_movement: MovementInput,
        movement_controller: MovementController = Depends(get_movement_controller),
    ) -> MovementResponse:
        """Save a new movement."""
        return movement_controller.create(new_movement)
