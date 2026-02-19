from pydantic import BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber


class BasePydanticModel(BaseModel):
    """Базовая модель для генерации моделей pydantic"""
    model_config = ConfigDict(populate_by_name=True)


class BasePhoneModel(PhoneNumber):
    """Базовая модель для поля phone в модели pydantic"""
    phone_format = "E164"
