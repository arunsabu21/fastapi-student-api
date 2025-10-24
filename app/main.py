from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Student, Course, Enrollment 
from schemas import StudentCreate, StudentUpdate, StudentsBulk, CourseCreate, EnrollmentCreate
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# Serve static files (CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")

# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
        
# ---------- Students CRUD ----------
        
@app.post("/students/")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, age=student.age)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.post("/students/bulk/")
def create_multiple_students(students_data: StudentsBulk, db: Session = Depends(get_db)):
    new_students = []
    for s in students_data.students:
        student = Student(name=s.name, age=s.age)
        db.add(student)
        new_students.append(student)
    db.commit()
    for student in new_students:
        db.refresh(student)
    return new_students

@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()



@app.put("/students/{student_id}")
def update_student(student_id: int, student_data: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    if student_data.name is not None:
        student.name = student_data.name
    if student_data.age is not None:
        student.age = student_data.age
    db.commit()
    db.refresh(student)
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Deleted successfully"}

# ---------- Courses CRUD ----------

@app.post("/courses/")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(name=course.name)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@app.get("/courses/")
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

# ---------- Enrollment ----------

@app.put("/enrollments/")
def enroll_student(data: EnrollmentCreate, db: Session = Depends(get_db)):
    enrollment = Enrollment(student_id=data.student_id, course_id=data.course_id)
    db.add(enrollment)
    db.commit()
    return {"detail": f"Student {data.student_id} enrolled in course {data.course_id}"}

@app.get("/enrollments/")
def get_enrollments(db: Session = Depends(get_db)):
    results = db.query(Enrollment, Student, Course).join(Student, Enrollment.student_id == Student.id)\
                                                   .join(Course, Enrollment.course_id == Course.id).all()
    response = []
    for enrollment, student, course in results:
        response.append({
            "student": student.name,
            "course": course.name
        })
    return response