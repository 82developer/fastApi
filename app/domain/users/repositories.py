from abc import ABC, abstractmethod
from typing import List, Optional

from .entities import User


class UserRepository(ABC):
    """Abstraction of user persistence."""

    @abstractmethod
    def get_all(self) -> List[User]:
        ...

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    def add(self, name: str, email: str) -> User:
        ...
