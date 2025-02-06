"""habits routs processing module"""

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
    """the router returns the habits of the current user"""
    res = await get_product_detail_db(product_id)
    return res


# @router.get(
#     path="/<int:habit_id>",
#     response_description="habits_sch.HabitsSchemas",
#     response_model=HabitSchemas,
#     status_code=200,
# )
# async def get_details_habit(
#     current_user: Annotated[InfoUserSchemas, Depends(get_current_active_user)],
#     habit_id: int,
# ) -> dict[str, int | str] | Any:
#     """the router returns the details of the habit"""
#     res = await get_detail_habit_by_telegram_id_db(current_user.id, habit_id)
#     if not res:
#         return DEF_HABIT
#     else:
#         return res[0].to_json()
#
#
# @router.post(
#     path="/",
#     response_description="habits_sch.Habit",
#     response_model=HabitSchemas,
#     status_code=201,
# )
# async def create_habit(
#     current_user: Annotated[InfoUserSchemas, Depends(get_current_active_user)],
#     data: CreateHabitSchemas,
# ) -> dict:
#     """the router creates new habits"""
#     data = data.model_dump()
#     data.update({"user_id": current_user.id})
#     data["alert_time"] = data["alert_time"].replace(second=0, microsecond=0)
#     habit = await create_habit_db(data)
#     return habit.to_json()
#
#
# @router.delete(path="/<int:habit_id>", status_code=204)
# async def delete_habit(
#     current_user: Annotated[InfoUserSchemas, Depends(get_current_active_user)],
#     habit_id: int,
# ) -> None:
#     """the router deletes the habit"""
#     await delete_habit_db(current_user.id, habit_id)
#
#
# @router.patch(
#     path="/<int:habit_id>",
#     response_description="habits_sch.HabitSchemas",
#     response_model=HabitSchemas,
#     status_code=201,
# )
# async def patch_habit(
#     current_user: Annotated[InfoUserSchemas, Depends(get_current_active_user)],
#     habit_id: int,
#     data: PatchHabitSchemas,
# ) -> dict[str, int | str] | bool:
#     """the router updates the habit"""
#     dict_data = data.model_dump()
#     if dict_data.get("alert_time"):
#         dict_data["alert_time"] = dict_data["alert_time"].replace(
#             second=0, microsecond=0
#         )
#     res = await patch_habit_db(current_user.id, habit_id, dict_data)
#     if not res:
#         return DEF_HABIT
#     return res
#
#
# @router.post(
#     path="/<int:habit_id>/fulfilling",
#     response_description="habits_sch.FulfilHabitSchemas",
#     response_model=HabitSchemas,
#     status_code=201,
# )
# async def fulfilling_habit(
#     current_user: Annotated[InfoUserSchemas, Depends(get_current_active_user)],
#     habit_id: int,
# ) -> dict[Any, Any]:
#     """the router fulfilling a habit"""
#     res = await fulfilling_habit_db(current_user.id, habit_id)
#     if not res:
#         return DEF_HABIT
#     return res.to_json()
