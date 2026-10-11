
from uuid import uuid4

from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def make_student_payload(email=None):
    """Create test data with a unique email address."""
    return {
        "student_name": "Test Student",
        "student_class": "10",
        "student_section": "A",
        "student_dob": "2008-05-15",
        "email": email or f"test-{uuid4().hex[:12]}@example.com",
        "phone": "9876543210",
        "course": "Computer Science",
        "address": "Bengaluru",
        "enrollment_date": "2025-08-01",
    }


def test_crud_flow():
    response = client.get("/")
    assert response.status_code == 200
    assert "Student Management API" in response.json()["message"]

    payload = make_student_payload()
    response = client.post("/students", json=payload)
    assert response.status_code == 201, response.text

    student_id = response.json()["id"]
    assert response.json()["student_name"] == "Test Student"

    try:
        response = client.get("/students")
        assert response.status_code == 200
        assert any(s["id"] == student_id for s in response.json())

        response = client.get(f"/students/{student_id}")
        assert response.status_code == 200

        updated_payload = {
            **payload,
            "student_name": "Updated Test Student",
            "student_class": "11",
            "student_section": "B",
        }
        response = client.put(
            f"/students/{student_id}", json=updated_payload
        )
        assert response.status_code == 200, response.text
        assert response.json()["student_name"] == "Updated Test Student"

        response = client.patch(
            f"/students/{student_id}",
            json={"student_section": "A+"},
        )
        assert response.status_code == 200, response.text
        assert response.json()["student_section"] == "A+"

    finally:
        # Remove the test record even if an assertion fails.
        client.delete(f"/students/{student_id}")

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 404


def test_duplicate_email_returns_409():
    payload = make_student_payload()
    response = client.post("/students", json=payload)
    assert response.status_code == 201, response.text

    student_id = response.json()["id"]

    try:
        response = client.post("/students", json=payload)
        assert response.status_code == 409, response.text
    finally:
        client.delete(f"/students/{student_id}")


def test_invalid_email_returns_422():
    payload = make_student_payload(email="wrong-email")
    response = client.post("/students", json=payload)
    assert response.status_code == 422, response.text



def test_empty_patch_returns_422():
    payload = make_student_payload()
    create_response = client.post("/students", json=payload)
    assert create_response.status_code == 201, create_response.text

    student_id = create_response.json()["id"]

    try:
        response = client.patch(f"/students/{student_id}", json={})
        assert response.status_code == 422, response.text
    finally:
        client.delete(f"/students/{student_id}")



def test_missing_student_returns_404():
    missing_id = 999999

    response = client.get(f"/students/{missing_id}")
    assert response.status_code == 404

    response = client.patch(
        f"/students/{missing_id}", json={"phone": "9123456780"}
    )
    assert response.status_code == 404

    response = client.put(
        f"/students/{missing_id}",
        json=make_student_payload(),
    )
    assert response.status_code == 404

    response = client.delete(f"/students/{missing_id}")
    assert response.status_code == 404



def test_ai_query_returns_answer():
    response = client.post(
        "/ai/query-students",
        json={"question": "How many students are in the database?"},
    )

    assert response.status_code == 200, response.text

    data = response.json()
    assert data["question"] == "How many students are in the database?"
    assert isinstance(data["answer"], str)
    assert len(data["answer"].strip()) > 0


def test_ai_query_rejects_empty_question():
    response = client.post(
        "/ai/query-students",
        json={"question": ""},
    )

    assert response.status_code == 422, response.text
