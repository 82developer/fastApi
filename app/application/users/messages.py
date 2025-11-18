from dataclasses import dataclass

# ---- Commands ---- #

@dataclass
class CreateUserCommand:
    name: str
    email: str


# ---- Queries ---- #

@dataclass
class GetUserByIdQuery:
    user_id: int


@dataclass
class ListUsersQuery:
    pass
