import base64
import string
import random
import hashlib
from pprint import pprint
from collections import OrderedDict
from requests import post

# base_url = '你的调试地址'
# app_key = '你的 appkey'
# key = '你的签名秘钥' testapitoken


def sign(data, key):
    """md5 签名"""
    s = ''
    need_signed = dict(_flatten_dict(data))
    for k in sorted(need_signed, key = str.lower):
        s += '{k}={v}&'.format(k = k.lower(), v = need_signed[k])
    s += 'key=' + key
    # print(s)
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest().upper()


def _flatten_dict(d):
    items = []
    for k, v in d.items():
        if isinstance(v, (list, tuple)):
            continue
        elif isinstance(v, dict):
            items.extend(_flatten_dict(v))
        else:
            items.append((k, v))
    return items


def nonce():
    """生成随机字符串"""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))


if __name__ == '__main__':
    data = {
            "AppKey": "10222",
            "NonceStr": "greeteryer",
            "UserIndicateId": "2dl1z+sGrjQxacSkbKPxYg=="
        }

    # b = nonce()
    # a = {'NonceStr': b}
    # data.update(a)
    si = sign(data, 'testapitoken')
    s = {'Sign': si}
    data.update(s)
    print(data)