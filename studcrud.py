import os
from dotenv import load_dotenv
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI , Depends, HTTPException

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def check_database_connection():
    try:
        # Attempt to connect to the database
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False
    return True

check_database_connection()

app = FastAPI(title="neon db test" , description="API to test connection with Neon PostgreSQL database",
              version="1.0.0")

@app.get("/")
def home():
    return {"message": "Welcome to the Neon PostgreSQL database test API"}


@app.get("/students")
def get_students_data():
    try:
        with SessionLocal() as session:
            result = session.execute(text("SELECT * FROM students"))
            students = result.mappings().all()
        return students
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching students data: {e}")

@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    try:
        with SessionLocal() as session:
            result = session.execute(text("SELECT * FROM students WHERE id = :id"), {"id": student_id})
            student = result.mappings().first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching student data: {e}")
    
    
from pydantic import BaseModel ,Field , EmailStr, HttpUrl, field_validator   
class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr = Field(...)
    age: int = Field(ge=0, le=100)
    course: str = Field(min_length=2, max_length=50)

@app.post("/student")
def create_student(student: StudentCreate):
    try:
        with SessionLocal() as session:
            session.execute(
                text("INSERT INTO students (name, email,age, course) VALUES (:name, :email, :age, :course)"),
                {"name": student.name, "email": student.email, "age": student.age, "course": student.course}
            )
            session.commit()
        return {"message": "Student created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating student: {e}")
    
class StudentUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=50)
    email: EmailStr | None = Field(default=None)
    age: int | None = Field(default=None, ge=0, le=100)
    course: str | None = Field(default=None, min_length=2, max_length=50)

@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    try:
        with SessionLocal() as session:
            session.execute(
                text("UPDATE students SET name = :name, email = :email, age = :age, course = :course WHERE id = :id"),
                {"name": student.name, "email": student.email, "age": student.age, "course": student.course, "id": student_id}
            )
            session.commit()
        return {"message": "Student updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating student: {e}")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    try:
        with SessionLocal() as session:
            session.execute(
                text("DELETE FROM students WHERE id = :id"),
                {"id": student_id}
            )
            session.commit()
        return {"message": "Student deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting student: {e}")