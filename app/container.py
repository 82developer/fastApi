# app/container.py

from dependency_injector import containers, providers

from .services import UserService  # <-- note the dot .services


class Container(containers.DeclarativeContainer):
    """
    Dependency Injector container for our app.
    """

    user_service = providers.Singleton(
        UserService
    )
