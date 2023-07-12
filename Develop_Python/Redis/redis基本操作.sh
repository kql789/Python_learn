get key
set key value
del key

Redis hash 是一个键值(key=>value)对集合。

Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象
# 哈希的创建和获取
创建 hmset index field1 value1 field2 value2
获取 hget index field1

# 列表的创建
lpush index value
# 获取，按照索引获取
lrange index start_index end_index

# 集合的创建
# redis的set是string类型的无序集合，集合都是通过
# 哈希表实现的，所以添加、删除、查找的复杂度都是O1,
# 添加成功返回1，不成功返回0,
# 集合内部元素必须保证唯一性，即插入两个两个相同的元素，
# 集合内部只会显示一次
# 添加
sadd name value
# 查看
smembers name

# 有序集合
# zset 和set一样也是string类型元素的集合，且不允许
# 重复的成员。
# 不同的是每个元素都会关联一个double类型的分数，redis正式通过分数来为集合的成员
# 进行从小到大的排序。zset的成员是唯一的，但分数却可以重复。
# 添加
zadd key score value
# 例如：
zadd dxc 0 mysql
# 查询数据
zrangebyscore dxc 0 10


# 列表的增加
lpush runoobkey redis
lpush runoobkey musql
lpush runoobkey sqlserver
lpush runoobkey sqllite

#根据索引范围查看值
lrange runoobkey 0 10

#根据索引查看对应的值
lindex runoobkey 0
lindex runoobkey -1

#求列表的长度
llen runoobkey

lindex runoobkey 0
#移除并获取列表的第一个元素值
lpop runoobkey

#将一个值或多个值插入列表头部
lpush runoobkey kql tiechui beijing shanghai

#将一个值插入到已经存在的列表头部
lpush runoobkey xiaoming
lindex runoobkey 0

# 获取指定范围内的元素
lrange runoobkey 0 3

#移除列表元素值
lrem runoobkey 0 "xiaoming"
lrange runoobkey 0 1

#通过索引值设置列表元素的值
lset runoobkey 0 "blue"
lrange runoobkey 0 1

#对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的#元素都将被删除。
lrange runoobkey 0 -1
ltrim runoobkey 1 5
lrange runoobkey 0 -1

#移除列表的最后一个元素，返回值为移除的元素。
rpop runoobkey
lrange runoobkey 0 -1

#在列表中添加一个或多个值到列表尾部
lrange runoobkey 0 -1
rpush runoobkey "yellow" "black" "green"

#为已存在的列表添加值
rpushx runoobkey "bbb"
_________________________________________________________
##集合相关操作
#向集合添加一个或多个成员
sadd set1 redis mongodb mysql sqlserver sqllite
sadd set1 yellow

#查看所有元素
smembers set1

#获取集合的成员数
scard set1

#返回第一个集合与其他集合之间的差异。
sdiff set1

#返回给定所有集合的交集
sinter set1

#判断 member 元素是否是集合 key 的成员 0:否 1:是
sismember set1 redis

#返回集合中的所有成员
smembers set1
smembers dset

#将 yellow 元素从 set1 集合移动到 dset 集合
smove set1 dset yellow

#移除并返回集合中的一个随机元素
spop dset

#返回集合中一个或多个随机数
srandmember set1 2

#移除集合中一个或多个成员
srem set1 mysql
smembers set1

#返回所有给定集合的并集
sunion set1 dset

#所有给定集合的并集存储在 destination 集合中
sunionstore destination set1 dset

#迭代集合中的元素
sscan set1 10

sscan set1 0 match r*


##redis有序集合
#向有序集合添加一个或多个成员，或者更新已存在成员的分数
zadd bset 1 mysql
zadd bset 2 redis
zadd bset 3 sqllite
zadd bset 4 aaa
zadd bset 5 bbb
zadd bset 6 ccc

zrange bset 0 10 withscores

#获取有序集合的成员数
zcard bset

#计算在有序集合中指定区间分数的成员数
zcount bset 1 2

#在有序集合中计算指定字典区间内成员数量
zlexcount key min max

#通过索引区间返回有序集合指定区间内的成员
zrange bset 0 2

#通过字典区间返回有序集合的成员
zrangebylex key min max

#通过分数返回有序集合指定区间内的成员
zrangebyscore bset 1 2

#返回有序集合中指定成员的索引
zrank bset "redis"

#移除有序集合中的一个或多个成员
zrem bset redis
zrange bset 0 10 withscores

#移除有序集合中给定的排名区间的所有成员
zremrangebyscore bset 1 3

#返回有序集中指定区间内的成员，通过索引，分数从高到低
zrevrange bset 0 5 withscores

#返回有序集中指定分数区间内的成员，分数从高到低排序
zrevrangebyscore bset 10 0 withscores

#返回有序集合中指定成员的排名，有序集成员按分数值递减(从大到小)排序
zrevrank bset aaa

#返回有序集中，成员的分数值
zscore bset bbb

#计算给定的一个或多个有序集的并集，并存储在新的 key 中
zunionstore bset dxc cvb[key]

#迭代有序集合中的元素（包括元素成员和元素分值）
zscan dxc 0

# Redis数据备份与恢复
# 获取redis安装目录
config get dir
# 创建当前数据库的备份
save  #改命令将在redis安装目录中创建dump.rdb文件
# 创建redis备份我呢间也可以使用bgsave,该命令在后台执行。
# 恢复数据，只需要将备份文件移动到redis安装目录并启动服务即可。

# 查看是否设置密码
config get requirepass
# 修改配置设置密码
config set requirepass "password"
# 查看redis客户端最大连接数
config get maxclients
# 设置客户端最大连接数,在服务启动时设置
redis-server --maxclients 100000

