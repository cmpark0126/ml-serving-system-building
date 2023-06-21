# locustfile.py
from locust import TaskSet, FastHttpUser, task, between, events


# 실험 별로 시작할 때 1번 실행
# e.g., data 초기화
@events.test_start.add_listener
def on_test_start(**kw):
    print("test is starting")


# 실험 별로 끝날 때 1번 실행
# e.g., data 저장
@events.test_stop.add_listener
def on_test_stop(**kw):
    print("test is stopping")


class UserBehavior(TaskSet):
    # User 별로 시작할 때 1번 실행
    # e.g., history 초기화
    def on_start(self):
        print("nested on start")

    # User 별로 끝날 때 1번 실행
    # e.g., history 저장
    def on_stop(self):
        print("nested on stop")

    # Task 호출 가중치
    @task(1)
    def get_metadata(self):
        self.client.get("/v1/models/resnet50")

    # Task 호출 가중치
    @task(2)
    def infer(self):
        payload = {"inputs": "i", "outputs": "o"}
        self.client.post("/v1/models/resnet/infer", json=payload)


# 한 번에 하나의 요청만 보냄
class User(FastHttpUser):
    # : 뒤에 있는 값은 여러개의 taskset이 있을 때 가중치
    tasks = {UserBehavior: 1} # type: ignore
    wait_time = between(0.1, 0.2)
