# @Author : Kql
# @Time : 2023/9/16 10:25
# @FileName : redis_mysql_update.py
# @Blog ：https://blog.csdn.net/weixin_56175042

import redis
import pymysql


class Update(object):
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1',
                                  user='root',
                                  password='xiao9988',
                                  port=3306,
                                  database='userdb',
                                  charset='utf8')
        self.cursor = self.db.cursor()
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    def update_mysql(self, score, username):
        upd = 'update user set score=%s where name=%s;'
        try:
            # code: 0或1，几行受到了影响
            code = self.cursor.execute(upd, [score, username])
            # code为1，说明新成绩和原成绩不一样
            if code == 1:
                self.db.commit()
                return True
        except Exception as e:
            self.db.rollback()
            print("Error", e)

    def update_redis(self, username, score):
        result = self.r.hgetall(username)
        if result:
            self.r.hset(username, 'score', score)
        else:
            self.select_mysql(username)

    def select_mysql(self, username):
        sel = 'select age,gender,score from user where name=%s'
        self.cursor.execute(sel, [username])
        result = self.cursor.fetchall()
        user_dict = {
            'age': result[0][0],
            'genger': result[0][1],
            'score': result[0][2]
        }
        self.r.hset(username, mapping=user_dict)
        # 设置过期时间
        self.r.expire(username, 60)

    def main(self):
        username = input("请输入用户名：")
        new_score = input("请输入一个新的成绩：")
        if self.update_mysql(new_score, username):
            self.update_redis(username, new_score)
        else:
            print("更改信息失败！")


if __name__ == '__main__':
    syn = Update()
    syn.main()
