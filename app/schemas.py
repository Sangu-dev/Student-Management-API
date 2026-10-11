
from datetime import date
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentBase(BaseModel):
    student_name: str = Field(min_length=1, max_length=100)
    student_class: str = Field(min_length=1, max_length=50)
    student_section: str = Field(min_length=1, max_length=20)
    student_dob: date

    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=20)
    course: str | None = None
    address: str | None = None
    enrollment_date: date | None = None


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    student_name: str | None = Field(
        default=None, min_length=1, max_length=100
    )
    student_class: str | None = None
    student_section: str | None = None
    student_dob: date | None = None
    email: EmailStr | None = None
    phone: str | None = None
    course: str | None = None
    address: str | None = None
    enrollment_date: date | None = None


class StudentResponse(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
