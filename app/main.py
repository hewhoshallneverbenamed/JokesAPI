from fastapi import FastAPI
from . import models
from .database import engine
from .routers import jokes, users, auth, categories, ratings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jokes.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(ratings.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}



