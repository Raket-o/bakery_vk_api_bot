"""Модуль менеджера API."""

import requests
from requests import Response

from config_data.config import URL_BACKEND_SERVER as url_from_config


class ApiManager:
    """
    Класс для работы с запросами по API
    """
    URL_BACKEND_SERVER = url_from_config + "/api"

    @classmethod
    def send_get(
        cls,
        params: dict = None,
        data: dict = None,
        headers: dict = None,
        url: str = "api/",
    ) -> Response:
        """Метод класса отправляет GET запрос, может принимать параметры, данные,
        заголовки и дополнительный URL. Возвращает Response"""
        return requests.get(
                f"{cls.URL_BACKEND_SERVER}/{url}",
                data=data,
                params=params,
                headers=headers,
            )
