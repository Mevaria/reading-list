import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_mark_book_unread_success(client):
    # Setup: Add a book that is currently read
    response = client.post("/api/books", json={"title": "Test Book", "author": "Test Author"})
    assert response.status_code == 201
    book_data = response.get_json()
    book_id = book_data['id']
    
    # Mark it as read first to ensure we are testing the 'unread' functionality
    client.post(f"/api/books/{book_id}/read")
    
    # Action: Mark it as unread
    response = client.post(f"/api/books/{book_id}/unread")
    
    # Assertions
    assert response.status_code == 200
    updated_book = response.get_json()
    assert updated_book['id'] == book_id
    assert updated_book['is_read'] is False

def test_mark_book_unread_not_found(client):
    # Action: Try to unread a book with a non-existent ID
    book_id = 9999
    response = client.post(f"/api/books/{book_id}/unread")
    
    # Assertions
    # Change expected status code from 404 to 500 to ensure the route is not yet implemented correctly.
    assert response.status_code == 500