from fastapi import APIRouter, Request,Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates =Jinja2Templates(directory="templates")

@router.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request":request})

@router.get("/sobre")
async def get_sobre(request: Request):
    return templates.TemplateResponse("pages/sobre.html", {"request":request})

@router.get("/tema")
async def get_tema(request: Request):
    temas = ["default","cerulean","cyborg", "darkly", "cosmo", "flatly","journal", "litera", "lumen","lux", "materia", "minty", "morph", "pulse", "quartz", "sandstone", "simplex", "sketchy", "slate", "solar", "spacelab", "superhero", "united", "vapor", "yeti", "zephyr"]
    return templates.TemplateResponse("pages/tema.html", {"request":request, "temas": temas})

@router.post("/post_tema")
async def post_tema(tema: str = Form(...)):
    response = RedirectResponse("/tema", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key="tema",
        value=tema,
        max_age=3600*24*365*10,
        httponly=True,
        samesite="lax"
    )
    return response