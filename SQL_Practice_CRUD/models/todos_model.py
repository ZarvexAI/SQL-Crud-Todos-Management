from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import datetime
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(String(200), nullable=True)
    status = Column(String(100), nullable=True)
    created_at = Column(String, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))