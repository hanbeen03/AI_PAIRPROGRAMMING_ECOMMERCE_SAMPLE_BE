from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
# from app.core.config import settings

app = FastAPI()

# # CORS 미들웨어 설정
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.CORS_ORIGINS,  # settings.CORS_ORIGINS는 본인의 설정에 맞게 정의
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

API_V1_STR = "/api/v1"
# API 라우터 추가
app.include_router(api_router, prefix=API_V1_STR)

# 선택적: 루트 경로에 대한 간단한 테스트 엔드포인트
@app.get("/")
def root():
    return {"message": "Hello World from FastAPI"}

# @app.get("/test")
# def root_test():
#     c = 0
#     for i in range(100):
#         c += int(str(int(str(i))))

#     return {"message": "This is just test endpoint for code review." + str(c)}