from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator


@allure.step("Валидация JSON схемы")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, что instance (JSON-объект) соответствует заданной JSON-схеме
    :param instance: проверяемый JSON-объект
    :param schema: Схема которой должен соответствовать JSON-объект
    :raises jsonschema.exceptions.ValidationError: Если JSON-объект (instance) не соответствует схеме
    """
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
