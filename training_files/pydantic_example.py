from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    city: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias='isActive')


user_data = {
    "id": 1,
    "name": 'Alice',
    "email": 'example@mail.ru',
    "isActive": False
}
user = User(**user_data)
print(user.model_dump())
print(user.model_dump_json())
