from typing import Annotated

from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STask(STaskAdd):
    id: int


tasks = []


@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}


