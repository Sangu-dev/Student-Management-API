# Student Management API (FastAPI)

A RESTful API built with FastAPI, SQLAlchemy, and SQLite to manage student records. The project supports CRUD operations, input validation, automated testing, and an optional local AI-powered student query endpoint using Ollama.

## Features

- Create, retrieve, update, and delete student records.
- Support for both full updates (`PUT`) and partial updates (`PATCH`).
- Input validation using Pydantic.
- SQLite database integration with SQLAlchemy.
- Interactive API documentation using Swagger UI and ReDoc.
- Automated tests using pytest.
- AI-powered student queries using a locally running Ollama model.

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **AI:** LangChain Ollama integration
- **Testing:** pytest, FastAPI TestClient

## Project Structure

```text
FastAPI/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── model.py
│   └── schemas.py
├── routes/
│   ├── __init__.py
│   ├── ai_query.py
│   ├── base.py
│   ├── create_student.py
│   ├── delete_student.py
│   ├── get_student.py
│   └── update_student.py
├── .gitignore
├── main.py
├── requirements.txt
└── test_api.py
```

Local files such as `.env`, SQLite databases, virtual environments, and backups are excluded from Git using `.gitignore`.

## Prerequisites

- Python 3.11 or a compatible Python version.
- Git (optional, for cloning or version control).
- Ollama and the `gemma3:1b` model for the AI query feature.

## Setup and Installation

### 1. Clone the repository

After uploading this project to GitHub, use:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd FastAPI
```

Alternatively, open your existing project folder in VS Code.

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with:

```text
DATABASE_URL=sqlite:///./students.db
```

Keep `.env` private and do not commit it to GitHub.

The application should create the configured database tables on startup. If the database file already exists, it may contain existing records.

### 5. Run the application

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

- **Base URL:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| POST | `/students` | Create a student |
| GET | `/students` | Retrieve student records |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update a student record |
| PATCH | `/students/{student_id}` | Partially update a student record |
| DELETE | `/students/{student_id}` | Delete a student |
| POST | `/ai/query-students` | Ask questions about student records |

Refer to Swagger UI for request schemas, parameters, and response details.

## Running Tests

Run the automated test suite from the project root:

```bash
python -m pytest -v
```

The current test suite contains seven tests covering CRUD operations, validation, error handling, and the AI query endpoint.

## AI Query Feature

The AI endpoint uses a local Ollama model to answer questions about student records. The model must be installed and Ollama must be running for AI-generated answers.

Some count and course queries are handled directly by SQL to improve accuracy. Other questions use the configured local language model.

## Security Notes

- Do not upload `.env` files, credentials, or private student data.
- Local database files are excluded from version control.
- Use appropriate authentication and authorization before deploying the API for real users.
- This project is intended for learning and demonstration unless additional production security measures are implemented.


