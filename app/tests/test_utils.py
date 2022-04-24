import numpy as np
from tensorflow.keras import Model
from app.utils.image import (
    read_byte_image,
    _resize_image,
    _add_axis_to_image,
    get_place_model,
    get_place_label_info,
    preprocess_image,
)


def test_read_byte_image(byte_image):
    image = read_byte_image(byte_image)
    assert len(image.shape) == 3
    assert type(image) == np.ndarray


def test_resize_image(normal_image):
    resized_image = _resize_image(normal_image)
    assert resized_image.shape == (224, 224, 3)


def test_add_axis_to_image(normal_image):
    add_axis_image = _add_axis_to_image(normal_image)
    assert add_axis_image.shape[0] == 1


def test_get_place_model():
    model = get_place_model()
    assert "predict" in model.__dir__()


def test_get_place_label_info():
    label_info = get_place_label_info()
    assert type(label_info) == dict


def test_preprocess_image(byte_image):
    preprocessed_image = preprocess_image(byte_image)
    assert type(preprocessed_image) == np.ndarray
    assert preprocessed_image.shape == (1, 224, 224, 3)
