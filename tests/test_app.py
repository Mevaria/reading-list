import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_list_starts_empty(client):
    response = client.get("/api/books")
    assert response.status_code == 200
    assert response.get_json() == []


def test_add_book(client):
    response = client.post("/api/books", json={"title": "Dune", "author": "Frank Herbert"})
    assert response.status_code == 201
    book = response.get_json()
    assert book["title"] == "Dune"
    assert book["is_read"] is False


def test_add_book_requires_title(client):
    response = client.post("/api/books", json={"author": "Nobody"})
    assert response.status_code == 400


def test_mark_read(client):
    book_id = client.post("/api/books", json={"title": "Dune"}).get_json()["id"]
    response = client.post(f"/api/books/{book_id}/read")
    assert response.status_code == 200
    assert response.get_json()["is_read"] is True


def test_mark_read_missing_book(client):
    response = client.post("/api/books/999/read")
    assert response.status_code == 404


def test_index_page_renders(client):
    client.post("/api/books", json={"title": "Dune", "author": "Frank Herbert"})
    response = client.get("/")
    assert response.status_code == 200
    assert b"Dune" in response.data
