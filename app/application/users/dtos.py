from dataclasses import dataclass


@dataclass(frozen=True)
class UserDto:
    id: int
    name: str
    email: str
