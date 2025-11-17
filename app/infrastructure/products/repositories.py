# app/infrastructure/products/repositories.py

from typing import List, Optional

from app.domain.products.entities import Product
from app.domain.products.repositories import ProductRepository


class InMemoryProductRepository(ProductRepository):
    """Simple in-memory product repository."""

    def __init__(self) -> None:
        self._products: List[Product] = [
            Product(id=1, name="Keyboard", price=50.0),
            Product(id=2, name="Monitor", price=200.0),
        ]

    def get_all(self) -> List[Product]:
        return list(self._products)

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return next((p for p in self._products if p.id == product_id), None)

    def add(self, product: Product) -> Product:
        self._products.append(product)
        return product
