from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.usuario_repo import UsuarioRepo
from routes.main_routes import router as main_router

app = FastAPI()

UsuarioRepo.criar_tabela()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(main_router)