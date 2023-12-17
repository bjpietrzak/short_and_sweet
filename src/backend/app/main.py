from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from setup import BACKEND
from routers import router


app = FastAPI(prefix='/backend')
app.include_router(router)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    run("main:app", host=BACKEND['host'], port=BACKEND['port']
        , log_level='info', reload=True)