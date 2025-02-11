"""Модуль схем товара"""


from typing import List

from pydantic import BaseModel, Base64Bytes


class ProductIdSchemas(BaseModel):
    id: int


class ProductNameSchemas(ProductIdSchemas):
    name: str


class ProductSchemas(ProductNameSchemas):
    description: str
    image: Base64Bytes


class ListProductSchemas(BaseModel):
    products: List[ProductNameSchemas]
