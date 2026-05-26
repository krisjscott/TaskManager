from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_done: bool = False

class TaskCreate(TaskBase):
    pass
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_done: Optional[bool] = None

class TaskOut(TaskBase):
    id : int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class config:
        from_attribute = True 
