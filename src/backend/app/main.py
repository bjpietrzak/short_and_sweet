from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from httpx import AsyncClient
import time

from app import config
from app.reviews import AppData, ReviewsData, Reviews
from app.scrape import (validate_url, extract_app_id,
                        scrape_app_data, scrape_app_reviews)




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
async def app_data(url: str, stars: int = None, count: int = 10) -> AppData:
    print('got here?')
    print(url)
    if not validate_url(url):
        raise HTTPException(status_code=404, detail='Invalid URL')

    app_id = extract_app_id(url)
    if app_id is None:
        raise HTTPException(status_code=404, detail='Invalid URL')

    app_data = scrape_app_data(app_id)
    if app_data is None:
        raise HTTPException(status_code=404, detail='App not found')
    if app_data.reviews < config['scraping']['min_reviews']:
        raise HTTPException(status_code=404, detail='Not enough reviews'
                            f'({app_data.reviews} < {config["scraping"]["min_reviews"]})')
    return app_data


@app.get('/get_reviews/')
async def get_reviews(app_id: str, stars: int = None,
                      count: int = 10) -> ReviewsData:
        print('results here')
        results = scrape_app_reviews(app_id, stars, count)
        if results.small_nb_of_reviews is not None and \
           results.small_nb_of_reviews < config['scraping']['min_reviews']:
            raise HTTPException(status_code=404, detail='Not enough reviews'
                                f'({results.small_nb_of_reviews} < {count})')
        return results

@app.get('/request_inference/bertopic/')
async def request_inference_bertopic() -> str:
    async with AsyncClient() as client:
        response = await client.get(f'{config["inference"]["bertopic_url"]}/bertopic/',
                                    params={"reviews": request.reviews})
        return response.json()

async def inference_transformers() -> str:
    async with AsyncClient() as client:
        response = await client.get(f'{config["inference"]["transformers_url"]}/transformers/',
                                    params={"reviews": request.reviews})
        return response.json()

@app.get('/healthckeck/')
async def healthcheck() -> str:
    return 'OK'