# @Author : Kql
# @Time : 2023/9/16 17:19
# @FileName : redis_case1.py
# @Blog ：https://blog.csdn.net/weixin_56175042

import redis

""""
网易音乐排行榜前3名
1. 每首歌的歌名作为元素
2. 每首歌的播放次数作为分值
3. 使用zrevrange 来获取播放次数最多的歌曲
"""

r = redis.Redis(host='127.0.0.1', port=6379, db=0, charset='utf8')

# 有序集合-song-rank,参数为字典

r.zadd('song:rank', {'稻香': 1, '以父之名': 10, '偏爱': 1})
r.zadd('song:rank', {'我们的爱': 2, '故乡': 1, '蓝莲花': 1})
r.zincrby('song:rank', 50, '稻香')
r.zincrby('song:rank', 30, '偏爱')
r.zincrby('song:rank', 40, '蓝莲花')

# 查看排名，前3名
# 输出格式：[(b'\xe7\xa8\xbb\xe9\xa6\x99', 51.0), (b'\xe8\x93\x9d\xe8\x8e\xb2\xe8\x8a\xb1', 41.0), (b'\xe5\x81\x8f\xe7\x88\xb1', 31.0)]
result = r.zrevrange('song:rank', 0, 2, withscores=True)
print(result)

# 第一名 稻香 播放次数：51
i = 1
for rank in result:
    string = "第{}名:{} 播放次数:{}"
    print(string.format(i, rank[0].decode(), int(rank[1])))
    i += 1
