from typing import List, Dict
from pydantic import BaseModel


class ModelInferenceRequest(BaseModel):
    reviews: List[str]


class BERTopicInferenceResponse(BaseModel):
    Topics: Dict[int, List[str]] | None
    DocumentClusters: List[int] | None
    RepresentativeDocuments: dict | None
