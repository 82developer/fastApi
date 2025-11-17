# app/api/v1/users.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from dependency_injector.wiring import inject, Provide

from app.core.container import AppContainer
from app.domain.users.entities import User
from app.domain.users.services import UserService


router = APIRouter(prefix="/users", tags=["users"])


# ----- Pydantic Schemas ----- #

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    @classmethod
    def from_entity(cls, user: User) -> "UserResponse":
        return cls(id=user.id, name=user.name, email=user.email)


class UserCreateRequest(BaseModel):
    name: str
    email: str


# ----- Endpoints with DI ----- #

@router.get("/", response_model=List[UserResponse])
@inject
def list_users(
    service: UserService = Depends(Provide[AppContainer.user_service]),
):
    """
    GET /users
    Returns all users.
    """
    users = service.list_users()
    return [UserResponse.from_entity(u) for u in users]


@router.get("/{user_id}", response_model=UserResponse)
@inject
def get_user(
    user_id: int,
    service: UserService = Depends(Provide[AppContainer.user_service]),
):
    """
    GET /users/{user_id}
    """
    user = service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.from_entity(user)


@router.post("/", response_model=UserResponse, status_code=201)
@inject
def create_user(
    payload: UserCreateRequest,
    service: UserService = Depends(Provide[AppContainer.user_service]),
):
    """
    POST /users
    """
    user = service.create_user(name=payload.name, email=payload.email)
    return UserResponse.from_entity(user)
