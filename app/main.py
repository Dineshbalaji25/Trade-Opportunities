
from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(title="Trade Opportunities API")
app.include_router(api_router)
