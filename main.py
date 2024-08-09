from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.main_routes import router as main_router

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(main_router)