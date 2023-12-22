from fastapi import FastAPI
from random import randint, choice
from lorem import sentence, paragraph
import numpy as np

from schemas import (InferenceRequest, BERTopicInferenceResponse,
                     DistilBertInferenceResponse)


app = FastAPI(prefix='/model')


def get_indexes(reviews: list, key: int) -> list:
    reviews = [i for i, x in enumerate(reviews) if x == key]
    return reviews

@app.post('/inference/bertopic', response_model=BERTopicInferenceResponse)
async def bertopic(request: InferenceRequest):
    topic_nb = randint(1, 11)
    topics = [sentence() for key in range(topic_nb)]
    document_classification = np.random.randint(-1, topic_nb, size=len(request.reviews)).tolist()
    representative_reviews = [choice(get_indexes(document_classification, i))
                              for i in range(topic_nb)]

    response = BERTopicInferenceResponse(
        topics=topics,
        classification=document_classification,
        representative_reviews=representative_reviews
        )
    return response

@app.post('/inference/distilbert', response_model=DistilBertInferenceResponse)
async def distilbert(request: InferenceRequest):
    response = DistilBertInferenceResponse(
        classification=np.random.randint(-1,2,
                                         size=len(request.reviews)).tolist())
    return response