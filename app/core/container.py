# app/core/container.py

from dependency_injector import containers, providers

from app.core.config import Settings
from app.domain.users.services import UserService
from app.infrastructure.users.repositories import InMemoryUserRepository


class AppContainer(containers.DeclarativeContainer):
    """
    Main application container.
    It composes all services, repositories, config, etc.
    """

    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.users",  # modules where we will inject dependencies
        ]
    )

    # --- Configuration ---
    config = providers.Singleton(Settings)

    # --- Repositories ---
    user_repository = providers.Singleton(InMemoryUserRepository)

    # --- Services ---
    user_service = providers.Factory(
        UserService,
        repository=user_repository,
    )
