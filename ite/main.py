from fastapi import FastAPI
from routes import main_router
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000" #App react
]


app = FastAPI(
    title="ITE Students API",
    version="0.1.1",
)


app.include_router(main_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)