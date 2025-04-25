from sqlalchemy.orm import Session

from src.movement.domain.entities import Movement
from src.movement.domain.repositories import MovementRepository
from src.movement.infra.mappers import MovementMapper
from src.movement.infra.models import MovementModel


class MovementRepositoryImpl(MovementRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, movement: Movement) -> Movement:
        movement_dict = MovementMapper.to_dict(movement)
        movement_model = MovementModel(**movement_dict)
        self.session.add(movement_model)
        self.session.commit()
        return MovementMapper.to_entity(movement_model)
