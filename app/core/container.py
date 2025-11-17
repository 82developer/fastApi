# app/core/container.py

from dependency_injector import containers, providers

from app.core.config import Settings
from app.domain.users.services import UserService
from app.domain.products.services import ProductService
from app.infrastructure.users.repositories import InMemoryUserRepository
from app.infrastructure.products.repositories import InMemoryProductRepository


class AppContainer(containers.DeclarativeContainer):
    """
    Main application container.
    It composes all services, repositories, config, etc.
    """

    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.users",  # modules where we will inject dependencies
            "app.api.v1.products",
        ]
    )

    # --- Configuration ---
    config = providers.Singleton(Settings)

    # --- Repositories ---
    user_repository = providers.Singleton(InMemoryUserRepository)
    product_repository = providers.Singleton(InMemoryProductRepository)

    # --- Services ---
    user_service = providers.Factory(
        UserService,
        repository=user_repository,
    )

    product_service = providers.Factory(
        ProductService,
        repository=product_repository,
        )
