from locust import HttpLocust, task, TaskSet

# 定义测试类：用户行为
class UserBehavior(TaskSet):
    # 指定测试任务
    @task
    def test_login(self):
        self.client.get("/")

class WebSiteUser(HttpLocust):
    host = "https://www.baidu.com/"
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 5000