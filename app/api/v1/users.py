from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from dependency_injector.wiring import inject, Provide

from app.core.container import AppContainer
from app.core.mediator import Mediator
from app.application.users.commands import CreateUserCommand
from app.application.users.queries import GetUserByIdQuery, ListUsersQuery
from app.application.users.dtos import UserDto


router = APIRouter(prefix="/users", tags=["users"])


# ----- Pydantic schemas for HTTP layer ----- #

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    @classmethod
    def from_dto(cls, dto: UserDto) -> "UserResponse":
        return cls(id=dto.id, name=dto.name, email=dto.email)


class CreateUserRequest(BaseModel):
    name: str
    email: str


# ----- Endpoints using Mediator (CQRS) ----- #

@router.post("/", response_model=int, status_code=201)
@inject
async def create_user(
    payload: CreateUserRequest,
    mediator: Mediator = Depends(Provide[AppContainer.mediator]),
) -> int:
    """
    Command endpoint: create a new user.
    CQRS: write side via CreateUserCommand.
    """
    cmd = CreateUserCommand(name=payload.name, email=payload.email)
    user_id = await mediator.send(cmd)
    return user_id


@router.get("/", response_model=List[UserResponse])
@inject
async def list_users(
    mediator: Mediator = Depends(Provide[AppContainer.mediator]),
) -> List[UserResponse]:
    """
    Query endpoint: list all users.
    CQRS: read side via ListUsersQuery.
    """
    query = ListUsersQuery()
    dtos = await mediator.send(query)
    return [UserResponse.from_dto(dto) for dto in dtos]


@router.get("/{user_id}", response_model=UserResponse)
@inject
async def get_user(
    user_id: int,
    mediator: Mediator = Depends(Provide[AppContainer.mediator]),
) -> UserResponse:
    """
    Query endpoint: get user by id.
    CQRS: read side via GetUserByIdQuery.
    """
    query = GetUserByIdQuery(user_id=user_id)
    dto = await mediator.send(query)

    if dto is None:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse.from_dto(dto)
