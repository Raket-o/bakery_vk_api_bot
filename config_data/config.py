"""Модуль конфиг для проверки создано ли окружение."""
import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")
VK_GROUP_ID = os.getenv("VK_GROUP_ID")
TITLE_TEXT = os.getenv("TITLE_TEXT")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = "bakery_vk_api_bot"
DB_TESTS = True if os.getenv("DB_TESTS") == "True" else False
DB_FILLING = True if os.getenv("DB_FILLING") == "True" else False
URL_BACKEND_SERVER = os.getenv("URL_BACKEND_SERVER")
