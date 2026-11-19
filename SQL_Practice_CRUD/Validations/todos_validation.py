from pydantic import BaseModel

class TodoValidation(BaseModel):
    title: str
    description: str
    status: str