from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def get_all_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: TaskCreate):
    db_task = Task(
        title = task.title,
        description = task.description,
        is_done = task.is_done
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    update_date = task.model_dump(exclude_unset = True)

    for field, value in update_date.items():
        setattr(db_task, field, value)

    db.commit()
    db.refresh(db.commit)
    return db_task

def delete_task(db:Session, task_id: int):
    db_task = get_task(db, task_id)
    if not db_task:
        print("Not found")
        return None
    db.delete(db_task)
    db.commit()
    return db_task
