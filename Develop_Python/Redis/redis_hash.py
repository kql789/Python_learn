# @Author : Kql
# @Time : 2023/9/14 17:57
# @FileName : redis_hash.py
# @Blog ：https://blog.csdn.net/weixin_56175042
# python与redis交互

import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# hset+hget
r.hset('user1', 'name', 'kql')
print(r.hget('user1', 'name'))

# hmset+hmget
user_dict = {
    'password': '123456',
    'gender': 'M',
    'girlfriend': 'chuchu'
}
r.hset('user1', mapping=user_dict)

print(r.hmget('user1', 'name', 'password', 'gender', 'girlfriend'))

# hgetall+hkeys+hvals
print(r.hgetall('user1'))
print(r.hkeys('user1'))
print(r.hvals('user1'))
# hdel
r.hdel('user1', 'gender')
print(r.hgetall('user1'))

# 应用场景
"""
微博好友关注
1. 用户id为key，field为好友id，value为关注时间
key      field      value
user:10  user:606   20230101

2. 用户维度统计
统计数：关注数、粉丝数、喜欢商品数、发帖数
用户为key 不同维度field，value为统计数
比如关注了5人
hset user:1000 fans 5
hincrby user:1000 fans 1
"""
