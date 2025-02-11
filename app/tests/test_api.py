"""Модуль тестов эндпоинтов"""

from fastapi.testclient import TestClient
from httpx import Response

from app.database.models import Category, Product
from app.main import app
from app.tests.fixtures import get_session


DATA_PRODUCT_DETAIL: dict = {
    "id": 0,
    "name": "",
    "description": "",
    "image": ""
}


def test_get_category_ok(get_session) -> None:
    qs = get_session.query(Category).order_by(Category.name).all()
    response_dict = dict()
    response_dict["categories"] = [category.to_json() for category in qs]
    get_session.close()

    with TestClient(app) as client:
        response = client.get(
            url="api/categories",
        )
    assert response.status_code == 200
    assert response.json() == response_dict


def test_get_products_by_category_ok(get_session) -> None:
    qs = (get_session.query(Product).join(Category).
          filter(Category.name =="хлеб").
          order_by(Product.name).all())

    response_dict = dict()
    response_dict["products"] = [product.to_json() for product in qs]
    get_session.close()

    with TestClient(app) as client:
        response = client.get(
            url="api/categories/<str:category_name>",
            params={"category_name": "хлеб"}
        )
    assert response.status_code == 200
    assert response.json().get("id") == response_dict.get("id")
    assert response.json().get("name") == response_dict.get("name")


def test_get_product_details_ok(get_session) -> None:
    qs = get_session.query(Product).filter(Product.name == 'белый').one()
    get_session.close()

    print(qs)
    with TestClient(app) as client:
        response = client.get(
            url="api/products/<str:product_name>",
            params={"product_name": "белый"}
        )
    assert response.status_code == 200
    assert response.json().get("name") == qs.to_json().get("name")
    assert response.json().get("description") == qs.to_json().get("description")


def test_get_product_details_fail() -> None:
    with TestClient(app) as client:
        response = client.get(
            url="api/products/<str:product_name>",
            params={"product_name": "бй"}
        )
    assert response.status_code == 200
    assert response.json() == DATA_PRODUCT_DETAIL
