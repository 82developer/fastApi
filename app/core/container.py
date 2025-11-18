from dependency_injector import containers, providers

from app.core.mediator import Mediator
from app.domain.users.repositories import UserRepository
from app.infrastructure.users.repositories import InMemoryUserRepository
from app.application.users.handlers import (
    CreateUserHandler,
    GetUserByIdHandler,
    ListUsersHandler,
)
from app.application.users.messages import (
    CreateUserCommand,
    GetUserByIdQuery,
    ListUsersQuery,
)


class AppContainer(containers.DeclarativeContainer):
    """
    Application DI container.
    """

    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.users",  # modules where we will inject Mediator
        ]
    )

    # Repositories
    user_repository: providers.Provider[UserRepository] = providers.Singleton(
        InMemoryUserRepository
    )

    # Handlers (each handler gets repo injected)
    create_user_handler = providers.Factory(
        CreateUserHandler,
        repo=user_repository,
    )

    get_user_by_id_handler = providers.Factory(
        GetUserByIdHandler,
        repo=user_repository,
    )

    list_users_handler = providers.Factory(
        ListUsersHandler,
        repo=user_repository,
    )

    # Mediator
    mediator = providers.Singleton(Mediator)
