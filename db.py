from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime
import uuid
import os

Base = declarative_base()
DB_PATH = "sqlite:///backup_tasks.db"
engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(String, primary_key=True)
    file_path = Column(String)
    backup_name = Column(String)
    status = Column(String)
    retries = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)

def create_task(file_path, backup_name):
    session = Session()
    task = Task(
        id=str(uuid.uuid4()),
        file_path=file_path,
        backup_name=backup_name,
        status="PENDING",
        retries=0,
    )
    session.add(task)
    session.commit()
    return task.id

def get_task_status(task_id):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if not task:
        return None
    return {
        "task_id": task.id,
        "file_path": task.file_path,
        "backup_name": task.backup_name,
        "status": task.status,
        "retries": task.retries,
        "created_at": task.created_at.strftime("%Y-%m-%d %H:%M:%S")
    }
def get_all_tasks():
    session = Session()
    tasks = session.query(Task).order_by(Task.created_at.desc()).all()
    return tasks

