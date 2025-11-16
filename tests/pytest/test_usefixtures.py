import pytest


@pytest.fixture
def clear_books():
    print("DELETE")


@pytest.fixture
def fill_books():
    print("FILL")


@pytest.mark.usefixtures("fill_books", "clear_books")
class TestLibrary:
    def test_library_user(self):
        ...

    def test_library_user_login(self):
        ...
