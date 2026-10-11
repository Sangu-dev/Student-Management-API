from fastapi import FastAPI
import uvicorn
from app import model  # Ensures models are registered with Base metadata
from app.database import Base, engine
from routes.base import api_router

# Automatically create database tables on startup if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="RESTful API for managing student records using FastAPI and SQLAlchemy",
    version="1.0.0",
)

# Include the aggregated router
app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Student Management API. Visit /docs for Swagger UI.",
        "docs": "/docs",
        "redoc": "/redoc",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)