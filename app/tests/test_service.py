from app.service.inference import inference, get_place_label_info
from app.utils.image import preprocess_image


def test_inference(byte_image):
    image = preprocess_image(byte_image)
    pred = inference(image)
    assert pred in [str(i) for i in range(0, 55)]


def test_get_place_label_info():
    label_info = get_place_label_info()
    assert type(label_info) == dict
