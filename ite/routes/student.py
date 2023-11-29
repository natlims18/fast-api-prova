from fastapi import APIRouter
from config.database import mongo
from models.student import Student
from schemas.students import student_list, student_schema


router = APIRouter()


@router.get("/list")
async def students_list():
    """List all students."""
    students = mongo.students.find()
    students = await students.to_list(None)
    return student_list(students)

@router.post("/create/")
async def student_detail(student: Student):
    """Student details."""
    mongo.students.insert_one(dict(student))
    return {"message": "Estudante incluído com sucesso"}


@router.put("/update/")
async def student_update(ra: str, student: Student):
    """Updates a student."""
    student_to_update = dict(student)

    if not student_to_update["email"]:
        del student_to_update["email"]

    if not student_to_update["course"]:
        del student_to_update["course"]

    mongo.students.find_one_and_update(
        {"ra": ra},
        {"$set": dict(student_to_update)}
    )
    return {"message": "Estudante alterado com sucesso"}


@router.delete("/delete/")
async def student_delete(ra: str):
    """Deletes a student."""
    mongo.students.find_one_and_delete(
        {"ra": ra}
    )
    return {"message": "Estuante deletado"}