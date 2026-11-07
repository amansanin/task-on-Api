
from pydantic import BaseModel, Field
from typing import Literal


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    priority: Literal["low", "medium", "high"] = "medium"
    status: Literal["pending", "in_progress", "completed"] = "pending"


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    priority: Literal["low", "medium", "high"]
    status: Literal["pending", "in_progress", "completed"]


class TaskStatusUpdate(BaseModel):
    status: Literal["pending", "in_progress", "completed"]
