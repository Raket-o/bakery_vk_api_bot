"""Обработчик состояния viewing_category"""

from keyboards.create_keyboard import create_keyboard_v1
from utils.manager_api import ApiManager
from utils.send_message import sending_messages


api = ApiManager


def processing_viewing_category(user_state, user_id: int, message: str) -> None:
    """
    Функция запускает при состоянии viewing_category.
    Делает запрос с сервера бекэнда продуктов по выбранной категории,
    выводит клавиатуру с продуктами и меняет состояния пользователя на view_product.
    Если продуктов нет, то возвращает пользователю
    текст "Товаров в этой категории пока нет"
    """
    category_name = message.lower()
    user_state.set_category(category_name)
    response = api.send_get(url="categories/<str:category_name>", params={"category_name": category_name})
    products = response.json().get("products")
    if products:
        buttons = [product.get("name").capitalize() for product in products]
        sending_messages(
            user_id,
            f'Товары в категории "{message.capitalize()}":',
            create_keyboard_v1(buttons, one_time=True, additional_btn=True)
        )
        user_state.view_product()

    else:
        sending_messages(
            user_id,
            "Товаров в этой категории пока нет",
        )
