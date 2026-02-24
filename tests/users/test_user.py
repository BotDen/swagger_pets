from http import HTTPStatus

import pytest

from clients.users.users_client import UsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.base_assertion import assert_status_code
from tools.assertions.schema_assertion import validate_json_schema
from tools.assertions.users.users_assertion import assert_created_user, assert_get_user_response


@pytest.mark.regression
class TestUser:
    def test_success_create_user(self, public_user_client: UsersClient):
        # тело запроса для создания пользователя
        request = CreateUserRequestSchema()
        # запрос на создание пользователя
        response = public_user_client.create_user_api(request=request)
        # преобразование json ответа в pydantic модель
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # проверка статус кода
        assert_status_code(
            actual=response.status_code,
            expected=HTTPStatus.OK,
        )
        # запрос на получения данных созданного пользователя
        get_response = public_user_client.get_user_by_username_api(user_name=request.user_name)
        # преобразование json ответа в pydantic модель
        get_response_modal = GetUserResponseSchema.model_validate_json(get_response.text)
        # проверка созданного пользователя с исходным
        assert_created_user(
            request=request,
            response=get_response_modal
        )

        # проверка ответа при создании пользователя на соответствие json схеме
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_get_user_by_username(
        self,
        public_user_client: UsersClient,
        function_user: UserFixture
    ):
        response = public_user_client.get_user_by_username_api(user_name=function_user.user_name)

        assert_status_code(
            actual=response.status_code,
            expected=HTTPStatus.OK
        )
        response_schema = GetUserResponseSchema.model_validate_json(response.text)
        assert_get_user_response(get_user_response=response_schema, create_user_request=function_user.request)

        validate_json_schema(instance=response.json(), schema=response_schema.model_json_schema())
