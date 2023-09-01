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




