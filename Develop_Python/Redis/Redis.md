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
  
## 字符串常用命令
```shell
set key value
get key
#key不存在时再进行设置
set key value nx
#设置过期时间(ex)
set key value ex seconds


```

## string值取值原则
- key值不宜过长，消耗内存，且在数据中查找这类键值的计算成本高
- 不宜过短，可读性较差
- 一个字符串类型的值最多能存储512m内容。




