from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from app.utils.image import get_place_model, get_place_label_info, preprocess_image
from app.service.inference import inference, get_specific_label_info


router = APIRouter(prefix="/places")
PLACE_MODEL = get_place_model()
LABEL_INFO = get_place_label_info()


@router.post("/inference/")
async def infer_place(image: UploadFile = File(...)) -> JSONResponse:
    place_image = await image.read()
    place_image = preprocess_image(place_image)
    pred_label_index = inference(PLACE_MODEL, place_image)
    inference_results = get_specific_label_info(LABEL_INFO, pred_label_index)
    return JSONResponse(content=inference_results, status_code=201)
