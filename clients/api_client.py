from httpx import Client, QueryParams, Response, URL


class ApiClient:
    """Базовый класс api клиента"""

    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Выполняет GET запрос
        :param url: URL адрес ручки
        :param params: Параметры запроса (?key=value)
        :return: Возвращает объект Response с данными ответа
        """
        return self.client.get(url=url, params=params)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
