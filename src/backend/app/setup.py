import json
import redis
import logging


with open('configs/endpoints.json', 'r') as f:
    ENDPOINTS = json.load(f)

with open('configs/errors.json', 'r') as f:
    ERRORS = json.load(f)

with open('configs/redis.json', 'r') as f:
    REDIS = json.load(f)

with open('configs/backend.json', 'r') as f:
    BACKEND = json.load(f)

logging.basicConfig(filename='backend.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')