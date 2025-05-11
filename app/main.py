from fastapi import FastAPI

from app.routes import contacts, linebots
from app.dependencies import SettingsDep

# Create FastAPI app
app = FastAPI()


@app.get("/")
async def health(settings: SettingsDep):
    return {"health": "OK", "version": settings.version}


# Include routers
app.include_router(contacts.router)
app.include_router(linebots.router)
