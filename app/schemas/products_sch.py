"""the schematics module for answering about the product"""

from typing import List

from pydantic import BaseModel


class ProductIdSchemas(BaseModel):
    id: int


class ProductSchemas(ProductIdSchemas):
    name: str
    description: str


class ListProductSchemas(BaseModel):
    products: List[ProductSchemas]
