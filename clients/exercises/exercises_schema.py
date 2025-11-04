from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict
from typing import List


class ExerciseSchema(BaseModel):
    id: UUID
    title: str
    course_id: UUID = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

    model_config = ConfigDict(populate_by_name=True)


class GetExercisesQuerySchema(BaseModel):
    course_id: str = Field(alias="courseId")
    model_config = ConfigDict(populate_by_name=True)

class CreateExerciseRequestSchema(BaseModel):
    title: str
    course_id: UUID = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")
    model_config = ConfigDict(populate_by_name=True)


class CreateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema
    model_config = ConfigDict(populate_by_name=True)


class UpdateExerciseRequestSchema(BaseModel):
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
    model_config = ConfigDict(populate_by_name=True)


class UpdateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema
    model_config = ConfigDict(populate_by_name=True)


class GetExercisesResponseSchema(BaseModel):
    exercises: List[ExerciseSchema]
    model_config = ConfigDict(populate_by_name=True)


class GetExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema
    model_config = ConfigDict(populate_by_name=True)
