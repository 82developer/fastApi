# app/api.py

from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException

from .services import UserService          # <-- relative import
from .container import Container           # <-- relative import


router = APIRouter()

# Create container instance (simple version)
container = Container()


def get_user_service() -> UserService:
    """
    Resolver used by FastAPI Depends() to get UserService from the container.
    """
    return container.user_service()


@router.get("/users", response_model=List[Dict[str, str]])
def get_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_all_users()


@router.get("/users/{user_id}", response_model=Dict[str, str])
def get_user(user_id: str, user_service: UserService = Depends(get_user_service)):
    user = user_service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", response_model=Dict[str, str])
def create_user(
    payload: Dict[str, str],
    user_service: UserService = Depends(get_user_service),
):
    name = payload.get("name")
    email = payload.get("email")

    if not name or not email:
        raise HTTPException(status_code=400, detail="Name and email are required")

    user = user_service.create_user(name=name, email=email)
    return user
