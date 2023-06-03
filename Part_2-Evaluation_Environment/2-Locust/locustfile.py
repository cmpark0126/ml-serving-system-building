# locustfile.py
from locust import FastHttpUser, task, between


class ModelsPredictionUser(FastHttpUser):
    wait_time = between(0.1, 0.1)

    @task(1)
    def predict(self):
        self.client.get("/v1/models/resnet50")

    @task(10)
    def inference(self):
        payload = {"inputs": "i", "outputs": "o"}
        self.client.post("/v1/models/resnet/infer", json=payload)
