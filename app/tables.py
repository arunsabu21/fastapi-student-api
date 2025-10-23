from db import engine, Base
from models import Student, Course, Enrollment

Base.metadata.create_all(bind=engine)