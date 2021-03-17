FROM python:3.9-slim-buster
RUN pip install -U pip && pip install poetry && poetry config virtualenvs.create false
WORKDIR /app
COPY ./poetry.lock    ./
COPY ./pyproject.toml ./
RUN poetry install --no-dev
COPY ./migrations ./migrations
COPY ./queries    ./queries
COPY ./todo_app   ./todo_app
ENV MYSQL_USER="todo_app"
ENV MYSQL_PASS="todo_app"
ENV MYSQL_HOST="todo_app-db"
EXPOSE 8000
VOLUME /app
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "todo_app:api"]
