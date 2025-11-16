# app/main.py

from fastapi import FastAPI

from .api import router as users_router   # <-- relative import


app = FastAPI(
    title="FastAPI + dependency_injector Example",
    version="1.0.0",
)

# Register routes
app.include_router(users_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",   # <-- important: app.main, not just main
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
