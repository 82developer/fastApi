from typing import Protocol, Optional, List
from app.repositories import IUserRepository, User

class IUserService(Protocol):
    def list_users(self) -> List[User]:...
    def create_user(self, name: str) -> User:...
    def find(self, user_id: int) -> Optional[User]: ...

class UserService(IUserService):
    def __init__(self, repo: IUserRepository):
        self._repo = repo
    
    def list_users(self) -> List[User]:
        return self._repo.get_all()  

    def create_user(self, name: str) -> User:
        return self._repo.add(name)

    def find(self, user_id: int) -> Optional[User]:
        return self._repo.get_by_id(user_id)




