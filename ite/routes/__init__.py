from fastapi import APIRouter
from .student import router as student_router
from .review import router as review_router


main_router = APIRouter()
main_router.include_router(
    student_router,
    prefix="/student",
    tags=["student"],
)
main_router.include_router(
    review_router,
    prefix="/review",
    tags=["review"],
)
