from httpx import AsyncClient
from fastapi import HTTPException
from typing import List, Tuple

from setup import ERRORS, ENDPOINTS, BACKEND
from schemas import ProcessedReview, AppData, ReviewsData
from cache_management import redis_client as rc
from scrape import validate_url, extract_app_id, scrape_app_data, \
                   scrape_app_reviews


async def fetch_inference_result(url: str, payload: dict) -> dict:
    async with AsyncClient() as client:
        response = await client.post(url, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=ERRORS['inferenceError'])
    return response.json()

def get_topic_reviews(topic_key: int,
                      representative_idx: int,
                      reviews: List[str],
                      thumbs_up_count: List[int], 
                      sentiment_classification: List[int],
                      review_classification: List[int]
                      ) -> List[ProcessedReview]:

    topic_reviews_idx = [i for i, v in enumerate(review_classification)
                           if int(v) == topic_key and i != representative_idx]
    representative_review = [{
        'review': reviews[representative_idx],
        'thumbs_up_count': thumbs_up_count[representative_idx],
        'sentiment': sentiment_classification[representative_idx]
    }]
    topic_reviews = [{
        'review': reviews[i],
        'thumbs_up_count': thumbs_up_count[i],
        'sentiment': sentiment_classification[i]
    } for i in topic_reviews_idx]

    return representative_review + topic_reviews

async def request_inference(endpoint: str) -> dict:
    reviews = rc.get_cache('reviews')
    response = await fetch_inference_result(ENDPOINTS[endpoint],
                                            {"reviews": reviews})
    return response

def check_count(count: int) -> None:
    if count > BACKEND['max_reviews']:
        raise HTTPException(status_code=400,
            detail=f"{ERRORS['invalidCount']}. " +
            "Maximum allowed: {BACKEND['max_reviews']}")

def validate_app_data(url: str) -> Tuple[str, AppData]:
    if not validate_url(url):
        raise HTTPException(status_code=400, detail=ERRORS['invalidUrl'])

    app_id = extract_app_id(url)
    app_data = scrape_app_data(app_id)
    if app_data is None or app_data.reviews < BACKEND['min_reviews']:
        raise HTTPException(status_code=400, detail=ERRORS['invalidUrl'])

    return app_id, app_data

def validate_app_reviews(app_id: str, stars: int, count: int) -> ReviewsData:
    app_reviews = scrape_app_reviews(app_id, stars, count)
    if app_reviews.length < BACKEND['min_reviews']:
        raise HTTPException(status_code=400,
                            detail=ERRORS['insufficientReviews'])
    return app_reviews