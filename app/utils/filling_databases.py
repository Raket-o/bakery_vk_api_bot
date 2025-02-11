"""Модуль для предзаполнения базы данных информацией"""

import base64
from pathlib import Path

import aiofiles
from sqlalchemy.future import select

from app.database.connect import engine, session
from app.database.models import Category, Product

BASE_DIR = Path(__file__).resolve().parent


async def encoded_images_to_string(path_image: str) -> base64:
    """
    Функция принимает путь до файла(картинки)
    и возвращает эту картинку в байтах
    """
    async with aiofiles.open(path_image, "rb") as file:
        data = await file.read()
    return base64.b64encode(data)


async def filling_categories() -> None:
    """
    Функция заполняет базу данных информацией
    """
    async with engine.begin() as _:
        res = await session.execute(select(Category))
        if not len(res.all()):
            categories = {
                Category(id=1, name="хлеб"),
                Category(id=2, name="булочки"),
                Category(id=3, name="печенье"),
                Category(id=4, name="злаковые"),
            }
            session.add_all(categories)

        res = await session.execute(select(Product))

        if not len(res.all()):
            products = {
                Product(
                    name="бородинский",
                    description="бородинский",
                    image=await encoded_images_to_string(str(BASE_DIR) + "/image_prods/bread_borodin.jpg"),
                    category_id=1
                ),
                Product(
                    name="белый",
                    description="белый",
                    image=await encoded_images_to_string(str(BASE_DIR) + "/image_prods/bread_white.jpg"),
                    category_id=1
                ),
                Product(
                    name="столичный",
                    description="столичный",
                    image=await encoded_images_to_string(str(BASE_DIR) + "/image_prods/bread_stolich.jpg"),
                    category_id=1
                ),

                Product(
                    name="с маком",
                    description="с маком",
                    image=await encoded_images_to_string(str(BASE_DIR) + "/image_prods/bulka_s_makom.jpg"),
                    category_id=2),
                Product(
                    name="с грушей",
                    description="с грушей",
                    image=await encoded_images_to_string(str(BASE_DIR) + "/image_prods/bulka_s_grushei.jpg"),
                    category_id=2
                ),
                Product(
                    name="с яблоком",
                    description="с яблоком",
                    image=await encoded_images_to_string(str(BASE_DIR) + "/image_prods/bulka_s_yablokom.jpg"),
                    category_id=2
                ),

                Product(
                    name="золотой ключик",
                    description="золотой ключик",
                    image=await encoded_images_to_string(str(BASE_DIR) + "/image_prods/pechen_zol_kluch.jpg"),
                    category_id=3
                ),
                Product(
                    name="крендельки",
                    description="крендельки",
                    image=await encoded_images_to_string(str(BASE_DIR) + "/image_prods/pechen_krendelki.jpg"),
                    category_id=3
                ),
                Product(
                    name="к чаю",
                    description="к чаю",
                    image=await encoded_images_to_string(str(BASE_DIR) + "/image_prods/pechen_k_chau.jpg"),
                    category_id=3
                ),
            }
            session.add_all(products)

            await session.commit()
