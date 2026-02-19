from http import HTTPStatus

import pytest

from clients.users.users_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.base_assertion import assert_status_code
from tools.assertions.schema_assertion import validate_json_schema
from tools.assertions.users.users_assertion import assert_created_user


@pytest.mark.regression
class TestUser:
    def test_success_create_user(self):
        user_client = get_public_user_client()
        # тело запроса для создания пользователя
        request = CreateUserRequestSchema()
        # запрос на создание пользователя
        response = user_client.create_user_api(request=request)
        # преобразование json ответа в pydantic модель
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # проверка статус кода
        assert_status_code(
            actual=response.status_code,
            expected=HTTPStatus.OK,
        )
        # запрос на получения данных созданного пользователя
        get_response = user_client.get_user_by_username_api(user_name=request.user_name)
        # преобразование json ответа в pydantic модель
        get_response_modal = GetUserResponseSchema.model_validate_json(get_response.text)
        # проверка созданного пользователя с исходным
        assert_created_user(request=request, response=get_response_modal)

        # проверка ответа при создании пользователя на соответствие json схеме
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
