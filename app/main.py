from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from app.repositories import get_user_repository,IUserRepository
from app.services import UserService,IUserService
from app.schemas import UserIn, UserOut

app = FastAPI(title="IoC with FastApi")

def get_user_service(
        repo: Annotated[IUserRepository, Depends( get_user_repository)]) -> IUserService:
    return UserService(repo)
@app.get("/users", response_model=list[UserOut])
def list_users(
        service:Annotated[IUserService,Depends(get_user_service)]
        ):
    return [UserOut(id=u.id, name=u.name) for u in service.list_users()]

@app.post("/users", response_model=UserOut, status_code=201)
def create_user(
        payload: UserIn,
        service: Annotated[IUserService, Depends(get_user_service)]
        ):
    user = service.create_user(payload.name)
    return UserOut(id = user.id, name=user.name)

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(
        user_id: int,
        service: Annotated[IUserService, Depends(get_user_service)]
        ):
    user = service.find(user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return UserOut(id=user.id, name=user.name)
