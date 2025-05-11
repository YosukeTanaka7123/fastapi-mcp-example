from fastapi import FastAPI

from app.routes import linebot, openweather, contacts
from app.dependencies import SettingsDep

# Create FastAPI app
app = FastAPI()


@app.get("/")
async def health(settings: SettingsDep):
    return {"health": "OK", "version": settings.version}


# Include routers
app.include_router(contacts.router)
app.include_router(linebot.router)
app.include_router(openweather.router)
