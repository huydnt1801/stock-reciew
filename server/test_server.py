import pytest
from app import app


class TestServer:
    def test_return_data(self):
        client = app.test_client()
        response = client.get("/health/check")
        assert 200 == response.status_code
        response = client.get("/health/ready")
        assert 200 == response.status_code
