"""Обработчик состояния init"""

from pathlib import Path

from vk_api import VkUpload

from config_data.config import TITLE_TEXT
from loader import VK_SESSION
from utils.send_message import sending_messages


BASE_DIR = Path(__file__).resolve().parent.parent.parent

upload = VkUpload(VK_SESSION)


def processing_init(user_state, user_id: int) -> None:
    """
    Функция запускает при состоянии init. Выводит картинку, текст приветствия в чат группы
    и меняет состояния пользователя на start
    """
    upload_image = upload.photo_messages(photos=str(BASE_DIR) + "/images/showcase.jpg")[0]
    attachment = [f"photo{upload_image.get('owner_id')}_{upload_image.get('id')}"]
    sending_messages(
        user_id,
        message=TITLE_TEXT + '\nНапиши "начать" для просмотра нашей витрины',
        attachment=attachment,
    )
    user_state.start()
