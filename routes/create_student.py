
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.model import Student
from app.schemas import StudentCreate, StudentResponse

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("", response_model=StudentResponse,
             status_code=status.HTTP_201_CREATED)
@router.post("/", response_model=StudentResponse,
             status_code=status.HTTP_201_CREATED,
             include_in_schema=False)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    db_student = Student(**student.model_dump())
    db.add(db_student)

    try:
        db.commit()
        db.refresh(db_student)
        return db_student
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A student with this email already exists."
        ) from exc
