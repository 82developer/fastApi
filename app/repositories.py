from typing import Protocol,List, Optional
from functools import lru_cache

class User:
    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name

class IUserRepository(Protocol):
    def get_all(self)->List[User]:...
    def get_by_id(self, user_id: int)->Optional[User]:...
    def add(self, name: str)-> User:...

class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self._db:List[User]=[]
        self._next_id=1

    def get_all(self) -> List[User]:
        return self._db
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        return next((u for u in self._db if u.id == user_id), None)

    def add(self, name: str) -> User:
        user = User(self._next_id,name)
        self._db.append(user)
        self._next_id =+ 1
        return user

@lru_cache
def get_user_repository() -> IUserRepository:
    return InMemoryUserRepository()
