from fastapi import FastAPI
from routes import router as moderation_router

app = FastAPI(title="PixelPolice")

app.include_router(moderation_router, prefix="/api")
