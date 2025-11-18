from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from dependency_injector.wiring import inject, Provide

from app.core.container import AppContainer
from app.core.mediator import Mediator
from app.application.users.messages import (
    CreateUserCommand,
    GetUserByIdQuery,
    ListUsersQuery,
)
from app.domain.users.entities import User


router = APIRouter(prefix="/users", tags=["users"])


# ----- Pydantic Schemas ----- #

class UserResponse(BaseModel):
    id: int
    name: str
    email: str


class CreateUserRequest(BaseModel):
    name: str
    email: str


def to_user_response(user: User) -> UserResponse:
    return UserResponse(id=user.id, name=user.name, email=user.email)


# ----- Endpoints using Mediator ----- #

@router.post("/", response_model=int, status_code=201)
@inject
async def create_user(
    payload: CreateUserRequest,
    mediator: Mediator = Depends(Provide[AppContainer.mediator]),
) -> int:
    """
    Command endpoint: create user.
    CQRS: write side -> CreateUserCommand.
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
    Query endpoint: list users.
    CQRS: read side -> ListUsersQuery.
    """
    query = ListUsersQuery()
    users = await mediator.send(query)
    return [to_user_response(u) for u in users]


@router.get("/{user_id}", response_model=UserResponse)
@inject
async def get_user(
    user_id: int,
    mediator: Mediator = Depends(Provide[AppContainer.mediator]),
) -> UserResponse:
    """
    Query endpoint: get user by id.
    CQRS: read side -> GetUserByIdQuery.
    """
    query = GetUserByIdQuery(user_id=user_id)
    user = await mediator.send(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return to_user_response(user)
