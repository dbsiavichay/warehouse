from src.movement.app.use_cases import CreateMovementUseCase

from .validators import MovementInput, MovementResponse


class MovementController:
    def __init__(self, create_movement: CreateMovementUseCase):
        self.create_movement = create_movement

    def create(self, new_movement: MovementInput) -> MovementResponse:
        movement = self.create_movement.execute(
            new_movement.model_dump(exclude_none=True)
        )
        return MovementResponse.model_validate(movement)
