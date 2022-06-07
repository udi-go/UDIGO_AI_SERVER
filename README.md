# UDIGO AI Inference server 
- Framework: FastAPI, Tensorflow

## 55개의 장소이미지를 학습한 이미지 분류모델 서빙

- UDIGO WAS에서 이미지를 받아서 추론하고 **카테고리**와 카테고리를 설명하는 한 문장을 return
    - label_category: 추론한 카테고리
    - sentence: 카테고리에 적합한 설명하는 멘트 

- 기존의 안드로이드 앱과 연동되는 것과는 별개로 WAS가 없는 Web Frontend와 연결되는 프로젝트도 존재
    - [WEB](https://github.com/udi-go/UDIGO_FRONTEND)
---
- Endpoint: input - image
    - /api/places/inference
    
