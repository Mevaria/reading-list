
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_delete_existing_book_success(client):
    # Setup: Add a book first
    response = client.post("/api/books", json={"title": "Test Book", "author": "Test Author"})
    assert response.status_code == 201
    book_id = response.json["id"]

    # Action: Delete the book
    response = client.delete(f"/api/books/{book_id}")

    # Assert: Successful deletion returns 204 and an empty body
    assert response.status_code == 204
    assert response.data == b''

def test_delete_non_existent_book_failure(client):
    # Action: Attempt to delete a book with a non-existent ID (e.g., 999)
    response = client.delete("/api/books/999")

    # Assert: Failure returns 404 and the specific error JSON
    assert response.status_code == 404
    assert response.get_json() == {"error": "Book not found"}
