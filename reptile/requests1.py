import requests
import re


class RQ:
    def __init__(self, url, values):
        self.url = url
        self.UserName = values['UserName']
        self.Password=values['Password']
        self.LoginType=values['LoginType']




    # r = requests.post(url, values)
    # q = r.text
    # w = re.split(',', q)
    # print(w)
    # for i in w:
    #     print(i)



url = 'http://10.0.2.62:50500/Login/Login'
values = {'UserName':'qingypqgly', 'Password':666666, 'LoginType':3}
r = RQ(url, values)
print(r)