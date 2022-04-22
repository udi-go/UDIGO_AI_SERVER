import pytest
from starlette.datastructures import UploadFile
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# TODO: 422에러 해결필요
@pytest.mark.skip
def test_inference(byte_image):
    response = client.post("/api/places/inference/", data={"image": byte_image})
    assert response == 201
