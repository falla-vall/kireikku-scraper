from fastapi import APIRouter
from app.api.routes.scraper import router as scraper_router

router = APIRouter()

router.include_router(scraper_router, prefix="/scraper", tags=["scraper"])