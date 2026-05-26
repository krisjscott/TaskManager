from fastapi import FastAPI
from app.routers import task
from app.database import engine, Base

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title = "TaskManager",
    description = "Task manager build with FastAPI",
    version = "1.0.0"
)

app.include_router(task.router)

@app.get("/")
def root():
    return {"message" : "API is running"}