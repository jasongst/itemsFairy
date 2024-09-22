from database.database import init

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router.AlertRouter import AlertRouter

app = FastAPI(
    title="Items Fairy",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Routers
app.include_router(AlertRouter)

init()