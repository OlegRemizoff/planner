from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import uvicorn


from .routers.users import router as user_router
from .routers.events import router as event_router
from .routers.pages import router as pages_router

from app.routers.pages import templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), "static")

@app.get("/", name="home")
async def get_home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})



app.include_router(user_router)
app.include_router(event_router)
app.include_router(pages_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0000", port=8000, reload=True)
