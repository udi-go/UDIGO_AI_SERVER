import json
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from app.common.config import MLSettings


ml_settings = MLSettings()


def preprocess_image(bytes_image: bytes):
    image = read_byte_image(bytes_image)
    image = _resize_image(image)
    image = _add_axis_to_image(image)
    return image


def get_place_model():
    model = load_model(ml_settings.MODEL_PATH)
    return model


def get_place_label_info():
    with open(ml_settings.LABEL_PATH, "r", encoding="utf-8-sig") as f:
        label_info = json.load(f)
    return label_info


def read_byte_image(bytes_image):
    image = cv2.imdecode(np.frombuffer(bytes_image, np.uint8), cv2.IMREAD_UNCHANGED)
    return image


def _resize_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, ml_settings.IMAGE_SIZE)
    return image


def _add_axis_to_image(image):
    image = image[np.newaxis, :, :, :]
    return image
