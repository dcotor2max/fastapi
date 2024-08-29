from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class student(BaseModel):
    id: int
    name: str
    grade: int

students = [
    student(id=1, name="ahmad", grade=5),
    student(id=2, name="ali", grade=3),
]

@app.get("/students/")
def red_students():
    return students

@app.post("/students/")
def creat_student(new_student:student):
    students.append(new_student)
    return new_student
@app.post("/students/{student_id}")
def update_student(student_id: int, update_student: student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = update_student
            return update_student
    return {"error" : "student not found"}
@app.delete("/students/{student_id}")
def delet_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"messege": "Student delete"}
    return {"error": "Student not found"}



