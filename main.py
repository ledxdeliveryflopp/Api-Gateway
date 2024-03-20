from fastapi import FastAPI
from src.gateway.router import gateway_api_router

gateway_api = FastAPI()

gateway_api.include_router(gateway_api_router)
