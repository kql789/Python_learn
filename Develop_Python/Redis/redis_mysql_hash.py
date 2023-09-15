# @Author : Kql
# @Time : 2023/9/15 18:58
# @FileName : redis_mysql_hash.py
# @Blog ：https://blog.csdn.net/weixin_56175042
import redis
import pymysql

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='xiao9988',
                     port=3306,
                     database='userdb',
                     charset='utf8')
cursor = db.cursor()

# 1. 输入要查询的用户名
# 2. 先到redis中查询
# 3. redis中如果没有，到mysql中查询

# key field value

username = input('请输入查询的用户名：')
result = r.hgetall(username)
if result:
    print('redis:', result)
else:
    # mysql中查询
    sql = 'select age,gender,score from user where name=%s'
    cursor.execute(sql, [username])
    userinfo = cursor.fetchall()
    if not userinfo:
        print("用户不存在！")
    else:
        print('mysql:', userinfo)
    # (('niefeng',25,'M'),)
    # 缓存到redis中，设置过期时间30秒
        user_dict = {
            'age': userinfo[0][0],
            'genger': userinfo[0][1],
            'score': userinfo[0][2]
        }
        r.hset(username, mapping=user_dict)
        # 设置过期时间
        r.expire(username, 30)
