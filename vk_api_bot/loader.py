"""Модуль создания VK сессии"""

from vk_api import VkApi
from vk_api.longpoll import VkLongPoll

from config_data.config import VK_GROUP_ID, VK_TOKEN


VK_SESSION = VkApi(token=VK_TOKEN)
LONGPOLL = VkLongPoll(VK_SESSION, group_id=VK_GROUP_ID)
VK = VK_SESSION.get_api()
