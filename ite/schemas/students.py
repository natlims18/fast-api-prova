def student_schema(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["name"],
        "ra": db_item["ra"],
        "email": db_item["email"],
        "course": db_item["course"],
    }


def student_list(db_item) -> list:
    students = []
    for item in db_item:
        students.append(
            student_schema(item)
        )
    return students