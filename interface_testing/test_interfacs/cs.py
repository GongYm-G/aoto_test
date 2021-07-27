import requests
import unittest
from interface_testing.test_interfacs.test_interface import *

url1 = 'http://10.0.3.75:8080/jwshoplogin/user/login.do'
url2 = 'http://10.0.3.75:8080/jwshoplogin/user/get_information.do'
url3 = 'http://10.0.3.75:8080/jwshoplogin/user/loginout.do'

data1 = {'username':'测试账号6', 'password':'qwerty'}
data2 = {}
cookie1 = None

r1 = requests.post(url1, data1, cookies = cookie1)
cookie2 = r1.cookies
r2 = requests.post(url2, data2, cookies = cookie2)
r3 = requests.get(url3, data2, cookies = cookie2)
print(r1.json())

print(cookie2)
print(r3.text)




#------------------------------我是分割线------------------------------#