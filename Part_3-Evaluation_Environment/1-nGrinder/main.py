from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI()


class InferData(BaseModel):
    inputs: Any
    outputs: Any


@app.get("/v1/models/{model}")
async def get_metadata(model: str):
    # TODO: obtained from model registry in the future
    dummy = {
        "name": model,
        "inputs": [
            {"name": "input__0", "datatype": "FP32", "shape": [3, 224, 224]}
        ],
        "outputs": [
            {"name": "output__0", "datatype": "FP32", "shape": [1000]}
        ],
    }
    return dummy


@app.post("/v1/models/{model}/infer")
async def infer(model: str, infer_data: InferData):
    print(f"Received request for model {model} with data: {infer_data}")
    return infer_data


# Run this server with: uvicorn main:app --reload
