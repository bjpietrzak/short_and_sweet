from typing import List, Dict, Optional
from pydantic import BaseModel
from fastapi import Form


class InferenceRequest(BaseModel):
    reviews: List[str] = Form(...)


class BERTopicInferenceResponse(BaseModel):
    topics: Optional[List[str]]
    classification: Optional[List[int]]
    representative_reviews: Optional[List[int]]