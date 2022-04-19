import json
import cv2
import numpy as np 
from fastapi import APIRouter, File, UploadFile
from fastapi.logger import logger
from tensorflow.keras.models import load_model


router = APIRouter(prefix="/places")


IMAGE_SIZE = (224, 224)

def get_place_labels():
    with open("ml_model/place_55_label.json", "r", encoding="utf-8-sig") as f:
        label_info = json.load(f)
    return label_info


def get_place_model()
    model = load_model("place/model/efn_b0_224_na_5-0.43-0.90.h5")
    return model

def resize_image(byte_image):
    image = cv2.imdecode(
            np.fromstring(byte_image, np.uint8), cv2.IMREAD_UNCHANGED
        )
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, IMAGE_SIZE)
    return image

def add_axis_to_image(image):
    image = image[np.newaxis, :, :, :]
    return image

def inference(image):
    pred = model.predict(image, batch_size=1)
    return str(np.argmax(pred))


@router.post("inference")
async def infer_place():
    return ""
