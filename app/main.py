# app/main.py

from fastapi import FastAPI

from app.api.v1.users import router as users_router
from app.core.container import AppContainer


def create_app() -> FastAPI:
    container = AppContainer()

    # If you need to customize config:
    # settings = container.config()
    # settings.environment = "production"   # or from elsewhere

    app = FastAPI(
        title="Professional FastAPI + dependency_injector App",
        version="1.0.0",
    )

    # Attach container to app for access in middlewares, tests, etc.
    app.state.container = container

    # Wire the container with the FastAPI app modules
    container.wire(modules=["app.api.v1.users"])

    # Include routers
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
