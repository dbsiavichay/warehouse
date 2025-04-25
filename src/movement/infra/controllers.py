from src.movement.app.commands import MovementCommands
from src.movement.domain.entities import Movement

from .validators import MovementSchema


class MovementController:
    def __init__(self, movement_commands: MovementCommands):
        self.movement_commands = movement_commands

    def create(self, new_movement: MovementSchema) -> Movement:
        movement = Movement(**new_movement.model_dump(exclude_none=True))
        return self.movement_commands.create(movement)
