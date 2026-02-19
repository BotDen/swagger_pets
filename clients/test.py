from clients.users.users_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fake import fake

users_client = get_public_user_client()
data = CreateUserRequestSchema()
phon = fake.get_phone_number()
print(phon)
print(data.model_dump())
response = users_client.create_user_api(request=CreateUserRequestSchema())

print(response)