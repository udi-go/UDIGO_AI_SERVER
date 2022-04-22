import pytest
import tempfile
import requests
from app.utils.image import read_byte_image


def get_test_image():
    url = f"https://picsum.photos/id/1/256/256"
    image = requests.get(url)
    byte_image = image.content
    return byte_image


@pytest.fixture
def byte_image():
    byte_image = get_test_image()
    return byte_image


@pytest.fixture
def normal_image():
    image = get_test_image()
    noraml_image = read_byte_image(image)
    return noraml_image
