from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    age: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

class StudentsBulk(BaseModel):
    students: List[StudentCreate]

class CourseBase(BaseModel):
    name: str

class CourseCreate(CourseBase):
    name: str

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
