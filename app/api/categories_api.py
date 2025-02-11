"""Модуль обработчик API категорий"""

from typing import Any

from fastapi import APIRouter

from app.database.transactions import (
    get_categories_db,
    get_products_by_category_db,
)
from app.schemas.categories_sch import ListCategorySchemas
from app.schemas.products_sch import ListProductSchemas

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get(
    path="/",
    response_description="categories_sch.ListCategorySchemas",
    response_model=ListCategorySchemas,
    response_model_exclude_unset=True,
    status_code=200,
)
async def get_categories(
) -> dict[str, list[Any]]:
    """
    Хендлер для эндпоинта /categories.
    При запросе возвращает все категории товара.
    """
    res = await get_categories_db()
    return {"categories": [category[0].to_json() for category in res]}


@router.get(
    path="/<str:category_name>",
    response_description="products_sch.ListProductSchemas",
    response_model=ListProductSchemas,
    response_model_exclude_unset=True,
    status_code=200,
)
async def get_products_by_category(
    category_name: str
) -> dict[str, list[Any]]:
    """
    Хендлер для эндпоинта /categories/"наименование_категории".
    При запросе необходимо передать в параметрах
    "наименование_категории" возвращает все продукта
    по данной категории.
    """
    category_name = bytes(category_name, encoding="UTF-8").decode().lower()
    res = await get_products_by_category_db(category_name)
    return {"products": [products[0].to_json() for products in res]}
