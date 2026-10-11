from fastapi import APIRouter
from routes import (
    ai_query,
    create_student,
    delete_student,
    get_student,
    update_student,
)

# Master router to aggregate all individual API route modules
api_router = APIRouter()

api_router.include_router(create_student.router)
api_router.include_router(get_student.router)
api_router.include_router(update_student.router)
api_router.include_router(delete_student.router)
api_router.include_router(ai_query.router)