from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.root import rootRoute

app = FastAPI(
    title='GESIVE API REST SERVICE',
    description= 'API REST Services for GESIVE clients',
    openapi_tags=[{}]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(rootRoute)