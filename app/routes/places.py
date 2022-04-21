from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from app.utils.image import preprocess_image
from app.service.inference import inference, get_specific_label_info


router = APIRouter(prefix="/places")


@router.post("/inference/")
async def infer_place(image: UploadFile = File(...)) -> JSONResponse:
    print(type(image))
    place_image = await image.read()
    place_image = preprocess_image(place_image)
    pred_label_index = inference(place_image)
    inference_results = get_specific_label_info(pred_label_index)
    return JSONResponse(content=inference_results, status_code=201)
