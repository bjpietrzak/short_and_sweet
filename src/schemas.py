from typing import List
from pydantic import BaseModel


class AppScrapeRequest(BaseModel):
    URL: str
    Order: str | None
    Stars: int | None
    Count: int | None


class ModelInferenceRequest(BaseModel):
    Reviews: List[str]