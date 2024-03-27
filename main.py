from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.gateway.router import gateway_api_router

gateway_api = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:7000",
    "http://localhost:6000",
    "http://localhost:5000",
]

gateway_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gateway_api.include_router(gateway_api_router)
