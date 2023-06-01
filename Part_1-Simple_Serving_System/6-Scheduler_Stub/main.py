from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI()


class InferData(BaseModel):
    inputs: Any
    outputs: Any


@app.get("/v2/models/{model}")
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


@app.get("/v2/models/{model}/config")
async def get_config(model: str):
    # TODO: obtained from model registry in the future
    dummy = {
        "name": model,
    }
    return dummy


@app.get("/v2/models/{model}/stats")
async def get_stats(model: str):
    # TODO: obtained from model registry in the future
    dummy = {
        "name": model,
    }
    return dummy


@app.get("/v2")
async def get_api_metadata():
    # NOTE: simulate triton server
    dummy = {
        "name": "triton",
        "version": "2.33.0",
        "extensions": [
            "classification",
            "sequence",
            "model_repository",
            "model_repository(unload_dependents)",
            "schedule_policy",
            "model_configuration",
            "system_shared_memory",
            "cuda_shared_memory",
            "binary_tensor_data",
            "parameters",
            "statistics",
            "trace",
            "logging",
        ],
    }
    return dummy


@app.post("/v2/models/{model}/infer")
async def infer(model: str, infer_data: InferData):
    print(f"Received request for model {model} with data: {infer_data}")
    return infer_data


# Run this server with: uvicorn main:app --reload
