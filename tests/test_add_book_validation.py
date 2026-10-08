
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_add_book_whitespace_title_rejected(client):
    # Test case: Title consists only of whitespace
    payload = {"title": "   ", "author": "Test Author"}
    response = client.post("/api/books", json=payload)
    
    # Expect rejection with 400 status code
    assert response.status_code == 400
    
    # Optionally check for an error message, though the spec only requires rejection like a missing title
    response_data = response.get_json()
    assert "error" in response_data
