# 一、Redis启动与关闭

## 启动

1. 命令行启动，关闭终端，服务立即关闭

```shell
redis-server /usr/local/etc/redis.conf
```

2. 后台启动

```shell
#mac电脑后台
brew services start redis

#ubuntu后台启动
方法1：
redis根目录下，执行./redis-server &
#&使redis以后台程序方式运行

方法二
1. 配置文件将daemonize设置为yes
2. 启动 redis-server /xxx/xxx/xxx/redis.conf
3. 检查redis是否在后台启动
ps -ef | grep redis
```

## 关闭

```shell
#前台
ctrl+c
#后台
kill+pid
#推荐
redis-cli shutdown
#mac电脑
brew services stop redis
# 强行终止redis
sudo pkill redis-server
```


# 二、连接

1. 远程连接——redis-cli

```shell
redis-cli -h host -p port -a password
redis-cli -h 127.0.0.1 -p 6379
```

2. 本地连接

```shell
# 连接本地服务,有时候会中文乱码 则使用redis-cli --raw
redis-cli --raw
```


# 三、常用其他配置

```shell
# 修改配置
#配置文件路径：/etc/redis/redis.conf

#配置密码
requirepass 密码

#配置远程连接
1. bind 127.0.0.1 改为 bind 0.0.0.0 或者直接注释掉
2. 关闭保护模式，即 protected-mode no
3. 允许后台运行，即 daemonize yes


# 获取redis安装目录
config get dir

# 创建当前数据库的备份
save #改命令将在redis安装目录中创建dump.rdb文件
# 创建redis备份也可以使用bgsave,该命令在后台执行。
# 恢复数据，只需要将备份文件移动到redis安装目录并启动服务即可。

# 查看是否设置密码
config get requirepass

# 修改配置设置密码
config set requirepass "password"

# 查看redis客户端最大连接数
config get maxclients

# 设置客户端最大连接数,在服务启动时设置
redis-server --maxclients 100000

#rdb持久化-默认配置
dbfilename 'dump.rdb'
dir /var/lib/redis

rdb持久化-自动触发（条件）
save 900 1
save 300 10
save 60 10000   #时间+修改次数

#aof持久化-自动触发（条件）
appendonly yes
appendfilename 'appendonly.aof'
#aof持久化策略
appendfsync always
appendfsync everysec #默认
appendfsync no 
#aof重写触发
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

#设置为从服务器
salveof <master-ip> <master-port>
```

# Redis相关文件存放路径(Ubuntu)
1. 配置文件： /etc/redis/redis.conf
2. 备份文件： /var/lib/redis/*.rdb|*.aof
3. 日志文件： /var/log/redis/redis-server.log
4. 启动文件： /etc/init.d/redis-server
/etc/下存放配置文件
/etc/init.d/下存放服务启动文件




















