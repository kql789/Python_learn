# @Author : Kql
# @Time : 2023/9/16 17:39
# @FileName : redis_case2.py
# @Blog ：https://blog.csdn.net/weixin_56175042
import redis

"""
京东手机畅销榜
获取三款手机的销量排名
"""
r = redis.Redis(host='127.0.0.1', port=6379, db=0, charset='utf8')

day01_dict = {
    'huawei': 5000,
    'oppo': 3000,
    'iphone': 4000
}

day02_dict = {
    'huawei': 5200,
    'oppo': 3300,
    'iphone': 4400
}
day03_dict = {
    'huawei': 6000,
    'oppo': 3800,
    'iphone': 5900
}
r.zadd('mobile:001', day01_dict)
r.zadd('mobile:002', day02_dict)
r.zadd('mobile:003', day03_dict)

# 求并集mobile:001-003
r.zunionstore('mobile:001-003',
              ('mobile:001', 'mobile:002', 'mobile:003'),
              aggregate='max')
# 求排名
result = r.zrevrange('mobile:001-003', 0, 2, withscores=True)

# 打印输出
i = 1
for rank in result:
    string = "第{}名:{} 销量:{}"
    print(string.format(i, rank[0].decode(), int(rank[1])))
    i += 1
