from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import lorem
import random

from . import number_of_reviews, clusters
from app.schemas import AppData, DistilBertResponse, \
                        BertopicInferenceResponse, ClusterReviews


app = FastAPI(prefix='/backend')

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/app_data/')
async def app_data(url: str, stars: int = None, count: int = 10,
                   inssuficien: bool = False,
                   invalid_url: bool = False) -> AppData:
    if invalid_url:
        raise HTTPException(status_code=404,
                            detail='Invalid URL. Make sure URL is ' +
                                   'from english version of the site.')

    if inssuficien:
        raise HTTPException(status_code=404, detail='App did not recive ' +
                                                    'sufficient number of reviews')

    response = AppData(
        title='Google Maps',
        icon='https://play-lh.googleusercontent.com/Kf8WTct65hFJxBUDm5E-EpYsiDoLQiGGbnuyP6HBNax43YShXti9THPon1YKB6zPYpA',
        reviews=2239)

    return response


@app.get('/request_inference/bertopic/')
async def request_inference_bertopic() -> BertopicInferenceResponse:
    response = BertopicInferenceResponse(
        topics={
            0:"phone_app_service_picture",
            1:"instagram_time_bad_habbit",
            2:"cant_open_camera_error",
            3:"instagram_time_bad_habbit",
            4:"cant_open_camera_error",
            5:"instagram_time_bad_habbit",
            6:"cant_open_camera_error",
            7:"instagram_time_bad_habbit",
            8:"cant_open_camera_error",
            9:"instagram_time_bad_habbit",
        },
        counts={
            0: 740,
            1: 350,
            2: 210,
            3: 200,
            4: 190,
            5: 180,
            6: 170,
            7: 160,
            8: 150,
            9: 140,
        })
    return response

@app.get('/request_inference/distilbert/')
async def request_inference_distilbert() -> DistilBertResponse:
    response = DistilBertResponse(
        positive=2402,
        neutral=10,
        negative=90)
    return response

@app.get('/more_data/')
async def more_data(cluster: int,
                    results_not: bool = False) -> ClusterReviews:
    if results_not:
        raise HTTPException(status_code=404, detail='Results are not ready.')
    if cluster not in number_of_reviews:
        raise HTTPException(status_code=404, detail='Cluster not found.')

    reviews = [{"review": lorem.paragraph(),
                "thumbs_up_count": random.randint(0, 100),
                "sentiment": random.choice([-1,0,1])}
                for _ in range(number_of_reviews[cluster])]
    return ClusterReviews(
        cluster=clusters[cluster],
        reviews=reviews
    )
