from pydantic import BaseSettings


class MLSettings(BaseSettings):
    IMAGE_SIZE: tuple = (224, 224)
    MODEL_PATH: str = "ml_model/efn_b0_224_na_5-0.43-0.90.h5"
    LABEL_PATH: str = "ml_model/place_55_label.json"
