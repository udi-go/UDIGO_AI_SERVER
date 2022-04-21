from starlette.datastructures import UploadFile
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# TODO: 422에러 해결필요
def test_inference(dummy_image):
    response = client.post("/api/places/inference/", data={"image": dummy_image})
    assert response == 201
