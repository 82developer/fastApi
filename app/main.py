from fastapi import FastAPI

from app.api.v1.users import router as users_router
from app.core.container import AppContainer
from app.core.mediator import Mediator
from app.application.users.commands import CreateUserCommand
from app.application.users.queries import GetUserByIdQuery, ListUsersQuery


def create_app() -> FastAPI:
    container = AppContainer()

    app = FastAPI(
        title=container.settings().app_name,
        version="1.0.0",
    )

    # Attach container (optional but useful for tests/infra)
    app.state.container = container

    # Wire DI into API modules
    container.wire(modules=["app.api.v1.users"])

    # --- Register handlers in Mediator (central place) ---
    mediator: Mediator = container.mediator()

    mediator.register(CreateUserCommand, container.create_user_handler)
    mediator.register(GetUserByIdQuery, container.get_user_by_id_handler)
    mediator.register(ListUsersQuery, container.list_users_handler)

    # --- Register routers ---
    app.include_router(users_router)

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
