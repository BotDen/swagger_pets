import allure

from clients.errors.errors_schema import ValidationErrorSchema
from tools.assertions.base_assertion import assert_equal


@allure.step("Проверяем фактически полученную ошибку с ожидаемой")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что полученная фактическая ошибка соответствует ожидаемой ошибке
    :param actual: Фактическая ошибка
    :param expected: Ожидаемая ошибка
    :return AssertionError: Если хотя бы одно поле не совпало
    """
    assert_equal(actual=actual.code, expected=expected.code, name="code")
    assert_equal(actual=actual.type, expected=expected.type, name="type")
    assert_equal(actual=actual.message, expected=expected.message, name="message")
