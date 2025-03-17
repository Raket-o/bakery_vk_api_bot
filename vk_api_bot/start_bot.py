"""Главный модуль запуска VK_API бота"""

import sys
sys.path.append(".")

from handlers.custom_handlers.handler_init import processing_init
from handlers.custom_handlers.handler_main_menu import processing_main_menu
from handlers.custom_handlers.handler_viewing_category import \
    processing_viewing_category
from handlers.custom_handlers.handler_viewing_product import \
    processing_viewing_product
from loader import LONGPOLL
from states.states import UserState, create_state_machine
from vk_api.longpoll import VkEventType

users = {}  # База для хранения состояний пользователей


def handler_event(event):
    """
    Обработка сообщений от пользователей
    """
    user_id = event.user_id
    message = event.message.lower()

    if user_id not in users:
        users[user_id] = UserState(user_id)
        create_state_machine(users[user_id])

    user = users[user_id]

    if message == "назад":
        user.set_category(None)
        user.start()

    elif message == "вернуться к товарам":
        user.view_category()

    if user.state == "main_menu":
        processing_main_menu(user, user_id)

    elif user.state == "init":
        processing_init(user, user_id)

    elif user.state == "viewing_category":
        if message == "вернуться к товарам":
            message = user.get_category()
        processing_viewing_category(user, user_id, message)

    elif user.state == "viewing_product":
        processing_viewing_product(user, user_id, message.lower())


def main():
    """
    Главная функция для запуска бота
    """
    print('Бот запущен. Ожидание сообщений...')
    for event in LONGPOLL.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            handler_event(event)


if __name__ == '__main__':
    main()
