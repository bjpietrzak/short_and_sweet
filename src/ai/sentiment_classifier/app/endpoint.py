from fastapi import APIRouter
import torch
import torch.nn.functional as F
from fastapi import HTTPException

from schemas import InferenceRequest, ClassificationResponse
from load_dependencies import model, tokenizer


router = APIRouter()

@router.post('/inference/sentiment')
async def sentiment(request: InferenceRequest) -> ClassificationResponse:
    try:
        inputs = tokenizer(request.reviews, return_tensors="pt", padding=True,
                        truncation=True, max_length=3000)
        with torch.no_grad():
            logits = model(**inputs).logits
        probabilities = F.softmax(logits, dim=1)
        sentiments = torch.argmax(probabilities, dim=-1)
        sentiments = sentiments * 2 - 1
        max_probabilities = torch.max(probabilities, dim=-1).values
        sentiments[(max_probabilities >= 0.4) & (max_probabilities <= 0.6)] = 0
        sentiments = sentiments.tolist()
        return ClassificationResponse(
            classification=sentiments)
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))