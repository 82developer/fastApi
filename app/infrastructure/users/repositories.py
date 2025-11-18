from typing import List, Optional

from app.domain.users.entities import User
from app.domain.users.repositories import UserRepository


class InMemoryUserRepository(UserRepository):
    """Simple in-memory repository for demo purposes."""

    def __init__(self) -> None:
        self._users: List[User] = [
            User(id=1, name="Alice", email="alice@example.com"),
            User(id=2, name="Bob", email="bob@example.com"),
        ]
        self._next_id = 3

    def get_all(self) -> List[User]:
        return list(self._users)

    def get_by_id(self, user_id: int) -> Optional[User]:
        return next((u for u in self._users if u.id == user_id), None)

    def add(self, name: str, email: str) -> User:
        user = User(id=self._next_id, name=name, email=email)
        self._users.append(user)
        self._next_id += 1
        return user
