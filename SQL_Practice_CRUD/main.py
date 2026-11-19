from fastapi import FastAPI
from Routes.todos_CRUD_routes import TodoRoutes

app = FastAPI()
app.include_router(TodoRoutes, prefix="/function", tags=["Todo_routes"])