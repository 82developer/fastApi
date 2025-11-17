# app/domain/products/entities.py

from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float
