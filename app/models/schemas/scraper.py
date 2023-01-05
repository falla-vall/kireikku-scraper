from typing import Union
from pydantic import BaseModel

class ScraperUrl(BaseModel):
    is_success: bool
    data: Union[str, None]
    error: Union[str, None]