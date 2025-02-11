"""Обработчик состояния main_menu"""

from keyboards.create_keyboard import create_keyboard_v1
from utils.manager_api import ApiManager
from utils.send_message import sending_messages

api = ApiManager


def processing_main_menu(user_state, user_id: int) -> None:
    """
    Функция запускает при состоянии main_menu.
    Делает запрос с сервера бекэнда всех категорий,
    выводит клавиатуру с категориями и меняет
    состояние пользователя на view_category
    """
    response = api.send_get(url="categories/")
    categories = response.json().get("categories")
    buttons = [category.get("name").capitalize() for category in categories]

    sending_messages(
        user_id=user_id,
        message='Выберите категорию:',
        keyboard=create_keyboard_v1(buttons),
    )
    user_state.view_category()
