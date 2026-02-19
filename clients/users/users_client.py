from httpx import Response

from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UpdateUserRequestSchema
from tools.routes import APIRoutes


class UsersClient(ApiClient):
    """Клиент для работы с ручкой /user"""

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод создания нового пользователя
        :param request: Словарь с id, user_name, first_name, last_name, email, password, phone, user_status
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.post(url=APIRoutes.USER, json=request.model_dump(by_alias=True))

    def get_user_by_username_api(self, user_name: str) -> Response:
        """
        Метод получения данных пользователя по username
        :param user_name: Логин пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"{APIRoutes.USER}/{user_name}")

    def update_user_by_username_api(self, user_name: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновляет существующего пользователя
        :param user_name: Логин существующего пользователя
        :param request: Словарь с полями id, user_name, first_name, last_name, email, password, phone, user_status
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.put(url=f"{APIRoutes.USER}/{user_name}", json=request.model_dump(by_alias=True))

    def delete_user_by_username_api(self, user_name: str) -> Response:
        """
        Метод удаления существующего пользователя
        :param user_name: Логин существующего пользователя
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"{APIRoutes.USER}/{user_name}")

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request=request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_user_client() -> UsersClient:
    """Функция по созданию экземпляра UsersClient с уже настроенным HTTP-клиентом"""
    return UsersClient(client=get_public_http_client())
