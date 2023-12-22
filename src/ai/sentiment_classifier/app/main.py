from fastapi import FastAPI
import uvicorn

from load_dependencies import config
from endpoint import router


app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host=config['host'],
                port=config['port'])