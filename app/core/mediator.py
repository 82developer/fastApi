from typing import Any, Awaitable, Dict, Type

from dependency_injector import providers


class Mediator:
    """
    Simple async Mediator.

    - Handlers are provided via dependency_injector providers.
    - Each handler is a callable: async def __call__(request) -> response
    """

    def __init__(self) -> None:
        # Map: RequestType -> provider of handler
        self._handlers: Dict[Type[Any], providers.Provider] = {}

    def register(self, request_type: Type[Any], handler_provider: providers.Provider) -> None:
        if request_type in self._handlers:
            raise ValueError(f"Handler already registered for {request_type}")
        self._handlers[request_type] = handler_provider

    async def send(self, request: Any) -> Any:
        request_type = type(request)
        if request_type not in self._handlers:
            raise ValueError(f"No handler registered for {request_type}")
        provider = self._handlers[request_type]
        handler = provider()  # get handler instance from DI container
        return await handler(request)
