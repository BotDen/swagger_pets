from typing import Any

import allure


@allure.step("Проверка, что фактический {actual} код ответа соответствует ожидаемому {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус код соответствует ожидаемому

    :param actual: Фактический статус код
    :param expected: Ожидаемый статус код
    :raises AssertionError: Если статус коды не совпадут
    """
    assert actual == expected, (
        f"Некорректный статус код "
        f"Ожидаемый статус код {expected} "
        f"Фактический статус код {actual} "
    )


@allure.step("Проверка, что {name} равно {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Базовая проверка, что фактическое значение соответствует ожидаемому
    :param actual: Фактическое значение
    :param expected: Ожидаемое значение
    :param name: Имея элемента
    :return AssertionError: Если значения не совпали
    """
    assert actual == expected, (
        f"Некорректное значение {name} "
        f"Ожидаемое значение {expected} "
        f"Фактической значение {actual}"
    )
