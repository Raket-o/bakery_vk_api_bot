"""Модуль работы с запросами к базе данных"""

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
    """
    Функция создаёт базу данных
    """
    db_name = DB_NAME + "_tests" if DB_TESTS else DB_NAME
    cursor = await asyncpg.connect(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"
    )
    await cursor.execute(f"CREATE DATABASE {db_name};")


async def get_categories_db() -> list[Category]:
    """
    Функция возвращает все категории
    """
    qs = await session.execute(select(Category).order_by(Category.name))
    return qs.all()


async def get_products_by_category_db(category: str) -> list[Category]:
    """
    Функция возвращает все товары по определённой переданной категории
    """
    qs = await session.execute(select(Product).join(Category, Category.id == Product.category_id).filter(Category.name == category).order_by(Product.name))
    return qs.all()


async def get_product_detail_db(product_name: str) -> Product:
    """
    Функция возвращает всё информацию о товаре
    """
    qs = await session.execute(select(Product).filter(Product.name == product_name))
    return qs.scalar()
