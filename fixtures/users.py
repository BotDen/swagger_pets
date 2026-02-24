import pytest
from pydantic import EmailStr

from clients.base_pydantic_modal import BasePydanticModel
from clients.users.users_client import get_public_user_client, UsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BasePydanticModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def user_name(self) -> str:
        return self.request.user_name

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def email(self) -> EmailStr:
        return self.request.email


@pytest.fixture
def public_user_client() -> UsersClient:
    return get_public_user_client()


@pytest.fixture
def function_user(public_user_client: UsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    return UserFixture(request=request, response=response)
