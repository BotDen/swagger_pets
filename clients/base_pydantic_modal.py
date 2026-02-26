from pydantic import BaseModel, ConfigDict


class BasePydanticModel(BaseModel):
    """Базовая модель для генерации моделей pydantic"""
    model_config = ConfigDict(populate_by_name=True)
