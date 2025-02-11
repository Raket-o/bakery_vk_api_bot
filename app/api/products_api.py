"""Модуль обработчик API продуктов"""


from typing import Annotated, Any, Dict, List

from fastapi import APIRouter, Depends

from app.database.models import Product
from app.database.transactions import get_product_detail_db
from app.schemas.products_sch import ProductSchemas


router = APIRouter(prefix="/products", tags=["products"])


@router.get(
    path="/<str:product_name>",
    response_description="products_sch.ProductSchemas",
    response_model=ProductSchemas,
    response_model_exclude_unset=True,
    status_code=200,
)
async def get_product_detail(
    product_name: str
) -> dict[str, str | int] | Product:
    """
    Хендлер для эндпоинта /products/"наименование_продукта". При запросе
    необходимо передать в параметрах "наименование_продукта" возвращает все продукта по данной категории.
    """
    product_name = bytes(product_name, encoding="UTF-8").decode().lower()
    res = await get_product_detail_db(product_name)
    if not res:
        return {"id": 0, "name": "", "description": "", "image": ""}
    return res
