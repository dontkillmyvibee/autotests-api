from faker import Faker

fake = Faker('ru_RU')
print(fake.email())
print(fake.name())
print(fake.address())

data = {
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "email": fake.email(),
    "address": fake.address(),
    "age": fake.random_int(min=18, max=100)
}
print(data)
