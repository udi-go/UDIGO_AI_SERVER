import numpy as np
from utils.image import get_place_model


def inference(image):
    model = get_place_model()
    pred = model.predict(image, batch_size=1)
    return str(np.argmax(pred))
