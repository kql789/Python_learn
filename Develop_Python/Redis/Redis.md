# Redis

## 特点及优点

![redis](./photo/redis_te.png)

## 与其他数据库对比

![redis](./photo/redis_y.png)

## 应用场景

![redis_b](./photo/redis_b.png)

## 附加功能

![redis](./photo/redis_c.png)

## 安装

**Ubuntu**

```shell
#安装
sudo apt-get install redis-server
#启动、停止、暂停
sudo /et/init.d/redis-server status | start| stop|restart
#客户端连接
redis-cli -h Ip -p 6379 -a password
```

## 通用命令，适用于所有数据类型

```shell
# 切换库 0-15
select number
#查看所有键
kyes 表达式
#数据类型
TYPE key
#键是否存在
exists key  
#删除键
dek key
#键重命名
rename key newkey
#清除当前库中所有数据
flushdb
#清除所有库中所有数据
flushll
```

# 字符串类型

- 特点
    - 1.字符串、数字、都会转为字符串来存储
    - 2.以二进制的方式存储在内存中

## 字符串常用命令 —必须掌握

```shell
set key value
get key
#key不存在时再进行设置
set key value nx
#设置过期时间(ex)
set key value ex seconds
#同时设置多个key-value
mset key1 value1 key2 value2 key3 value3
#同时获取多个key-value
mget key1 key2 key3
```

## 字符串常用命令 -了解

```shell
#获取字符串长度
strlen key
#获取指定范围切片内容
getrange key start stop
#从索引开始，value替换原内容
setrange key index value 
#追加拼接value的值
append key value
```

## 字符串数值操作-必须掌握

```shell
#整数操作
INCRBY key 步长
DECRBY key 步长
INCR key +1操作
DECR key -1操作
#应用场景：抖音上有人关注了你，是不是可以用INCR呢，如果取消了关注是不是可以用DECR
#浮点数操作：自动先转为数字操作，然后再进行相加减，不能使用append
incrbyfloat key stop
```

## 键的命名规范

```shell
mset wang:email wangwei@126.com kql:email kql@126.com
```

## string值取值原则

- key值不宜过长，消耗内存，且在数据中查找这类键值的计算成本高
- 不宜过短，可读性较差
- 一个字符串类型的值最多能存储512m内容。

# 列表

## 特点

    - 元素是字符串类型
    - 列表头尾增删快
    - 元素可重复
    - 最多可包含2^32-1个元素
    - 索引同python列表

## 常用命令

```
#增
#从头部压入元素
lpush key value1 value2 value3
#从尾部压入元素
rpush key value1 value2 value3
#从列表src尾部弹出一个元素，压入到列表dst的头部
rpoplpush src dst
# 在列表指定元素后/前插入元素
linsert key before|after value newvalue
#查
#查看列表元素
lrange key start stop
# 查看列表长度
llen key

#删
#从列表头部弹出一个元素
lpop key
#从列表尾部弹出一个元素
rpop key
#列表头部，阻塞弹出，列表为空时阻塞
brpop key timeout
#列表尾部，阻塞弹出，列表为空时阻塞
brpop key timeout

关于blpop和brpop说明：
1. 如果弹出的列表为空或不存在，就会阻塞
2. 超时时间设置为0，就是永久阻塞，直到有数据可以弹出
3. 如果多个客户端阻塞在同一个列表上，使用first in first service原则，即先到先得服务。

#删除指定元素
lrem key count value
count>0 表示从头部开始向表尾搜索，移除与value相等的元素，数量为count。
count<0 表示从尾部开始向头部搜索，移除与value相等的元素，数量为count。
count=0 移除表中所有value相等的值。

#保留指定范围内的元素
ltrim key start stop
应用场景：保留微博评论最后500条
ltrim weibo:comment 0 499

#改
lset key index newvalue
```

# Redis与Python交互

## 安装

```shell
# ubuntu
sudo pip3 install redis

windows
1. python -m pip install redis
2. pip install redis
```

## 使用流程

```python
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
```

通用命令代码——> redis_test

# 位图操作

## 定义：

1. 位图不是真正的数据类型，它是定义在字符串类型中
2. 一个字符串类型的值最多能存储512m字节的内容，位上限：2^32

   1MB = 1024KB
   1KB = 1024B
   1B=8bit

## 强势点

可以实时的进行统计，机器节省空间。官方模拟一亿二千八百万用户的模拟环境中，使用macbookpro，典型统计如“日用户数”的时间消耗小于50ms，占用内存16MB

```shell
#设置某一位上的值,(offset是偏移量，从0开始)
setbit key offset value


#获取某一位上的值
getbit key offset

#统计键所对应的值有多少个1
bitcount key
```

## 应用场景

1. 用户签到
2. 统计用户活跃度
3. 统计用户活跃天数
4. 统计用户活跃小时数
5. 统计用户活跃分钟数
6. 网站用户的上线次数统计







