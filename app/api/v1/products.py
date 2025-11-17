# app/api/v1/products.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from dependency_injector.wiring import inject, Provide

from app.core.container import AppContainer
from app.domain.products.entities import Product
from app.domain.products.services import ProductService


router = APIRouter(prefix="/products", tags=["products"])


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

    @classmethod
    def from_entity(cls, product: Product) -> "ProductResponse":
        return cls(id=product.id, name=product.name, price=product.price)


class ProductCreateRequest(BaseModel):
    name: str
    price: float


@router.get("/", response_model=List[ProductResponse])
@inject
def list_products(
    service: ProductService = Depends(Provide[AppContainer.product_service]),
):
    products = service.list_products()
    return [ProductResponse.from_entity(p) for p in products]


@router.get("/{product_id}", response_model=ProductResponse)
@inject
def get_product(
    product_id: int,
    service: ProductService = Depends(Provide[AppContainer.product_service]),
):
    product = service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponse.from_entity(product)


@router.post("/", response_model=ProductResponse, status_code=201)
@inject
def create_product(
    payload: ProductCreateRequest,
    service: ProductService = Depends(Provide[AppContainer.product_service]),
):
    product = service.create_product(name=payload.name, price=payload.price)
    return ProductResponse.from_entity(product)
