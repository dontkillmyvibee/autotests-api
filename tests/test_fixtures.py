import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("scope=autouse")

@pytest.fixture(scope="session")
def settings():
    print("SESSION")

@pytest.fixture(scope="class")
def user():
    print("scope=class")

@pytest.fixture
def users_client(settings):
    print("scope=function")

class TestUserFlow:
    def test_user_can_login(self, user, users_client, settings):
        ...

    def test_user_can_create_course(self, user, users_client, settings):
        ...

class TestAccountFlow:
    def test_user_account(self, user, users_client, settings):
        ...


@pytest.fixture
def user_data():
    print("Создаем пользователя до теста")
    yield {"username": "test_user", "email": "test@example.com"}
    print('Удаляем пользователя после теста')

def test_user_email(user_data: dict):
    print(user_data)
    assert user_data["email"] == "test@example.com"

def test_user_username(user_data: dict):
    print(user_data)
    assert user_data["username"] == "test_user"