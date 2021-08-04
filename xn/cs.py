from locust import HttpUser, task, TaskSet
import time,requests
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.post("http://10.0.2.62:50500/Login/Login", json={"UserName":"13700000001", "Password":123456,'LoginType':3})


    def on_start(self):
        a=self.client.post("http://10.0.2.62:50500/Login/Login", json={"UserName":"13700000001", "Password":123456,'LoginType':3}).text
        if a.find('金太阳第一中学')>0:
            print(True)
        else:
            print(False)
