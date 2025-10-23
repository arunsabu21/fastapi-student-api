# FastAPI Student Management API

A simple **FastAPI** project to manage students, courses, and enrollments using **PostgreSQL**.  
This project demonstrates how to create a RESTful API with full **CRUD operations** and **database relationships**.

---

## **Features**

- Manage students (CRUD)
- Manage courses (CRUD)
- Enroll students in courses
- Retrieve enrollments with student and course details
- Bulk student creation
- Clean project structure
- Environment variable configuration using `.env`

---

## **Project Structure**

FastAPI-New-Project/
├─ db.py                # Database connection and session setup
├─ models.py            # SQLAlchemy ORM models (Student, Course, Enrollment)
├─ schemas.py           # Pydantic schemas for request/response validation
├─ tables.py            # Creates tables in the database
├─ main.py              # FastAPI application with routes
├─ requirements.txt     # Python dependencies
├─ .gitignore           # Ignored files/folders (venv, .env)
├─ .env.example         # Template for environment variables
└─ README.md            # Project documentation