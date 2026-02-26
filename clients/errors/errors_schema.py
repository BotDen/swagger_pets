from clients.base_pydantic_modal import BasePydanticModel


class ValidationErrorSchema(BasePydanticModel):
    code: int
    type: str
    message: str
