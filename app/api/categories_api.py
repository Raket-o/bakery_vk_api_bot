

from typing import Annotated, Any, Dict, List

from fastapi import APIRouter, Depends

from app.database.models import Category
from app.database.transactions import (
    get_categories_db,
    get_product_detail_db,
    get_products_by_category_db,
)
from app.schemas.categories_sch import CategorySchemas, CategoryIdSchemas, ListCategorySchemas
from app.schemas.products_sch import ListProductSchemas, ProductSchemas


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

    res = await get_categories_db()
    return {"categories": [category[0].to_json() for category in res]}


@router.get(
    path="/<int:category_id>",
    response_description="products_sch.ListProductSchemas",
    response_model=ListProductSchemas,
    response_model_exclude_unset=True,
    status_code=200,
)
async def get_products_by_category(
    category_id: int
) -> dict[str, list[Any]]:

    res = await get_products_by_category_db(category_id)
    return {"products": [products[0].to_json() for products in res]}
