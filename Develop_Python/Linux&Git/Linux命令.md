# 一、默认熟悉命令
```shell
pwd
cd    --cd .. 
ls   -l  -- ll
mkdir -p #(递归创建) /home/tae
#python_os 
#os.mkdir('')
#os.mkdirs('') #递归创建

touch
tar
#压缩
tar -zcvf xxx.tar.gz dir1 dir2
#解压
tar -zxvf xxx.tar.gz 
tar -xf xxx.tar.gz
 
cp   --cp -r #r 选项递归复制，复制非空文件夹
mv 
#剪切
mv dir1 /home/etc
#重命名
mv dir1 new_dir1
```
# 二、常用命令

```shell
# 查看ip地址和mac地址，windows中命令ipconfig 或者ipconfig/all
ifconfig
#ubunutu18.04 不能使用ifconfig
sudo apt-get install net-tools

#测试网络连通性/域名 [-c n]
ping IP/域名 [-c n] 

#解析域名对应的IP地址
nslookup 域名

#显示文件权限及详细信息
ls -lh file|directory

-rw-r--r--  1 user  staff 
#分三组：所有者权限 所属组用户权限 其他用户权限
r -读(4)
w -写(2)
x -可执行(1)
前3位：所有者(user这个用户) rw-
中3位：所属组其他用户(用户staff对文件权限) r--
后3位：其他组其他用户(用户develop1对文件权限) r--
#777 rwxrwxrwx
#666 rw-rw-rw-
#744 rwxr--r--

#将文件|目录打包并压缩
tar -zcvf filename.tar.gz file1 file2

#解压缩，默认解压到当前路径 -C可指定路径
tar -zxvf filename.tar.gz [-C path]

#显示进程命令（包含PID号） ps -aux | grep 'mysql'
ps -aux

#杀死某个进程
kill PID

# 给文件指定或者增加某权限
chmod 权限 file
chmod 777 文件名
rw-r--r--
chmod u+x 文件名 #给文件所有者增加x权限(user)
chmod g+w 文件名 #同组其他用户增加w权限(group)
chmod o-r 文件名 #其他组其他用户减r权限(other)
chmod a+x 文件名 #给所有用户增加x权限(all)

#更改属主和属组
chown root:root file #所有者和所属组+文件名

# 在某个路径下查找文件
find path -name filemname

# 远程连接到服务器
ssh user@172.40.91.138

# 本地文件复制到远程
scp file user@IP:绝对路径
scp python.tar.gz user@172.40.91.138:/home/user/
``` 

# 三、vi及vim使用

```shell
#文本编辑器，vim是vi的升级版
1. vi filename
浏览模式
插入模式 a/i/u
命令行模式 shift+:
wq!保存退出
q!不保存退出

2. 查找
浏览模式->输入/ ——> 输入查找内容 ——>enter
n表示查找下一个，shift+n表示上一个

3. 复制+删除+粘贴+撤销
yy 复制光标所在行(2yy复制两行)
p  粘贴
dd 删除(剪切)光标所在行(3dd删除3行内容）
u  撤销 

4. 光标跳转(浏览模式)
行首 home
行尾 end
全文的首行 gg 或者 :1
全文的最后一行 G 或者 :$
全文的12行 12G
5. 批量缩进
显示行号 命令行模式下输入 :set nu
命令行模式下
1,3> 敲Enter -向右缩进
3,8< 敲Enter -向左缩进
```
# 四、Goon命令
```shell
#1. 显示一个文件的前5行
head -5 test.txt
#2. 显示一个文件的后3行
tail -3 test.txt

#3. 管道操作
#将前面命令的输出，传递给后面命令，作为后面命令的参数
#查看/etc/passwd 文件的第6-10行?
cat /etc/passwd | head -10 |tail -5

# 4.统计目录总共占用空间的大小
du -sh 目录

#5.查看磁盘使用情况 (根分区使用情况)
df -h

#6. 常见通配符使用
* :任意多个字符
? :单个字符

rm -rf /home/user/test/*
ls *.jpg

# 7. 重定向：将前面命令的输出，写入到文本文件中
>:覆盖重定向
>>:追加重定向

# 8.创建用户
useradd username

# 9. 设置密码
sudo passwd 用户名

# 10. 删除用户
userdel
# -r:递归删除，删除用户的家目录以及用户的邮件文件

#11.统计文件行数
wc -l filename_path

#12.对文件内容进行排序
sort filename

#13.取出重复行，并统计每行出现的次数（相邻行）
uniq -c
sort filename | uniq -c
```
# 五、raid0 raid1 raid5的区别
什么时候开始设置的？是在做虚拟化的之前。
## 什么是raid？
由一系列硬盘组成的阵列，简单说，一个服务器有10个—硬盘，你如何能保证坏掉一个硬盘后数据不丢，业务不断。

