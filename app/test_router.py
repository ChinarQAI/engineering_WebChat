import pytest
from fastapi.testclient import TestClient
from router import app  # Ensure 'router' matches your application filename

# Create a test client for the FastAPI app
client = TestClient(app)

def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Service is healthy and running."}