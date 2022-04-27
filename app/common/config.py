from typing import List
from decouple import config, Csv
from pydantic import BaseSettings


class BaseConfig(BaseSettings):
    ALLOWED_HOST: List[str] = config("ALLOWED_HOST", default="127.0.0.1", cast=Csv())


class MLSettings(BaseConfig):
    IMAGE_SIZE: tuple = (224, 224)
    MODEL_PATH: str = "app/ml_model/efn_b0_224_na_5-0.43-0.90.h5"
    LABEL_PATH: str = "app/ml_model/place_55_label.json"
