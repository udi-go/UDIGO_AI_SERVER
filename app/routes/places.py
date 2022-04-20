from fastapi import APIRouter, File, UploadFile
from utils.image import preprocess_image

router = APIRouter(prefix="/places")


@router.post("inference")
async def infer_place(image: UploadFile = File(...)):
    place_image = await image.read()
    place_image = preprocess_image(place_image)

    return ""
