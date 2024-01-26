from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.models.events import Event
from app.routers.events import retrive_all_events, retrive_event



router = APIRouter(
    prefix="/pages",
    tags=["Front-end"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/all-events", name='events')
async def get_all_events(request: Request, events: Event = Depends(retrive_all_events)):
    return templates.TemplateResponse("events.html", context={"request": request, "events": events})


@router.get("/event-detail/{id}", name='detail')
async def get_all_events(request: Request, event: Event = Depends(retrive_event)):
    return templates.TemplateResponse("detail.html", context={"request": request, "event": event})