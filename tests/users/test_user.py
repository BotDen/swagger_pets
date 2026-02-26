from http import HTTPStatus

import allure
import pytest

from clients.errors.errors_schema import ValidationErrorSchema
from clients.users.users_client import UsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTags
from tools.assertions.base_assertion import assert_status_code
from tools.assertions.schema_assertion import validate_json_schema
from tools.assertions.users.users_assertion import (
    assert_created_user,
    assert_get_not_exist_user,
    assert_get_user_response,
)


@pytest.mark.users
@pytest.mark.regression
@allure.epic(AllureEpic.PETSTORE)
@allure.parent_suite(AllureEpic.PETSTORE)
@allure.feature(AllureFeature.USER)
@allure.suite(AllureFeature.USER)
class TestUser:
    @allure.title("Успешное создание нового пользователя")
    @allure.tag(AllureTags.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    def test_success_create_user(self, public_user_client: UsersClient):
        # тело запроса для создания пользователя
        request = CreateUserRequestSchema()
        # запрос на создание пользователя
        response = public_user_client.create_user_api(request=request)
        # преобразование json ответа в pydantic модель
        response_data = CreateUserResponseSchema.model_validate_json(response.text)
        # проверка 200 статус кода
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        # запрос на получения данных созданного пользователя
        get_response = public_user_client.get_user_by_username_api(user_name=request.user_name)
        # преобразование json ответа в pydantic модель
        get_response_modal = GetUserResponseSchema.model_validate_json(get_response.text)
        # проверка созданного пользователя с исходным
        assert_created_user(request=request, response=get_response_modal)
        # проверка ответа при создании пользователя на соответствие JSON схеме
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.title("Получение данных пользователя по username")
    @allure.tag(AllureTags.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    def test_get_user_by_username(
        self,
        public_user_client: UsersClient,
        function_user: UserFixture,
    ):
        # запрос на получение данных созданного пользователя
        response = public_user_client.get_user_by_username_api(user_name=function_user.user_name)
        # проверка 200 статус кода
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        # преобразование json ответа в pydantic модель
        response_schema = GetUserResponseSchema.model_validate_json(response.text)
        # проверка полученного пользователя с запросом на создание пользователя
        assert_get_user_response(get_user_response=response_schema, create_user_request=function_user.request)
        # проверка ответа при получении пользователя на соответствие JSON схеме
        validate_json_schema(instance=response.json(), schema=response_schema.model_json_schema())

    @allure.title("Удаление пользователя по username")
    @allure.tag(AllureTags.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    def test_delete_user_by_username(
        self,
        public_user_client: UsersClient,
        function_user: UserFixture,
    ):
        # удаление пользователя по username
        response = public_user_client.delete_user_by_username_api(user_name=function_user.user_name)
        # проверка 200 статуса ответа
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        # запрос удаленного пользователя по username
        get_response = public_user_client.get_user_by_username_api(user_name=function_user.user_name)
        # проверка 404 статус кода
        assert_status_code(actual=get_response.status_code, expected=HTTPStatus.NOT_FOUND)
        # получение модели ошибки
        get_response_schema = ValidationErrorSchema.model_validate_json(get_response.text)
        # проверка полученной ошибки с ожидаемой
        assert_get_not_exist_user(actual=get_response_schema)
        # проверка, что полученная ошибка соответствует JSON схеме
        validate_json_schema(instance=get_response.json(), schema=get_response_schema.model_json_schema())
