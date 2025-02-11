"""Обработчик состояния viewing_product"""

import base64

from keyboards.create_keyboard import create_keyboard_v1
from loader import VK_SESSION
from utils.manager_api import ApiManager
from utils.send_message import sending_messages
from utils.upload_photo_VK_to_bytes import VkUploadCustom


api = ApiManager
upload = VkUploadCustom(VK_SESSION)


def processing_viewing_product(user_state, user_id: int, message: str) -> None:
    """
    Функция запускает при состоянии viewing_product.
    Делает запрос с сервера бекэнда об информации выбранного продукта,
    выводит ёё пользователю и меняет состояния пользователя на view_category.
    Если такого продукта нет, то возвращает пользователю
    текст "Такого товара у нас нет"
    """
    response = api.send_get(url="products/<str:product_name>", params={"product_name": message.lower()})
    if response.json().get("id"):
        name = response.json().get("name")
        description = response.json().get("description")
        image = response.json().get("image")
        image = base64.b64decode(image)
        upload_image = upload.photo_messages(bim=image)[0]
        attachment = [f"photo{upload_image.get('owner_id')}_{upload_image.get('id')}"]
        sending_messages(
            user_id,
            message=f"Наименование: {name.title()}\n"
                    f"Описание: {description.capitalize()}",
            keyboard=create_keyboard_v1(text="вернуться к товарам", additional_btn=True, inline=True),
            attachment=attachment,
        )
        user_state.view_category()

    else:
        sending_messages(
            user_id,
            message=f"Такого товара у нас нет"
        )