## raid0,raid1,raid5 
raid0  
1. 特点：数据分散存储在多个硬盘
2. 优点：读写并发，速度超快，提升数倍。
3. 缺点：一但一个硬盘挂掉，则损坏全部数据。

raid1  
1. 特点：数据分别写入两个磁盘（写了两份）。
2. 优点：实现了数据备份。
3. 缺点：磁盘使用率只能到50%

raid5  
1. 特点：提供热备盘实现故障恢复
2. 优点：只损坏1块磁盘，数据不会损坏。
3. 缺点：同时损坏2块磁盘，数据损坏。

# 六、周期性计划任务

## 1. 进入周期性计划任务
crontab -e (首次进入按2 - 找vim)
## 设置周期性计划任务
```shell
# * * * * *:五个*号代表 分 时 日 月 周
分：0-59
时：0-23
日：1-31
月：1-12
周：0-6

# 开始设置
'*' 代表所有可能值
',' 代表多个时间点 0 1,5 * * * xxx
'/' 指定时间间隔频率 0 0-6/1 * * *
'-' 指定一个时间段

#示例
每月的1日和5日两天 * * 1,5 * *
每10分钟  */10 * * * * 
0点-6点每小时执行 0 0-6/1 * * *
每分钟 * * * * * 
```
# 七、文本处理工具
**语法格式**  
```shell
awk 选项 '动作' 文件列表
```
**常用方式**  
```shell
linux命令 | awk 选项 '动作'

# 示例，提取分区的使用量
df -h | head -4 | tail -1 | awk '{print $5}' | awk -F '%' '{print $1}'

# 输出本机IP
ifconfig | head -2 | tail -1 | awk '{print $2}'

# nginx 的访问日志 输出ip
cat access.log | awk '{print $1}' | sort | uniq 

# nginx 的访问日志 输出ip 统计多少个ip访问过我
cat access.log | awk '{print $1}' | sort | uniq | wc -l
# 统计每个ip的访问次数，输出3
# 前10个访问量最大的用户IP
cat access.log | awk '{print $1}' | sort | uniq -c | sort -rnk 1 | head -10
```
**grep命令之正则表达式**  

```shell
# 正则表达式元字符集 ——使用grep命令
^ 以....开头
$ 以....结尾
. 任何1个字符
* 0次和多次
# 正则表达式扩展字符集使用egrep命令
+ 1次或多次
{n} 出现n次
() 分组

[a-z] 所有小写字母
[A-Z] 所有大写字母
[a-Z] 所有字母
[0-9] 所有数字
[a-Z0-9] 所有字母和数字

#Mac地址正则匹配
#06:da:6e:79:fa:91 
([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}

# 找出mac地址的匹配所有字母和数字表达式
ifconfig | egrep "([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}" | awk '{print $2}' 
```
# 八、常见服务端口
```shell
MYSQL 80
MongDB 27017
Redis 6379
Redis-sentinel 26379
SSH 22
HTTP 80
Nginx 80
HTTPS 443
TELNET 23
FTP 21
```

