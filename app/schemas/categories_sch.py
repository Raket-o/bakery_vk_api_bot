"""Модуль схем категорий"""

from typing import List

from pydantic import BaseModel


class CategoryIdSchemas(BaseModel):
    id: int


class CategorySchemas(CategoryIdSchemas):
    name: str


class ListCategorySchemas(BaseModel):
    categories: List[CategorySchemas]
