from typing import Any


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


def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, (
        f"Некорректное значение {name} "
        f"Ожидаемое значение {expected} "
        f"Фактической значение {actual}"
    )
