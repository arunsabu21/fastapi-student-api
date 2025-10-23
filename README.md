# FastAPI Student Management API

A simple **FastAPI** project to manage students, courses, and enrollments using **PostgreSQL**.  
This project demonstrates a RESTful API with full **CRUD operations** and **database relationships**.

---

## Features

- Manage students (CRUD)
- Manage courses (CRUD)
- Enroll students in courses
- Retrieve enrollments with student and course details
- Bulk student creation
- Environment variable configuration using `.env`
- Organized project structure for scalability

---

## Project Structure
```
FastAPI-New-Project/
├─ app/
│ ├─ db.py # Database connection and session setup
│ ├─ main.py # FastAPI application with routes
│ ├─ models.py # SQLAlchemy ORM models
│ ├─ schemas.py # Pydantic schemas
│ └─ tables.py # Creates tables in the database
├─ requirements.txt # Python dependencies
├─ .gitignore # Ignored files/folders (venv, .env)
├─ .env.example # Template for environment variables
└─ README.md # Project documentation
```
## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/arunsabu21/fastapi-student-api.git
cd fastapi-student-api





