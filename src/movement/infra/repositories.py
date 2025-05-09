from src.core.infra.repositories import BaseRepository
from src.movement.domain.entities import Movement
from src.movement.infra.models import MovementModel


class MovementRepositoryImpl(BaseRepository[Movement]):
    __model__ = MovementModel
