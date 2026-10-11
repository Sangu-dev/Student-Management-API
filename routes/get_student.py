
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Student
from app.schemas import StudentResponse

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("", response_model=List[StudentResponse])
@router.get("/", response_model=List[StudentResponse], include_in_schema=False)
def get_all_students(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    search: str | None = Query(default=None, min_length=1),
    course: str | None = Query(default=None, min_length=1),
    student_class: str | None = Query(default=None, min_length=1),
    db: Session = Depends(get_db),
):
    query = db.query(Student)

    if search:
        query = query.filter(
            Student.student_name.ilike(f"%{search.strip()}%")
        )

    if course:
        query = query.filter(
            Student.course.ilike(f"%{course.strip()}%")
        )

    if student_class:
        query = query.filter(
            Student.student_class == student_class.strip()
        )

    return query.order_by(Student.id).offset(skip).limit(limit).all()


@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db),
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student
