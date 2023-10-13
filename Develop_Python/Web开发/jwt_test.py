# @Author : Kql
# @Time : 2023/8/29 11:04
# @FileName : jwt_test.py
# @Blog ：https://blog.csdn.net/weixin_56175042
"""
Jwt模拟签名
优化点：header可以省略,从而可以节省流量
"""
import hmac
import base64
import json
import time
import copy


class Jwt():
    def __int__(self):
        pass

    @staticmethod
    def b64encode(content):
        return base64.urlsafe_b64encode(content).replace(b'=', b'')

    @staticmethod
    def b64decode(b):
        # base64编码后的长度一定能被4整除
        sem = len(b) % 4
        if sem > 0:
            b += b'=' * (4 - sem)
        return base64.urlsafe_b64decode(b)

    @staticmethod
    def encode(payload, key, exp=30):
        # init header
        header = {'typ': 'JWT', 'alg': 'HS256'}
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        header_bs = Jwt.b64encode(header_json.encode())

        # init payload
        payload_self = copy.deepcopy(payload)
        if not isinstance(exp, int) and not isinstance(exp, str):
            raise TypeError("Exp must be int or str")
        payload_self['exp'] = time.time() + int(exp)
        payload_js = json.dumps(payload_self, separators=(',', ':'), sort_keys=True)
        payload_bs = Jwt.b64encode(payload_js.encode())

        # init sign
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256')
        sign_bs = Jwt.b64encode(hm.digest())
        return header_bs + b'.' + payload_bs + b'.' + sign_bs

    @staticmethod
    def decode(token, key):
        """
        校验签名
        检查exp是否过期
        return payload部分
        """
        header_bs, payload_bs, sign_bs = token.split(b'.')
        # 校验sign_bs
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256')
        # 比对两次的sign的结果
        if sign_bs != Jwt.b64encode(hm.digest()):
            raise ValueError("sign not match")
        # 检查是否过期
        payload_js = Jwt.b64decode(payload_bs)
        payload = json.loads(payload_js)
        if 'exp' in payload:
            now = time.time()
            if now > payload['exp']:
                raise ValueError("Time has expired")
        return payload


if __name__ == '__main__':
    token = Jwt.encode({'username': 'kanqilu123'}, '123456', 15)
    print("生成token如下：")
    print(token)
    print("校验结果如下：")
    print(Jwt.decode(token, '123456'))
