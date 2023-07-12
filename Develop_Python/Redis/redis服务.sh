# redis服务启动两种方式启动和关闭
# 命令行启动，关闭终端，服务立即关闭
redis-server /usr/local/etc/redis.conf
# brew后台启动
brew services start redis

# 关闭redis服务
redis-cli shutdown
brew services stop redis

# 强行终止redis
sudo pkill redis-server

# 查看进程
ps aux | grep redis

# redis-cli 连接redis服务
redis-cli -h 127.0.0.1 -p 6379
# 启动客户端，打开终端命令输入 redis-cli 该命令会链接本地的redis服务。
redis-cli

# 修改配置
1. 在usr/local/ect/redis.conf中直接修改配置文件
2. 使用config set 命令进行修改

# redis数据类型：
字符串、哈希、列表、集合、有序集合

# redis常用命令
# 连接本地服务
redis-cli  #有时候会中文乱码 则使用redis-cli --raw

# 远程服务链接指令
redis-cli -h host -p port -a password












