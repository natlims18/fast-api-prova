from fastapi import FastAPI
from ite.routes.review import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic


app = FastAPI(
    title="ITE Review de salgados API",
    version="1.1.1",
)

security = HTTPBasic()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)