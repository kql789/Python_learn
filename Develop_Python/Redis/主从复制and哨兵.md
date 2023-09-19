# Redis主从复制
- 定义  
1. 一个redis服务可以有多个该服务的复制品，这个redis服务成为master，其他复制品成为slaves
2. master会一直讲自己的数据更新同步给slaves，保持主从同步。
3. 只有master可以执行命令，slave只能执行读命令。

- 作用  

    
    分担了读的压力（高并发）

- 原理  


    从服务器执行客户端发送的读命令，比如get、lrange、smemmers、hget、zrange等等，客户端可以连接slaves  
    执行读请求。

- 两种实现方式

**方式一(Linux命令行实现)**

        方法1
        #从服务端
        redis-server --slaveof <master-ip> <master-port>
        # 将6300服务端得redis作为6379的从服务
        redis-server --port 6300 --slaveof 127.0.0.1 6379

**方式一(redis命令行实现)**

        #在从服务端设置
        slaveof ip port
        slaveof no one  #取消设置


**方式二(修改配置文件)**
1. 进入从服务器的redis配置文件，/etc/redis/redis.conf
2. 设置为主服务器的从服务，
slaveof 127.0.0.1 6379 #为127.0.0.1的从服务
3. 启动从服务器。

**问题总结**
1. 一个master可以有多个slaves
2. slave下线，只是读请求的处理性能下降
3. master下线，写请求无法执行
4. 其中一台slave使用slaveof no one 命令成为master，其他slaves执行slaveof命令指向
这个信的master，从它这里同步数据
注意：以上过程是手动的，能够实现自动，这就需要sentinel哨兵，实现故障转移failover操作。


# 高可用方案

**Redis之哨兵**  

      1. Sentinel会不断检查Master和slaves是否正常
      2. 每一个Sentinel可以监控任意多个Master和该Master下的slaves


## 环境搭建

      1. 共3台服务器，6379为主，6380和6381为从 (在同一台机子上测试)
      2. 启动主服务器 redis-server (6379主) 
      3. redis-server --port 6380 
      4. redis-server --port 6381
      5. 分别在两台从服务器上 绑定主服务器 slaveof ip port 

## 安装并搭建sentinel哨兵
         
      1. 安装redis-sentinel
      sudo apt install redis-sentinel
      2. 新建配置文件sentinel.conf
      port 26379
      # tedu 监控的服务名字，自定义；1，为投票机制
      Sentinel monitor tedu 127.0.0.1 6379 1

      3. 启动sentinel
      方式一： redis-sentinel sentinel.conf
      方式二： redis-server sentinel.conf --sentinel

      4. 将master的redis服务终止，查看是否会提升为主
      sudo /etc/init.d/redis-server stop 
      发现提升6381为master，依然两个为从
      在6381上设置新值，6380查看
      127.0.0.1:6381>set name tedu
      OK

      #启动6379 观察日志，发现变为了6381的从
      主从+哨兵基本就够用了

sentinel.conf 解释
```shell
#sentinel 监听端口，默认是26379，可以修改
port 26379
#告诉sentinel去监听地址为ip:port的一个master，这里面的master-name可以自定义，quorum是一个数字，指明当有多少个sentinel认为一个master时效时，
master才算真正失效
sentinel moniitor <master-name> <ip> <redis-port> <quorum>

```

# 生产环境中设置哨兵sentinel

```shell
1. 安装sentinel
sudo apt-get install redis-sentinel
2. 创建配置文件 sentinel.conf
3. 启动sentinel开始监控
redis-sentinel sentinel.conf
```
        
