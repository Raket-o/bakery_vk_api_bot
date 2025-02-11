"""Модуль отправки сообщений VK_API"""

from loader import VK
from vk_api.utils import get_random_id


def sending_messages(user_id, message, keyboard=None, attachment=None):
    """
    Отправка сообщений пользователю VK_API. Принимает id_пользователя,
    текст сообщения, может принимать клавиатуру и вложения
    """
    if attachment is None:
        attachment = []
    VK.messages.send(
        user_id=user_id,
        message=message,
        random_id=get_random_id(),
        keyboard=keyboard,
        attachment=attachment,
    )
