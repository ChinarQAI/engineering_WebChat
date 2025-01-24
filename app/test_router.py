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
