from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import uvicorn


from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from .routers.users import router as user_router
from .routers.events import router as event_router
from .routers.pages import router as pages_router

from app.routers.pages import templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(user_router)
app.include_router(event_router)
app.include_router(pages_router)


@app.on_event("startup")
def startup():
    redis = aioredis.from_url("redis://localhost:6379")
    FastAPICache.init(RedisBackend(redis), prefix="cache")


@app.get("/", name="home")
async def get_home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0000", port=8000, reload=True)
