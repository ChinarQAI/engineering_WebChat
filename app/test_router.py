import pytest
from fastapi.testclient import TestClient
import sys
import os
from unittest.mock import patch

# Adding paths to import custom modules
sys.path.insert(1, "src")
sys.path.insert(2, "app")
sys.path.insert(3, "config")

from app.router import app  
from app.settings_manager import fetch_settings

# Create a test client for the FastAPI app
client = TestClient(app)

def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Service is healthy and running."}

@pytest.fixture
def mock_redis_client():
    """Fixture to mock the Redis client."""
    with patch("app.settings_manager.redis_client") as mock_client:
        yield mock_client

def test_fetch_settings_cqai_chat(mock_redis_client):
    """Test the fetch_settings function for app_id 'cqai_chat'."""
    # Mock Redis `get` method for app_id 'cqai_chat'
    mock_redis_client.get.return_value = '{"setting1": "value1", "setting2": "value2"}'
    
    # Call the function
    app_id = "cqai_chat"
    settings = fetch_settings(app_id)
    
    # Assert the returned settings
    assert settings == {"setting1": "value1", "setting2": "value2"}
    
    # Verify the `get` method was called with the correct app_id
    mock_redis_client.get.assert_called_once_with(app_id)
