from typing import Any, ClassVar, Generic, List, Optional, TypeVar, Union

from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BinaryExpression, BooleanClauseList

from src.core.app.repositories import Repository
from src.core.domain.entities import Entity
from src.core.infra.mappers import Mapper

from .db import Base

M = TypeVar("T", bound="Base")
E = TypeVar("E", bound="Entity")

Criteria = List[Union[BinaryExpression, BooleanClauseList, Any]]
OrderCriteria = Union[str, Any]


class BaseRepository(Repository[E], Generic[E]):
    __model__: ClassVar[type[M]]

    def __init__(self, session: Session, mapper: Mapper[E, M]):
        self.session = session
        self.mapper = mapper

    def create(self, entity: E) -> E:
        """
        Creates a new entity.
        Args:
            entity: Entity to create
        Returns:
            Created entity
        """
        model = self.__model__(**self.mapper.to_dict(entity))
        self.session.add(model)
        self.session.commit()
        return self.mapper.to_entity(model)

    def update(self, entity: E) -> E:
        """
        Updates an entity.
        Args:
            entity: Entity to update
        """
        model = self.session.query(self.__model__).get(entity.id)
        if model:
            for key, value in self.mapper.to_dict(entity).items():
                setattr(model, key, value)
            self.session.commit()
        return self.mapper.to_entity(model)

    def delete(self, id: int) -> None:
        """
        Deletes an entity.
        Args:
            entity: Entity to delete
        """
        model = self.session.query(self.__model__).get(id)
        if model:
            self.session.delete(model)
            self.session.commit()

    def get_by_id(self, id: int) -> Optional[E]:
        """
        Retrieves an entity by its ID.
        Args:
            id: ID of the entity to retrieve
        Returns:
            Entity if found, None otherwise
        """
        model = self.session.query(self.__model__).get(id)
        return self.mapper.to_entity(model)

    def get_all(self) -> List[E]:
        """
        Retrieves all entities.
        Returns:
            List of all entities
        """
        models = self.session.query(self.__model__).all()
        return [self.mapper.to_entity(model) for model in models]

    def first(self, **kwargs) -> Optional[E]:
        """
        Retrieves the first entity that matches the given criteria.
        Args:
            criteria: List of conditions to filter by
        Returns:
            First entity that matches the criteria, or None if no entity is found
        """
        criteria = [
            getattr(self.__model__, key) == value for key, value in kwargs.items()
        ]
        model = self.session.query(self.__model__).filter(*criteria).first()
        return self.mapper.to_entity(model)

    def filter(
        self,
        criteria: Criteria,
        order_by: Optional[OrderCriteria] = None,
        desc_order: bool = False,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[M]:
        """
        Filters entities according to given criteria

        Args:
            criteria: List of conditions to filter by
            order_by: Field or expression to order by
            desc_order: If True, orders in descending order
            limit: Maximum number of results to return

        Returns:
            List of entities that match the criteria
        """
        query = self.session.query(self.__model__)
        query = query.filter(*criteria)

        if order_by:
            if isinstance(order_by, str):
                order_by = getattr(self.__model__, order_by)

            if desc_order:
                query = query.order_by(desc(order_by))
            else:
                query = query.order_by(asc(order_by))

        if limit is not None:
            query = query.limit(limit)

        if offset is not None:
            query = query.offset(offset)

        return query.all()

    def filter_by(self, limit=None, offset=None, **kwargs) -> List[E]:
        """
        Filters entities by given keyword arguments.
        Args:
            limit: Maximum number of results to return
            offset: Number of results to skip
            **kwargs: Keyword arguments to filter by
        Returns:
            List of entities that match the criteria
        """
        filter_criteria = []
        for key, value in kwargs.items():
            filter_criteria.append(getattr(self.__model__, key) == value)
        objects = self.filter(criteria=filter_criteria, limit=limit, offset=offset)
        return [self.mapper.to_entity(obj) for obj in objects]
