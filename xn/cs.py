from locust import HttpLocust, task, TaskSet


# 定义测试类：用户行为
class UserBehavior(TaskSet):
    # 指定测试任务
    @task
    def test_login(self):
        self.client.get("/")


class WebSiteUser(HttpLocust):
    host="https://www.baidu.com/"
    task_set=UserBehavior
    min_wait=2000
    max_wait=5000


##import time
##from locust import HttpUser, task, between
##
##class QuickstartUser(HttpUser):
##    wait_time = between(1, 2.5)
##
##    @task
##    def hello_world(self):
##        self.client.get("/hello")
##        self.client.get("/world")
##
##    @task(3)
##    def view_items(self):
##        for item_id in range(10):
##            self.client.get(f"/item?id={item_id}", name="/item")
##            time.sleep(1)
##
##    def on_start(self):
##        self.client.post("/login", json={"username":"foo", "password":"bar"})
