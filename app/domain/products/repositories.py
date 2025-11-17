# app/domain/products/repositories.py

from abc import ABC, abstractmethod
from typing import List, Optional

from .entities import Product


class ProductRepository(ABC):
    """Abstraction of product persistence."""

    @abstractmethod
    def get_all(self) -> List[Product]:
        ...

    @abstractmethod
    def get_by_id(self, product_id: int) -> Optional[Product]:
        ...

    @abstractmethod
    def add(self, product: Product) -> Product:
        ...

