import pytest
from fastapi.testclient import TestClient
from backend.main import app   # importa tu FastAPI

@pytest.fixture
def client():
    return TestClient(app)
