
from fastapi import APIRouter, HTTPException
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskStatusUpdate
)
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# Create task
@router.post("/")
def create_task(task: TaskCreate):
    return task_service.create_task(task)


# Get all tasks with optional filters
@router.get("/")
def get_tasks(status: str = None, priority: str = None):
    return task_service.get_all_tasks(status, priority)


# Get task by ID
@router.get("/{task_id}")
def get_task(task_id: int):
    task = task_service.get_task_by_id(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# Update complete task
@router.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    existing_task = task_service.get_task_by_id(task_id)

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task_service.update_task(task_id, task)


# Update task status
@router.patch("/{task_id}/status")
def update_status(task_id: int, task: TaskStatusUpdate):
    existing_task = task_service.get_task_by_id(task_id)

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task_service.update_task_status(task_id, task.status)


# Delete task
@router.delete("/{task_id}")
def delete_task(task_id: int):
    deleted = task_service.delete_task(task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
