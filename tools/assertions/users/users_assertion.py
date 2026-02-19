from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.base_assertion import assert_equal


def assert_created_user(request: CreateUserRequestSchema, response: GetUserResponseSchema):
    """
    Проверка, что созданный пользователь соответствует исходному запросу
    :param request: Исходный запрос на создание пользователя
    :param response: Ответ на запрос пользователя после создания
    :raises AssertionError: Если хотя бы одно поле не совпало
    """
    assert_equal(actual=response.id, expected=request.id, name="id")
    assert_equal(actual=response.user_name, expected=request.user_name, name="user_name")
    assert_equal(actual=response.first_name, expected=request.first_name, name="first_name")
    assert_equal(actual=response.last_name, expected=request.last_name, name="last_name")
    assert_equal(actual=response.email, expected=request.email, name="email")
    assert_equal(actual=response.password, expected=request.password, name="password")
    assert_equal(actual=response.phone, expected=request.phone, name="phone")
    assert_equal(actual=response.user_status, expected=request.user_status, name="user_status")
