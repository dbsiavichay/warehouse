from abc import ABC, abstractmethod

from .entities import Movement


class MovementRepository(ABC):
    @abstractmethod
    def create(self, movement: Movement) -> Movement:
        raise NotImplementedError
