import pytest
import tempfile
import requests


@pytest.fixture
def dummy_image():
    url = f"https://picsum.photos/id/1/256/256"
    image = requests.get(url)
    with tempfile.NamedTemporaryFile(suffix=".jpg", dir="./") as f:
        f.write(image.content)
        byte_image = open(f.name, "rb")
    return byte_image
