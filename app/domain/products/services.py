# app/domain/products/services.py

from typing import List, Optional

from .entities import Product
from .repositories import ProductRepository


class ProductService:
    """Business logic for products."""

    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def list_products(self) -> List[Product]:
        return self._repository.get_all()

    def get_product(self, product_id: int) -> Optional[Product]:
        return self._repository.get_by_id(product_id)

    def create_product(self, name: str, price: float) -> Product:
        products = self._repository.get_all()
        next_id = (max((p.id for p in products), default=0) + 1) if products else 1
        product = Product(id=next_id, name=name, price=price)
        return self._repository.add(product)
