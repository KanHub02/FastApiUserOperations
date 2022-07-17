from fastapi import FastAPI, Query, Path, Body
from database import engine
from tables import Base
from api import router

Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(router)

