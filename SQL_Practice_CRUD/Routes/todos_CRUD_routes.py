from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from Validations.todos_validation import TodoValidation
from models.todos_model import Todo
from config.db_connection import get_db

TodoRoutes = APIRouter()

@TodoRoutes.get("/")
def test():
    return {"message": "server is running"}


@TodoRoutes.post("/Create")
def create_todo(todo_data:TodoValidation, db:Session = Depends(get_db)):
    try:
        todoCreate = Todo(
            title=todo_data.title,
            description=todo_data.description,
            status=todo_data.status
        )
        db.add(todoCreate)
        db.commit()
        db.refresh(todoCreate)


        return{
            "status":"Success",
            "data":todoCreate,
            "message":"Todo created successfuly"
        }
    
    except Exception as e:
        return{
            "status":"Error",
            "data":[],
            "message":str(e)
        }




@TodoRoutes.get("/GetAll")
def get_all_todos(db:Session = Depends(get_db)):
    try:
        todosall = db.query(Todo).all()
        return{
            "status":"Success",
            "data":todosall,
            "message":"Todos retrieved successfully"
        }
    
    except Exception as e:
        return{
            "status":"Error",
            "data":[],
            "message":str(e)
        }   


@TodoRoutes.get("/GetById/{id}")
def get_todo_by_id(id:int, db:Session = Depends(get_db)):
    try:
        todosbyid = db.query(Todo).where(Todo.id == id).all()
        if not todosbyid:
            return{
                "status":"Error",
                "data":[],
                "message":"Todo not found"
            }
        return{
                "status":"Success",
                "data":todosbyid,
                "message":"Todo retrieved successfully"
                }
    
    except Exception as e:
        return{
                "status":"Error",
                "data":[],
                "message":str(e)
            }   


@TodoRoutes.put("/Update/{id}")
def update_todo(id:int,updated_data:TodoValidation, db: Session = Depends(get_db)):
    try:
        upd_todo=db.query(Todo).filter(Todo.id == id).first()
        if not upd_todo:
            return {"Message":"Todo not found"}
        
        upd_todo.title = updated_data.title
        upd_todo.description = updated_data.description
        upd_todo.status = updated_data.status
        
        db.commit()
        
        return{
            "status":"Success",
            "message":"Todo updated successfully"
            }

    except Exception as e:
         return{
                "status":"Error",
                "data":[],
                "message":str(e)
                }   


@TodoRoutes.delete("/Delete/{id}")
def delete_todo (id:int, db:Session = Depends(get_db)):
    try:
        req_todo= db.query(Todo).filter(Todo.id==id).first()
        
        if not req_todo:
            return {"Todo not found"}
        
        db.delete(req_todo)
        db.commit()
        
        return{
            "status":"Success",
            "data":[],
            "message":"Todo deleted succssfuly"
        }

    except Exception as e:
        return{
            "Status":"error",
            "data":[],
            "message":str(e)
        }