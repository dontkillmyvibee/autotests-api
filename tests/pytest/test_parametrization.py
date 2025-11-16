import pytest
from _pytest.fixtures import SubRequest


def test_number_1():
    assert 1 > 0


def test_number_2():
    assert 2 > 0


def test_number_3():
    assert 3 > 0


def test_number_minus_1():
    assert -1 > 0


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["macos", "windows", "linux"])
@pytest.mark.parametrize("stand",
                         ["https://stable.company.com", "https://dev.company.com", "https://stage.company.com"])
def test_multiplication_of_numbers(os: str, stand: str):
    assert len(os + stand) > 0

@pytest.fixture(params=[
    "https://stable.company.com",
    "https://dev.company.com",
    "https://stage.company.com"
])
def host(request: SubRequest) -> str:
    return request.param


def test_host(host: str):
    print(f"Запускаем тест с хостом: {host}")

@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperation:
    def test_with_operations(self, user: str):
        print(f"with operations")

    def test_without_operations(self, user: str):
        print(f"without operations")

users = {
    "+7..." : "user with money",
    "+7909": "user without money",
    "+7888": "user with credit"
}

@pytest.mark.parametrize(
    "phone_number", users.keys(),
    ids=lambda phone_number: f" {phone_number}, {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    pass



















