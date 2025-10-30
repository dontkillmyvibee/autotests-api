from typing import TypedDict
import httpx
from clients.api_client import APIClient


class CreateUserRequest(TypedDict):
    """Типизированная структура запроса на создание пользователя"""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для публичных методов, не требующих авторизации
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequest) -> httpx.Response:
        """
        Создаёт нового пользователя через публичный API.

        Args:
            request (CreateUserRequest): Данные пользователя для создания.
                Должны содержать поля:
                - email (str)
                - password (str)
                - lastName (str)
                - firstName (str)
                - middleName (str)

        Returns:
            httpx.Response: Ответ сервера после выполнения запроса.
        """
        return self.post("/api/v1/users", json=request)
