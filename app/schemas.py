# i schemas lägger vi till pydantic
# detta är API-datamodeller
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TaskBase(BaseModel):
    title: str = Field(
        min_length=1, 
        max_length=255,
        description="Readable content of a Task model",
        examples=["Buy milk", "Do your homework", "Send in report"])
    description: str | None = None

class TaskCreate(TaskBase): # i POST
    pass

class TaskUpdate(BaseModel): # i PUT/PATCH
    """Partial update. Only the included fields will be changed."""
    title: str | None = Field(
        default=None, 
        min_length=1, 
        max_length=255,
        description="New title. Omit to leave unchanged.")
    description: str | None = None
    done: bool | None = None

class TaskRead(TaskBase): # i GET
    id: int
    done: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        frozen=True, # readonly, immutable, kan inte ändras efteråt
        extra="forbid", # denna förbjuder extra fält i body med felkod 422. Mer användbar i POST/PUT/PATCH
        str_strip_whitespace=True
        )

# task.id - funkar pga ConfigDict ovan
# task["id"] - funkar inte pga ConfigDict ovan