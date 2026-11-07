
from app.database import create_table

create_table()

print("Database and tasks table created successfully!")


from fastapi import FastAPI
from app.database import create_table
from app.routes.tasks import router as task_router

app = FastAPI(
    title="Task Management API",
    description="A REST API to manage tasks using FastAPI and SQLite",
    version="1.0.0"
)


# Create database table when application starts
@app.on_event("startup")
def startup():
    create_table()


# Connect task routes
app.include_router(task_router)


@app.get("/")
def home():
    return {"message": "Welcome to Task Management API"}
