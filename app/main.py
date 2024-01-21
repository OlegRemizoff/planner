from fastapi import FastAPI
import uvicorn

from .routers.users import router as user_router
from .routers.events import router as event_router
from .routers.pages import router as pages_router


app = FastAPI()
app.include_router(user_router)
app.include_router(event_router)
app.include_router(pages_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0000", port=8000, reload=True)
