from typing import Any

from httpx import Client, QueryParams, Response, URL
from httpx._types import RequestData, RequestFiles


class ApiClient:
    """Базовый класс api клиента"""

    def __init__(self, client: Client):
        self.client = client

    def get(
        self,
        url: URL | str,
        params: QueryParams | None = None,
    ) -> Response:
        """
        Выполняет GET запрос

        :param url: URL адрес ручки
        :param params: Параметры запроса (?key=value)
        :return: Возвращает объект Response с данными ответа
        """
        return self.client.get(url=url, params=params)

    def post(
        self,
        url: URL | str,
        params: QueryParams | None = None,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
    ) -> Response:
        """
        Выполняет POST запрос

        :param url: URL адрес ручки
        :param params: Параметры запроса (?key=value)
        :param json: Данные в формате JSON
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded)
        :param files: Файл для загрузки на сервер
        :return: Возвращает объект Response с данными ответа
        """
        return self.client.post(url=url, params=params, json=json, data=data, files=files)

    def put(
        self,
        url: URL | str,
        params: QueryParams | None = None,
        json: Any | None = None,
    ) -> Response:
        """
        Выполняет PUT запрос

        :param url: URL адрес ручки
        :param params: Параметры запроса (?key=value)
        :param json: Данные в формате JSON
        :return: Возвращает объект Response с данными ответа
        """
        return self.client.put(url=url, params=params, json=json)

    def delete(
        self,
        url: URL | str,
        params: QueryParams | None = None,
    ) -> Response:
        """
        Выполняет DELETE запрос

        :param url: URL адрес ручки
        :param params: Параметры запроса (?key=value)
        :return: Возвращает объект Response с данными ответа
        """
        return self.client.delete(url=url, params=params)
