import allure

from clients.errors.errors_schema import ValidationErrorSchema
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.base_assertion import assert_equal
from tools.assertions.errors_assertion import assert_validation_error
from tools.logger import get_logger


logger = get_logger("USER_ASSERTION")


@allure.step("Проверяем созданного пользователя")
def assert_created_user(request: CreateUserRequestSchema, response: GetUserResponseSchema):
    """
    Проверка, что созданный пользователь соответствует исходному запросу
    :param request: Исходный запрос на создание пользователя
    :param response: Ответ на запрос пользователя после создания
    :raises AssertionError: Если хотя бы одно поле не совпало
    """
    logger.info("Проверяем созданного пользователя")
    assert_equal(actual=response.id, expected=request.id, name="id")
    assert_equal(actual=response.user_name, expected=request.user_name, name="user_name")
    assert_equal(actual=response.first_name, expected=request.first_name, name="first_name")
    assert_equal(actual=response.last_name, expected=request.last_name, name="last_name")
    assert_equal(actual=response.email, expected=request.email, name="email")
    assert_equal(actual=response.password, expected=request.password, name="password")
    assert_equal(actual=response.phone, expected=request.phone, name="phone")
    assert_equal(actual=response.user_status, expected=request.user_status, name="user_status")


@allure.step("Проверяем полученного пользователя")
def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_request: CreateUserRequestSchema):
    """
    Проверка, что полученный пользователь соответствует запросу на создание
    :param get_user_response: Полученный пользователь
    :param create_user_request: Данные на создание пользователя
    :return AssertionError: Если хотя бы одно поле не совпало
    """
    logger.info("Проверяем полученного пользователя")
    assert_equal(actual=get_user_response.id, expected=create_user_request.id, name="id")
    assert_equal(actual=get_user_response.user_name, expected=create_user_request.user_name, name="user_name")
    assert_equal(actual=get_user_response.first_name, expected=create_user_request.first_name, name="first_name")
    assert_equal(actual=get_user_response.last_name, expected=create_user_request.last_name, name="last_name")
    assert_equal(actual=get_user_response.email, expected=create_user_request.email, name="email")
    assert_equal(actual=get_user_response.password, expected=create_user_request.password, name="password")
    assert_equal(actual=get_user_response.phone, expected=create_user_request.phone, name="phone")
    assert_equal(actual=get_user_response.user_status, expected=create_user_request.user_status, name="user_status")

@allure.step("Проверяем запрос на несуществующего пользователя")
def assert_get_not_exist_user(actual: ValidationErrorSchema):
    """
    Проверка, что получена ожидаемая ошибка при запросе несуществующего пользователя
    :param actual: Полученная ошибка
    :return AssertionError: Если хотя бы одно поле не совпало
    """
    expected_error = ValidationErrorSchema(
        code=1,
        type="error",
        message="User not found",
    )
    logger.info("Проверяем запрос на несуществующего пользователя")
    assert_validation_error(actual=actual, expected=expected_error)
