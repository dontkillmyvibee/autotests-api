from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """Модель данных курса"""
    id: UUID
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

    model_config = ConfigDict(populate_by_name=True)


class GetCoursesQuerySchema(BaseModel):
    """Запрос на получение списка курсов"""
    user_id: UUID = Field(alias="userId")

    model_config = ConfigDict(populate_by_name=True)


class CreateCourseRequestSchema(BaseModel):
    """Запрос на создание курса"""
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: UUID = Field(alias="previewFileId")
    created_by_user_id: UUID = Field(alias="createdByUserId")

    model_config = ConfigDict(populate_by_name=True)


class CreateCourseResponseSchema(BaseModel):
    """Ответ при создании курса"""
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """Запрос на обновление курса"""
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")

    model_config = ConfigDict(populate_by_name=True)
