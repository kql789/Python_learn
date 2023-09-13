# @Author : Kql
# @Time : 2023/9/13 16:25
# @FileName : redis_test.py
# @Blog ：https://blog.csdn.net/weixin_56175042
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# 添加一个列表mylist
r.lpush('mylist', '1', '2', 3)
r.lpush('mylist2', '1', '2', 3)
key_list = r.keys('*')
print(key_list)
print(r.type('mylist'))
print(r.exists('mylist'))
# 删除
r.delete('mylist2')
print(r.keys('*'))
# r.expire('mylist', 5)
