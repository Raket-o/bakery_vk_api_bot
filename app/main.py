"""the main module"""

from contextlib import asynccontextmanager

import uvicorn
from asyncpg.exceptions import InvalidCatalogNameError
from fastapi import APIRouter, FastAPI

from app.api.categories_api import router as categories_api_router
# from app.api.products_api import router as products_api_router
from app.database.connect import Base, engine, session
from app.database.transactions import create_db
from app.utils.filling_databases import filling_categories

from config_data.config import DB_TESTS


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as _:
            pass

    except InvalidCatalogNameError:
        await create_db()

    finally:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        if DB_TESTS:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.drop_all)
                await conn.run_sync(Base.metadata.create_all)
            await filling_categories()

        else:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)

    yield
    await session.close()
    await engine.dispose()


app = FastAPI(lifespan=lifespan)

api_router = APIRouter(prefix="/api")
api_router.include_router(categories_api_router)
# api_router.include_router(products_api_router)

app.include_router(api_router)


if __name__ == "__main__":
    # uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    uvicorn.run("main:app", reload=True)
