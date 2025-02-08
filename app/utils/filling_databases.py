from sqlalchemy.future import select

from app.database.connect import engine, session
from app.database.models import Category, Product


async def filling_categories() -> None:
    """the function of filling the database with data of this"""
    async with engine.begin() as conn:
        res = await session.execute(select(Category))
        if not len(res.all()):
            categories = {
                Category(id=1, name="Хлеб"),
                Category(id=2, name="Булки"),
                Category(id=3, name="Печенье"),
            }
            session.add_all(categories)

        res = await session.execute(select(Product))
        if not len(res.all()):
            products = {
                Product(name="Бородинский", description="Бородинский", category_id=1),
                Product(name="Белый", description="Белый", category_id=1),
                Product(name="Столичный", description="Столичный", category_id=1),

                Product(name="Булка с маком", description="Булка с маком", category_id=2),
                Product(name="Булка с грушей", description="Булка с грушей", category_id=2),
                Product(name="Булка с яблоком", description="Булка с яблоком", category_id=2),

                Product(name="Буратино", description="Буратино", category_id=3),
                Product(name="Крендельки", description="Крендельки", category_id=3),
                Product(name="К чаю", description="К чаю", category_id=3),

            }
            session.add_all(products)

        await session.commit()
