from typing import Union

from fastapi import APIRouter, HTTPException

from app.services.scraper import scrap_url

router = APIRouter()


@router.get("")
def retrieve_page_source(url: str, css_selector: Union[str, None] = None):
    page_source = scrap_url(url, css_selector)
    if page_source["is_success"] == False:
        raise HTTPException(status_code=422, detail=page_source["error"])

    return {"page_source": page_source["data"]}
