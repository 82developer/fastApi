# app/domain/users/repositories.py

from abc import ABC, abstractmethod
from typing import List, Optional

from .entities import User


class UserRepository(ABC):
    """
    Abstraction of the user persistence.
    No SQLAlchemy, no DB, just business interface.
    """

    @abstractmethod
    def get_all(self) -> List[User]:
        ...

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    def add(self, user: User) -> User:
        ...
