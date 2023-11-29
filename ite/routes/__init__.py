from fastapi import APIRouter
from .review import router as review_router


main_router = APIRouter()

main_router.include_router(
    review_router,
    prefix="/review",
    tags=["review"],
)
