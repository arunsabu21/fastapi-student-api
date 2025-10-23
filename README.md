# FastAPI Student Management API

A simple **FastAPI** project to manage students, courses, and enrollments using **PostgreSQL**.  

**Repository:** [https://github.com/arunsabu21/fastapi-student-api](https://github.com/arunsabu21/fastapi-student-api)

---

## Features

- CRUD for students and courses
- Enroll students in courses
- Retrieve enrollment details
- Bulk student creation
- Environment variables via `.env`

---

## Technologies 
- Python 3.11+ – main programming language
- FastAPI – web framework for API development
- SQLAlchemy – ORM for database interactions
- PostgreSQL – relational database
- Uvicorn – ASGI server to run FastAPI
- Pydantic – data validation and serialization

## Project Structure

```
FastAPI-New-Project/
├─ app/
│ ├─ db.py
│ ├─ main.py
│ ├─ models.py
│ ├─ schemas.py
│ └─ tables.py
├─ requirements.txt
├─ .gitignore
├─ .env.example
└─ README.md
```

---

## Installation

```bash
git clone https://github.com/arunsabu21/fastapi-student-api.git
cd fastapi-student-api

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# Edit .env with PostgreSQL credentials

python app/tables.py
uvicorn app.main:app --reload
