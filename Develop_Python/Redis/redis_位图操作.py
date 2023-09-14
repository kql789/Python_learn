# @Author : Kql
# @Time : 2023/9/14 16:57
# @FileName : redis_位图操作.py
# @Blog ：https://blog.csdn.net/weixin_56175042
# 模拟位图操作应用场景
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# user001 一年中第五天和第200天登录
r.setbit('user:001', 4, 1)
r.setbit('user:001', 199, 1)
# user002 一年中第100天和第300天登录
r.setbit('user:002', 99, 1)
r.setbit('user:002', 299, 1)
# user003 登录了100次以上
for i in range(0, 365, 2):
    r.setbit('user:003', i, 1)
# user004 登录了100次以上
for i in range(0, 365, 3):
    r.setbit('user:004', i, 1)
# 返回列表
user_list = r.keys('user:*')
active_users = []
noactive_users = []
# 遍历
for user in user_list:
    login_count = r.bitcount(user)
    if login_count > 100:
        active_users.append((user, login_count))
    else:
        noactive_users.append((user, login_count))

print("活跃用户", active_users)
print("不活跃用户", noactive_users)
