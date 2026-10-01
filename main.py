from fastapi import FastAPI, Request
from .models import Base
from .database import engine
from .routers import admin, auth, todos, users
from fastapi.templating import Jinja2Templates

app = FastAPI()

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="FastAPITodos/templates")

@app.get("/")
def test(request: Request):
    return templates.TemplateResponse(request, "home.html", {"todos": todos})

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)
