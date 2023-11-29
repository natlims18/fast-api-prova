from fastapi import FastAPI
from routes import main_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic


app = FastAPI(
    title="ITE Review de salgados API",
    version="1.1.1",
)

app.include_router(main_router)

security = HTTPBasic()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)