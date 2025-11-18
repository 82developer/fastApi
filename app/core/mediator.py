# app/core/mediator.py

from __future__ import annotations

from typing import Any, Dict, Generic, Type, TypeVar, Protocol

from dependency_injector import providers


TRequest = TypeVar("TRequest")
TResponse = TypeVar("TResponse")


class RequestHandler(Protocol, Generic[TRequest, TResponse]):
    async def handle(self, request: TRequest) -> TResponse:
        ...


# 👇 Relaxed type: any provider that returns *something* with .handle(...)
HandlerProvider = providers.Provider[Any]


class Mediator:
    """
    Simple async Mediator with DI-friendly handler registration.

    Handlers must implement: async def handle(self, request) -> response
    """

    def __init__(self) -> None:
        # Dict[RequestType, Provider[handler_instance]]
        self._handlers: Dict[Type[Any], HandlerProvider] = {}

    def register(self, request_type: Type[TRequest], handler_provider: HandlerProvider) -> None:
        if request_type in self._handlers:
            raise ValueError(f"Handler already registered for {request_type.__name__}")
        self._handlers[request_type] = handler_provider

    async def send(self, request: TRequest) -> TResponse:
        request_type = type(request)
        if request_type not in self._handlers:
            raise ValueError(f"No handler registered for {request_type.__name__}")

        provider = self._handlers[request_type]
        handler = provider()  # CreateUserHandler / GetUserByIdHandler / etc.

        # Optional runtime safety check:
        # if not hasattr(handler, "handle"):
        #     raise TypeError(f"Handler for {request_type.__name__} has no 'handle' method")

        return await handler.handle(request)  # type: ignore[no-any-return]
