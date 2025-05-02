from abc import ABC, abstractmethod

from src.movement.domain.entities import Movement


class MovementRepository(ABC):
    @abstractmethod
    def create(self, movement: Movement) -> Movement:
        raise NotImplementedError

    @abstractmethod
    def filter_by(self, **kwargs) -> list[Movement]:
        raise NotImplementedError
