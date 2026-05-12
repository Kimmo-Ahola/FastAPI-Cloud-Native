# fil för att skapa FastAPI
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tasks
# skapar databasen automatiskt baserat på våra klasser
# all som ärver från Base skapas
# vi ska ersätta med alembic nästa lektion
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My demo api",
    description="""
A simple tasks API built as a demo.

## Features
* CRUD on tasks
* Pagination support
* Automatic validation via pydantic

## numbered List
1. first
1. second
1. third

<h1>Header 1</h1>
""",
version="0.1.0",
contact={"name":"Kimmo Ahola", "email":"kimmo@ahola.email.com"},
license_info={"name":"MIT"}
    )
# lägg till våra routers till app-objektet
app.include_router(tasks.router)


@app.get("/")
def root():
    return {"status": "ok"}
