"""Модуль схем товара"""


from typing import List

from pydantic import Base64Bytes, BaseModel


class ProductIdSchemas(BaseModel):
    id: int


class ProductNameSchemas(ProductIdSchemas):
    name: str


class ProductSchemas(ProductNameSchemas):
    description: str
    image: Base64Bytes


class ListProductSchemas(BaseModel):
    products: List[ProductNameSchemas]
