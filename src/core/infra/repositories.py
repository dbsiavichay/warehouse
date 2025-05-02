from typing import Any, ClassVar, Generic, List, Optional, TypeVar, Union

from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BinaryExpression, BooleanClauseList

from .db import Base

T = TypeVar("T", bound="Base")

Criteria = List[Union[BinaryExpression, BooleanClauseList, Any]]
OrderCriteria = Union[str, Any]


class BaseRepository(Generic[T]):
    __model__: ClassVar[type[T]]

    def __init__(self, session: Session):
        self.session = session

    def filter(
        self,
        criteria: Criteria,
        order_by: Optional[OrderCriteria] = None,
        desc_order: bool = False,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[T]:
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
