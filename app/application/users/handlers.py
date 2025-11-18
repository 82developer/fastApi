from typing import List, Optional

from app.domain.users.repositories import UserRepository
from app.domain.users.entities import User
from .messages import CreateUserCommand, GetUserByIdQuery, ListUsersQuery


class CreateUserHandler:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    async def __call__(self, command: CreateUserCommand) -> int:
        user = self._repo.add(name=command.name, email=command.email)
        return user.id


class GetUserByIdHandler:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    async def __call__(self, query: GetUserByIdQuery) -> Optional[User]:
        return self._repo.get_by_id(query.user_id)


class ListUsersHandler:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    async def __call__(self, query: ListUsersQuery) -> List[User]:
        return self._repo.get_all()
