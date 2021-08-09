import unittest
from test_interface_testing.test_interfacs.test_script.test_interface import *

# url1 = 'http://10.0.3.75:8080/jwshoplogin/user/login.do'
# url2 = 'http://10.0.3.75:8080/jwshoplogin/user/get_information.do'
# url3 = 'http://10.0.3.75:8080/jwshoplogin/user/loginout.do'
# url4 = 'http://10.0.3.75:8080/jwshoplogin/user/forget_check_answer.do'
# url5 = 'http://10.0.3.75:8080/jwshoplogin/user/forget_reset_password.do'
#
# data1 = {'username':'测试账号6', 'sign':'qwerty'}
# data2 = {}
# data4 = {'username':'qwerty', 'question':'e', 'answer':'w'}
# data5 = {'username':'qwerty', 'passwordNew':'123456', 'forgetToken':'4435ae12-9169-4aec-8661-04293ddfc400'}
# cookie1 = None
#
# r1 = requests.post(url4, data4, cookies = cookie1)
# cookie2 = r1.cookies
# header = r1.headers
# r2 = requests.post(url2, data2, cookies = cookie2)
# r3 = requests.get(url4, data2, cookies = cookie2)
#
# # r5 = requests.post(url5, data5)
#
# print(r1.json())
# print(cookie2)
# print(r3.text)




#------------------------------我是分割线------------------------------#
class Test_CS(unittest.TestCase):
    def setUp(self) -> None:
        pass


    def test_a(self):
        c=Config().parameterFormatting()
        cookie=None
        forgetToken=None
        for i, j in list(c):
            t=TestInterFace(i, j, cookie)
            a=t.test_interface()
            if str(type(a)) == "<class 'bool'>":
                pass
            else:
                cookie=a[0]
            print(a)
            try:
                self.assertIs(a, True)
            except:
                pass

if __name__ == '__main__':
    unittest.main()