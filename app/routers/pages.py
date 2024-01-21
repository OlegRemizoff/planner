from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.models.events import Event
from app.routers.events import retrive_all_events



router = APIRouter(
    prefix="/pages",
    tags=["Front-end"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/index.html")
async def get_home_page(request: Request, events: Event = Depends(retrive_all_events)):
    ...
    return templates.TemplateResponse("index.html", context={"request": request, "events": events})