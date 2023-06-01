from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI()


class InferData(BaseModel):
    inputs: Any
    outputs: Any


@app.post("/v2/models/{model}/infer")
async def infer(model: str, infer_data: InferData):
    print(f"Received request for model {model} with data: {infer_data}")

    # 여기서 실제로 모델의 추론을 수행할 수 있습니다.
    # 여기에서는 간단하게 요청 데이터를 그대로 반환하도록 하겠습니다.
    return infer_data

# Run this server with: uvicorn main:app --reload
