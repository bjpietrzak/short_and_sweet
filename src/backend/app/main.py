from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from endpoints import router


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