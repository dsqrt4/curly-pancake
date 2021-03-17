import os
from typing import Dict

import pugsql
from fastapi import FastAPI

from todo_app.model import UpdateTodoCommand, CreateTodoCommand, Todo


def get_db():
    connection_string = 'mysql+pymysql://{}:{}@{}/TodoDb'.format(
        os.getenv('MYSQL_USER', 'pug'),
        os.getenv('MYSQL_PASS', 'pug'),
        os.getenv('MYSQL_HOST', 'localhost:3306'),
    )

    queries = pugsql.module('queries/')
    queries.connect(connection_string)

    return queries


def add_get_todos_endpoint(api: FastAPI, db):
    @api.get("/todos")
    def read_items():
        return [Todo(**it) for it in db.find_all_todos()]


def main() -> FastAPI:
    db = get_db()
    api = FastAPI()

    @api.get("/todos/{task_id}")
    def read_item(task_id: int):
        return db.find_todo_by_id(id=task_id)

    @api.put("/todos/{task_id}")
    def update_item(task_id: int, update: UpdateTodoCommand):
        todo: Dict[str, any] = db.find_todo_by_id(id=task_id)
        if update.title is not None:
            todo['title'] = update.title
        if update.done is not None:
            todo['done'] = update.done

        db.update_todo(**todo)

    @api.post("/todos")
    def update_item(create: CreateTodoCommand):
        db.create_todo(title=create.title)

    add_get_todos_endpoint(api, db)

    return api
