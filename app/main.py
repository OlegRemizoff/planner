from fastapi import FastAPI
import uvicorn

from .routes.users import router as user_router
from .routes.events import router as event_router

from .database.conections import connect


app = FastAPI()
app.include_router(user_router)
app.include_router(event_router)

@app.on_event("startup")
def on_startup():
    connect()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0000", port=8000, reload=True)
