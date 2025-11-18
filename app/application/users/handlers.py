from typing import List, Optional

from app.domain.users.repositories import UserRepository
from app.application.users.dtos import UserDto
from app.application.users.commands import CreateUserCommand
from app.application.users.queries import GetUserByIdQuery, ListUsersQuery


def _to_dto(user) -> UserDto:
    return UserDto(id=user.id, name=user.name, email=user.email)


class CreateUserHandler:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    async def handle(self, command: CreateUserCommand) -> int:
        user = await self._repo.add(name=command.name, email=command.email)
        return user.id


class GetUserByIdHandler:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    async def handle(self, query: GetUserByIdQuery) -> Optional[UserDto]:
        user = await self._repo.get_by_id(query.user_id)
        if not user:
            return None
        return _to_dto(user)


class ListUsersHandler:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    async def handle(self, query: ListUsersQuery) -> List[UserDto]:
        users = await self._repo.get_all()
        return [_to_dto(u) for u in users]
