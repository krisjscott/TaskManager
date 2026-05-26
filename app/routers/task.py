from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut

import app.crud.task as crud

router = APIRouter(
    prefix = "/tasks",
    tags = ["tasks"])

@router.get("/", response_model = List[TaskOut])
def get_all_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    tasks = crud.get_all_tasks(db, skip=skip, limit=limit)
    return tasks

@router.get("/{task_id}", response_model=TaskOut)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = crud.get_task(db, task_id=task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task

@router.post("/", response_model = TaskOut, status_code = status.HTTP_201_CREATED)
def create_task(
    task : TaskCreate,
    db : Session = Depends(get_db)
):
    return crud.create_tasks(db, task=task)

@router.patch("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):
    updated = crud.update_task(db, task_id=task_id, task=task)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return updated


@router.delete("/{task_id}", response_model=TaskOut)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_task(db, task_id=task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return deleted