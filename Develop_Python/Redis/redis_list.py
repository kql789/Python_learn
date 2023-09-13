# @Author : Kql
# @Time : 2023/9/13 16:58
# @FileName : redis_list.py
# @Blog ：https://blog.csdn.net/weixin_56175042
# redis操作列表
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# 列表操作
r.rpush('tedu:teachers', 'lao', 'kql', 'laoguo')
r.rpush('tedu:teachers', 'Chaogege')

# 在kql后面加上一个zhangsan
r.linsert('tedu:teachers', 'after', 'kql', 'zhangsan')

# 打印长度
print(r.llen('tedu:teachers'))
print(r.lrange('tedu:teachers', 0, -1))

# 弹出一个元素
print(r.rpop('tedu:teachers'))
# 保留指定范围内元素
r.ltrim('tedu:teachers', 0, 2)
print(r.lrange('tedu:teachers', 0, -1))
# 设置有效期
r.expire('tedu:teachers', 5)
