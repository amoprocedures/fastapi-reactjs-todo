from fastapi import FastAPI
from api.routing import router as todo_router
from tortoise.contrib.fastapi import register_tortoise
from settings.configuration import Config

app = FastAPI()
app.include_router(todo_router)
register_tortoise(
    app=app,
    db_url=Config.DB_CONNECTION,
    modules={'models': Config.DB_MODELS},
    add_exception_handlers=True,
    generate_schemas=False
)


@app.get('/')
def home():
    return "Welcome to todos api"
