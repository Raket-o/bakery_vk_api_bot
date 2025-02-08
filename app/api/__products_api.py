

from typing import Annotated, Any, Dict, List

from fastapi import APIRouter, Depends

# from app.database.models import Product
from app.database.transactions import get_product_detail_db
# from app.schemas.categories_sch import CategorySchemas, CategoryIdSchemas, ListCategorySchemas
from app.schemas.products_sch import ProductSchemas


router = APIRouter(prefix="/products", tags=["products"])


@router.get(
    path="/<int:product_id>",
    response_description="products_sch.ProductSchemas",
    response_model=ProductSchemas,
    response_model_exclude_unset=True,
    status_code=200,
)
async def get_product_detail(
    product_id: int
) -> ProductSchemas:

    res = await get_product_detail_db(product_id)
    return res
