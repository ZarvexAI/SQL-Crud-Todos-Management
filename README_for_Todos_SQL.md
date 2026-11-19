# Todo Manager API

A REST API for managing todos, built with **FastAPI**, **SQLAlchemy** and **PostgreSQL**. It supports full CRUD operations (create, read, update, delete) and validates all incoming data with Pydantic.

## Features

- Create, read, update and delete todos
- Data stored in a PostgreSQL database
- Request validation with Pydantic models
- Automatic type conversion for path parameters (e.g. `id` is parsed to `int`)
- Consistent JSON responses (`status`, `data`, `message`)
- Interactive API docs generated automatically by FastAPI
- Tested with Postman

## Tech Stack

| Tool | Purpose |
|------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework |
| [PostgreSQL](https://www.postgresql.org/) | Database |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM (talks to the database) |
| [Pydantic](https://docs.pydantic.dev/) | Data validation |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |
| [Postman](https://www.postman.com/) | API testing |

## Project Structure

```
todo-manager/
├── main.py                      # App entry point, includes the router
├── config/
│   └── db_connection.py         # Database engine, session and get_db()
├── models/
│   └── todos_model.py           # SQLAlchemy model (Todo table)
├── Validations/
│   └── todos_validation.py      # Pydantic model (TodoValidation)
├── routes/
│   └── todo_routes.py           # CRUD endpoints (TodoRoutes)
├── requirements.txt
└── README.md
```

> Adjust file names above if yours differ (for example, where `TodoRoutes` lives).

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

At minimum you need:

```
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
```

### 4. Set up PostgreSQL

Create a database for the project:

```sql
CREATE DATABASE todo_db;
```

Then set your connection string in `config/db_connection.py` (or an environment variable):

```
postgresql://<user>:<password>@localhost:5432/todo_db
```

> **Tip:** don't commit your real password. Keep it in a `.env` file and add `.env` to `.gitignore`.

### 5. Run the server

```bash
uvicorn main:app --reload
```

The API is now running at `http://127.0.0.1:8000`.

## API Documentation

FastAPI generates interactive docs automatically:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check (confirms the server is running) |
| `POST` | `/Create` | Create a new todo |
| `GET` | `/GetAll` | Get all todos |
| `GET` | `/GetById/{id}` | Get a single todo by ID |
| `PUT` | `/Update/{id}` | Update an existing todo |
| `DELETE` | `/Delete/{id}` | Delete a todo |

### Request body (POST and PUT)

```json
{
  "title": "Buy milk",
  "description": "2 liters, full cream",
  "status": "pending"
}
```

### Example: create a todo

`POST /Create`

```json
{
  "status": "Success",
  "data": {
    "id": 1,
    "title": "Buy milk",
    "description": "2 liters, full cream",
    "status": "pending"
  },
  "message": "Todo created successfully"
}
```

### Example: get a todo by ID

`GET /GetById/1`

```json
{
  "status": "Success",
  "data": {
    "id": 1,
    "title": "Buy milk",
    "description": "2 liters, full cream",
    "status": "pending"
  },
  "message": "Todo retrieved successfully"
}
```

### Example: todo not found

`GET /GetById/999`

```json
{
  "status": "Error",
  "data": [],
  "message": "Todo not found"
}
```

### Example: delete a todo

`DELETE /Delete/1`

```json
{
  "status": "Success",
  "data": [],
  "message": "Todo deleted successfully"
}
```

## Testing with Postman

1. Start the server with `uvicorn main:app --reload`.
2. Open Postman and create a new request.
3. Choose the method (`GET`, `POST`, `PUT`, `DELETE`) and enter the URL, e.g. `http://127.0.0.1:8000/GetAll`.
4. For `POST` and `PUT`, go to **Body → raw → JSON** and paste your JSON.
5. Click **Send**.

## How It Works

- **Routes** receive the request. Path parameters such as `id` are converted to `int` by FastAPI using the type hint.
- **Pydantic models** validate the request body. Invalid data returns a `422` error automatically.
- **SQLAlchemy** queries and updates the PostgreSQL database through a session provided by `Depends(get_db)`.
- **Responses** are returned as JSON in a consistent `status` / `data` / `message` format.

## What I Learned

- Building REST APIs with FastAPI
- Connecting to PostgreSQL with SQLAlchemy
- Validating data with Pydantic
- Using dependency injection (`Depends`)
- Debugging common ORM errors (`.first()` vs `.all()`)

## Future Improvements

- [ ] Proper HTTP status codes (`201`, `404`, `500`) using `HTTPException`
- [ ] Response models with Pydantic
- [ ] User authentication (JWT)
- [ ] Pagination and filtering
- [ ] Due dates and priorities for todos
- [ ] Database migrations with Alembic
- [ ] Unit tests with pytest
- [ ] Docker setup

## License

This project is open source and available under the [MIT License](LICENSE).
