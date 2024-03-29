from typing import List, Optional, Dict
from pydantic import BaseModel


class ProcessedReview(BaseModel):
    review: str
    thumbs_up_count: int
    sentiment: int


class DetailedResponse(BaseModel):
    cluster: str
    reviews: List[ProcessedReview]


class ReviewsData(BaseModel):
    reviews: List[str] = None
    thumbs_up_count: List[int] = None
    small_nb_of_reviews: Optional[int] = None
    length: int


class AppData(BaseModel):
    title: str
    icon: Optional[str]


class BertopicResponse(BaseModel):
    topics: Dict[int, str]
    counts: Dict[int, int]


class DistillbertResponse(BaseModel):
    positive: int
    neutral: int
    negative: int