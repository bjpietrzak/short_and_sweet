from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form


class InferenceRequest(BaseModel):
    reviews: List[str] = Form(...)


class ClassificationResponse(BaseModel):
    classification: Optional[List[int]]