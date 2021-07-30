import requests
from interface_testing.test_interfacs.config import Config


class TestInterFace:
    def __init__(self, values, data, cookie=None):
        self.joint = values[-1]
        self.result = values[1]
        self.post = values[3]
        self.url = values[4]
        self.data = data
        self.cookie = cookie

    def requestsManner(self):
        if self.post == 'POST':
            r = requests.post(self.url, self.data, cookies = self.cookie)
            return r
        elif self.post == 'GET':
            r = requests.get(self.url, self.data, cookies = self.cookie)
            return r
        else:
            print('请求方式错误，请使用GET或POST方式进行请求')

    def test_interface(self):
        if self.joint == '是':
            a = self.requestsManner()
            if self.result in a.text:
                self.cookie = a.cookies
                print('pass', a.text)
                return True
            else:
                self.cookie=a.cookies
                print('fail', a.text)
                return False

        else:
            a = self.requestsManner()
            if self.result in a.text:
                print('pass', a.text)
                return True
            else:
                print('fail', a.text)
                return False


if __name__ == '__main__':
    c = Config().parameterFormatting()

    for i, j in list(c):
        t = TestInterFace(i, j)
        a = t.test_interface()
        if str(type(a)) == "<class 'bool'>":
            pass
        else:
            cookie = a[0]

