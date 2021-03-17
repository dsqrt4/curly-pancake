from typing import Optional

from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    done: bool


class CreateTodoCommand(BaseModel):
    title: str


class UpdateTodoCommand(BaseModel):
    title: Optional[str]
    done: Optional[bool]
