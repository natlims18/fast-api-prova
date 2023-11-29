from fastapi import APIRouter
from ite.config.database import mongo
from ite.models.reviews import Review
from ite.schemas.reviews import review_list

router = APIRouter()

@router.get("/list")
async def review_lists():
    """List all Reviews."""
    reviews = await mongo.reviews.find().to_list(None)
    return review_list(reviews)

@router.post("/create/")
async def review_detail(review: Review):
    """Review details."""
    mongo.reviews.insert_one(dict(review))
    return {"message": "Review incluída com sucesso"}


@router.put("/update/")
async def review_update(title: str, review: Review):
    """Updates a review."""
    review_to_update = dict(review)
    print(review_to_update)

    await mongo.reviews.find_one_and_update(
        {"title": title},
        {"$set": dict(review_to_update)}
    )
    return {"message": "Review alterada com sucesso"}


@router.delete("/delete/")
async def review_delete(title: str):
    """Deletes a review."""
    mongo.reviews.find_one_and_delete(
        {"title": title}
    )
    return {"message": "Review deletada"}