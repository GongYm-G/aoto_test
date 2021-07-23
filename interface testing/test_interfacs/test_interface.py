import requests

class TestInterFace:

    def __init__(self):
        pass

    def test_interface(self):
        url = 'http://10.0.3.75:8080/jwshoplogin/user/login.do'
        data={
            'username':'qwerty',
            'password':'123456'
        }
        r = requests.post(url, data)
        print(r.text)
        print('登录成功' in r.text)



if __name__ == '__main__':
    t = TestInterFace()
    t.test_interface()