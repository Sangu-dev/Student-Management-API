from sqlalchemy import Column, Integer, String, Date
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String, nullable=False)
    student_class = Column(String, nullable=False)
    student_section = Column(String, nullable=False)
    student_dob = Column(Date, nullable=False)

     # New contact and additional information
    email = Column(String(254), unique=True, nullable=True)
    phone = Column(String(20), nullable=True)
    course = Column(String(100), nullable=True)
    address = Column(String(250), nullable=True)
    enrollment_date = Column(Date, nullable=True)
