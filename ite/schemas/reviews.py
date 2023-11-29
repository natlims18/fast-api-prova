def review_schema(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "title": db_item["title"],
        "description": db_item["description"],
        "author": db_item["author"],
        "product": db_item["product"],
    }


def review_list(db_item) -> list:
    reviews = []
    for item in db_item:
        reviews.append(
            review_schema(item)
        )
    return reviews