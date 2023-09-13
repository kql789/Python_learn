# @Author : Kql
# @Time : 2023/9/13 17:44
# @FileName : redis_str.py
# @Blog ：https://blog.csdn.net/weixin_56175042
# redis操作字符串
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.set('user001:name', 'guods')
m_dict = {
    'user001:age': 34,
    'user001:gender': 'M'
}
r.mset(m_dict)

print(r.get('user001:name'))
print(r.mget('user001:age', 'user001:gender'))
# 获取长度
print(r.strlen('user001:name'))

# 数字操作
r.incr('user001:age', 1)
r.decr('user001:age', 1)

r.incrby('user001:age', 3)
r.decrby('user001:age', 3)

r.incrbyfloat('user001:age', 2.8)
r.incrbyfloat('user001:age', -2.8)
print(r.get('user001:age'))
