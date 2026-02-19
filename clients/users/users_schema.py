from pydantic import EmailStr, Field

from clients.base_pydantic_modal import BasePhoneModel, BasePydanticModel
from tools.fake import fake


class UserSchema(BasePydanticModel):
    """Модель объекта User"""

    id: int
    user_name: str = Field(alias="username")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: EmailStr
    password: str
    phone: str
    user_status: int = Field(alias="userStatus")


class CreateUserRequestSchema(BasePydanticModel):
    """Модель запроса для создания пользователя"""

    id: int = Field(default_factory=fake.get_id)
    user_name: str = Field(alias="username", default_factory=fake.get_user_name)
    first_name: str = Field(alias="firstName", default_factory=fake.get_first_name)
    last_name: str = Field(alias="lastName", default_factory=fake.get_last_name)
    email: EmailStr = Field(default_factory=fake.get_email)
    password: str = Field(default_factory=fake.get_password)
    phone: str = Field(default_factory=fake.get_phone_number)
    user_status: int = Field(alias="userStatus", default_factory=fake.get_random_int)


class UpdateUserRequestSchema(BasePydanticModel):
    """Модель запроса на обновление пользователя"""

    id: int = Field(default_factory=fake.get_id)
    user_name: str = Field(alias="username", default_factory=fake.get_user_name)
    first_name: str = Field(alias="firstName", default_factory=fake.get_first_name)
    last_name: str = Field(alias="lastName", default_factory=fake.get_last_name)
    email: EmailStr = Field(default_factory=fake.get_email)
    password: str = Field(default_factory=fake.get_password)
    phone: str = Field(default_factory=fake.get_phone_number)
    user_status: int = Field(alias="userStatus", default_factory=fake.get_random_int)


class CreateUserResponseSchema(BasePydanticModel):
    """Модель ответа после создания пользователя"""
    code: int
    type: str
    message: str


class GetUserResponseSchema(BasePydanticModel):
    """Модель ответа на запрос данных по пользователю"""

    id: int
    user_name: str = Field(alias="username")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: EmailStr
    password: str
    phone: str
    user_status: int = Field(alias="userStatus")
