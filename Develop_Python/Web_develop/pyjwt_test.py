# @Author : Kql
# @Time : 2023/8/29 15:19
# @FileName : pyjwt_test.py
# @Blog ：https://blog.csdn.net/weixin_56175042
import time

import jwt

payload = {'username': 'kql', 'exp': time.time() + 15}

# 生成token
a = jwt.encode(payload, '123456', algorithm='HS256')
print(a)

# 解码token
b = jwt.decode(a, '123456', algorithms='HS256')
print(b)
