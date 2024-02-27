from .models import Todo
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel, Field
from typing import Optional

TodoGet = pydantic_model_creator(Todo, name='TodoGet')


class TodoPost(BaseModel):
    title: str = Field(min_length=3, max_length=100)


class TodoPut(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    done: Optional[bool] = Field(None)
