"""module for working with transactions"""

import asyncpg
from config_data.config import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_PORT,
    DB_TESTS,
    DB_USER
)
from sqlalchemy import update
from sqlalchemy.future import select

from app.database.connect import session
from app.database.models import Category, Product


async def create_db() -> None:
    """the function creates a database"""
    db_name = "bakery_vk_api_bot_tests" if DB_TESTS else DB_NAME
    cursor = await asyncpg.connect(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"
    )
    await cursor.execute(f"CREATE DATABASE {db_name};")


async def get_categories_db() -> list[Category]:

    qs = await session.execute(select(Category))
    return qs.all()


async def get_products_by_category_db(category: int) -> list[Category]:

    qs = await session.execute(select(Product).filter(Product.category_id == category))
    return qs.all()


async def get_product_detail_db(id: int) -> list[Category]:

    qs = await session.execute(select(Product).filter(Product.id == id))
    return qs.one()
