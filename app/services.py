# app/services.py

from typing import List, Dict


class UserService:
    """
    Simple service that manages users in memory.
    """

    def __init__(self) -> None:
        self._users: List[Dict[str, str]] = [
            {"id": "1", "name": "Alice", "email": "alice@example.com"},
            {"id": "2", "name": "Bob", "email": "bob@example.com"},
        ]

    def get_all_users(self) -> List[Dict[str, str]]:
        return self._users

    def get_user_by_id(self, user_id: str) -> Dict[str, str] | None:
        return next((u for u in self._users if u["id"] == user_id), None)

    def create_user(self, name: str, email: str) -> Dict[str, str]:
        new_id = str(len(self._users) + 1)
        user = {"id": new_id, "name": name, "email": email}
        self._users.append(user)
        return user
