"""Модуль создания клавиатуры"""

import json

from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def create_keyboard_v1(
        buttons=None,
        one_time=False,
        color="primary",
        additional_btn=False,
        inline=False,
        text="Назад"
) -> VkKeyboard:
    """
    Создание клавиатуры с кнопками
    """
    if buttons is None:
        buttons = []

    if color == "primary":
        color = VkKeyboardColor.PRIMARY
    elif color == "secondary":
        color = VkKeyboardColor.SECONDARY
    elif color == "positive":
        color = VkKeyboardColor.POSITIVE
    elif color == "negative":
        color = VkKeyboardColor.NEGATIVE

    kb = VkKeyboard(one_time=one_time, inline=inline)
    for btn_name in buttons:
        kb.add_button(btn_name, color=color)

    if additional_btn:
        kb.add_button(text, color=color)

    return kb.get_keyboard()
