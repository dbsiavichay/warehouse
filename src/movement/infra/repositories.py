from typing import List

from src.core.infra.repositories import BaseRepository
from src.movement.app.repositories import MovementRepository
from src.movement.domain.entities import Movement
from src.movement.infra.mappers import MovementMapper
from src.movement.infra.models import MovementModel


class MovementRepositoryImpl(BaseRepository[MovementModel], MovementRepository):
    __model__ = MovementModel

    def create(self, movement: Movement) -> Movement:
        movement_dict = MovementMapper.to_dict(movement)
        movement_model = MovementModel(**movement_dict)
        self.session.add(movement_model)
        self.session.commit()
        return MovementMapper.to_entity(movement_model)

    def filter_by(self, limit=None, offset=None, **kwargs) -> List[Movement]:
        filter_criteria = []
        for key, value in kwargs.items():
            filter_criteria.append(getattr(MovementModel, key) == value)
        movements = self.filter(criteria=filter_criteria, limit=limit, offset=offset)
        return [MovementMapper.to_entity(movement) for movement in movements]
