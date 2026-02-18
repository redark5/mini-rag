from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import get_settings, settings

base_router = APIRouter(
prefix="/api/v1",
tags=["api_v1"]

)


@base_router.get("/")
# uvicorn main:app --reload --host 0.0.0.0 --port 8000

async def welcome(app_settings: settings = Depends(get_settings)):
    app_settings = get_settings()
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION

    return {
        "app_name": app_name,
        "app_version": app_version,
        }

