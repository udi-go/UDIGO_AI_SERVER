import json
import cv2
import numpy as np 
from tensorflow.keras.models import load_model

def inference(image):
    model = _get_place_model()
    pred = model.predict(image, batch_size=1)
    return str(np.argmax(pred))

def preprocess_image(image):
    image = _resize_image(image)
    image = _add_axis_to_image(image)
    return image

def _get_place_model():
    model = load_model("place/model/efn_b0_224_na_5-0.43-0.90.h5")
    return model

def _get_place_labels():
    with open("ml_model/place_55_label.json", "r", encoding="utf-8-sig") as f:
        label_info = json.load(f)
    return label_info
    
def _resize_image(byte_image):
    image = cv2.imdecode(
            np.fromstring(byte_image, np.uint8), cv2.IMREAD_UNCHANGED
        )
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, IMAGE_SIZE)
    return image

def _add_axis_to_image(image):
    image = image[np.newaxis, :, :, :]
    return image