import numpy as np
from app.utils.image import get_place_model, get_place_label_info


def inference(model, image) -> str:
    pred = model.predict(image, batch_size=1)
    return str(np.argmax(pred))


def get_specific_label_info(label: dict, index: str) -> dict:
    label_info = label[index]
    label_category = label_info["category"]
    random_label_sentence = np.random.choice(label_info["sentence"])
    return {"label_category": label_category, "sentence": random_label_sentence}
