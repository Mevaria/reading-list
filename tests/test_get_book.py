
import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_get_book_success(client):
    # Add a book first
    response_add = client.post("/api/books", json={"title": "The Hobbit", "author": "J.R.R. Tolkien"})
    assert response_add.status_code == 201
    book_id = response_add.get_json()["id"]

    # Test fetching the book
    response = client.get(f"/api/books/{book_id}")
    assert response.status_code == 200
    book = response.get_json()
    assert book["id"] == book_id
    assert book["title"] == "The Hobbit"
    assert book["author"] == "J.R.R. Tolkien"


def test_get_book_not_found(client):
    # Test fetching a book that does not exist
    non_existent_id = 9999
    response = client.get(f"/api/books/{non_existent_id}")
    assert response.status_code == 404
    assert response.get_json() == {"error": "Book not found"}
