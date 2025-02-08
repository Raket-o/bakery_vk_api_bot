"""Модуль конфиг для проверки создано ли окружение."""
import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = "bakery_vk_api_bot"
DB_TESTS = True if os.getenv("DB_TESTS") == "True" else False
