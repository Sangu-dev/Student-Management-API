
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.model import Student
from app.schemas import StudentResponse, StudentUpdate

router = APIRouter(prefix="/students", tags=["Students"])


@router.put("/{student_id}", response_model=StudentResponse)
@router.patch("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):
    db_student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not db_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    update_data = student_data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Provide at least one field to update."
        )

    for key, value in update_data.items():
        setattr(db_student, key, value)

    try:
        db.commit()
        db.refresh(db_student)
        return db_student
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The email may already belong to another student."
        ) from exc
