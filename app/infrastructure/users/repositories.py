# app/infrastructure/users/repositories.py

from typing import List, Optional

from app.domain.users.entities import User
from app.domain.users.repositories import UserRepository


class InMemoryUserRepository(UserRepository):
    """
    Simple in-memory repository for demo and testing.
    Replace this with a DB-backed repository in real projects.
    """

    def __init__(self) -> None:
        self._users: List[User] = [
            User(id=1, name="Alice", email="alice@example.com"),
            User(id=2, name="Bob", email="bob@example.com"),
        ]

    def get_all(self) -> List[User]:
        return list(self._users)

    def get_by_id(self, user_id: int) -> Optional[User]:
        return next((u for u in self._users if u.id == user_id), None)

    def add(self, user: User) -> User:
        self._users.append(user)
        return user
