from abc import ABC, abstractmethod
from typing import List, Optional

from .entities import User


class UserRepository(ABC):
    """Abstraction of user persistence (write + read)."""

    @abstractmethod
    async def get_all(self) -> List[User]:
        ...

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    async def add(self, name: str, email: str) -> User:
        ...
