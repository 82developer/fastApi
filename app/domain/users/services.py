# app/domain/users/services.py

from typing import List, Optional

from .entities import User
from .repositories import UserRepository


class UserService:
    """
    Application service (business logic).
    """

    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def list_users(self) -> List[User]:
        return self._repository.get_all()

    def get_user(self, user_id: int) -> Optional[User]:
        return self._repository.get_by_id(user_id)

    def create_user(self, name: str, email: str) -> User:
        # here you could add validations, rules, etc.
        users = self._repository.get_all()
        next_id = (max((u.id for u in users), default=0) + 1) if users else 1
        user = User(id=next_id, name=name, email=email)
        return self._repository.add(user)
