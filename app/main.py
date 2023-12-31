from fastapi import FastAPI
import uvicorn

from .routes.users import router as user_router


app = FastAPI()
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0000", port=8000, reload=True)
