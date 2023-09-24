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
# 五、raid raid1 raid5的区别
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
df -h | head -4 | tail -1 | awk 'print{ $5}' | swk -F '%' '{print $1}'

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
[a-Z0-9所有字母和数字]

#Mac地址正则匹配
#06:da:6e:79:fa:91 
([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}

# 找出mac地址的匹配表达式
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

九、Shell编程

```shell
1. xxx.sh
2. 正文第一行必须指定解释器: #!/bin/bash
```

## 执行方式
```shell
#方式一、加权限 ./xxx.sh执行
1. chmod +x xxx.sh
2. ./xxx.sh

#方式二手动指定解释器
bash xxx.sh
```

## 变量
**自定义变量**
```shell
# 1. 定义变量
变量名=值 -----> 注意：=两侧不能有空格
name="take me to your heart"

#2. 调用变量的格式
echo $变量名

#3. 小细节：单引号和双引号的区别
单引号：无法获取变量的值
双引号：可以获取变量的值
```
**环境变量+位置变量+预设变量**

```shell
#环境变量
echo $USER #当前用户
echo $UID  #当前用户的UID
echo $PWD  #当前路径
echp $PATH #命令搜索路径

#位置变量
$1 $2 $3 .....shell的位置变量

#预定义变量
$# $* $?
# $#返回位置变量的数量
# $?返回的位置变量的所有的值
# $?:返回上一条命令执行的状态(0代表正确，非0代表失败)


#示例，输出$1+$2,例如输出3+5
#!/bin/bash
echo $1+$2
echo `expr $1 + $2` #输出加法的运算结果

```

**变量赋值**
```shell
# 语法格式
read -p 提示信息 变量名
read -t n #设置时间超出时间自行往下执行

#示例
#!/bin/bash
read -p 请输入姓名： name
echo "您输入的姓名是：$name"

#练习
#!/bin/bash
read -p "请输入您的姓名:" name
read -t 3 -p "请输入成绩:" score
echo "$name的成绩是$score分"
```

**Shell-算术运算符**  

```shell
#运算符
1、 + - * / %
2、 ++：自加运算，类似于python 中i++ 等同于i+1
3、 --:同++

#运算命令
1、let运算表达式
 i=1
 let i++
 echo $i
 
2、expr运算表达式
i=1
sum=`expr $i + 5` #两侧要有空格
echo $sum

3、$[]
echo $[1+1]
echo $[1-1]
echo $[a+a] #调用变量不用多次添加$符号
echo $[1*1] # 乘法无需转义
```

**比较运算符**  
```shell
#语法格式
[判断语句] #注意括号必须有空格

#1、字符比较
[ A == A ] #相等(等号两边需要有空格)
[ A != B ] #不相等
[ -z $变量 ] #判断是否为空

#2、数字比较
-eq 等于 equal
-ne 不等于 not equal
-gt 大于 greater than
-ge 大于等于 greater or equal
-lt 小于 less than 
-le 小于等于 less or equal

#3、文件|目录比较
[ -e 文件或目录 ] 是否存在exist
[ -f 文件 ] 存在且为文件file
[ -d 目录 ] 存在且为目录directory
[ -r 文件或目录 ] 判断是否可读
[ -w 文件或目录 ] 判断是否可写
[ -x 文件或目录 ] 判断是否可执行
```

**Shell-if分支**
```shell
# 1. 单分支语法格式
if 判断 ;then
  命令
  命令
fi

#2. 双分支语法格式
if 判断 ; then
  命令1
else
  命令2
fi 

#3. 多分支语法格式
if 判断 ;then
  命令1
elif 判断 ;then
else
  命令3
fi

#示例

if [ ]
```

**Shell-for循环**
```shell
#语法格式
for 变量 in 值序列
do
  命令
done

#示例
for i in 1 2 3 4 5
do
  echo "hello world"
done 

#示例
#!/bin/bash
#seq造数 seq 起始值 步长 终值
for i in `seq 1 3 20`
do
        echo "hello world"
        echo $i
done

#练习 判断指定网段的IP地址哪些可用，哪些不能用
#!/bin/bash



for i in {2..254}
do
        #/dev/null 为黑洞,不想要的输出放到里面
        ping -c 2 10.24.25.$i &> /dev/null
        #$?返回上一条命令的执行状态
        if [ $? -eq 0 ];then
                echo "10.24.25.$i可用"

        else
                echo "10.24.25.$i不可用"

        fi

done
```

**Shell-while循环**  
```shell
#语法格式
while 条件判断
do
  命令
done


#示例
#!/bin/bash
i=1
while [ $i -le 5 ]
do
        echo $i
        #自加1
        let i++
done

#!/bin/bash

c=$[RANDOM%10000]

while :
do
        read -p "数字已想好,请猜:" you

        if [ $you -gt $c ];then
                echo "猜大了"
        elif [ $you -lt $c ];then
                echo "猜小了"
        else
                echo "猜对了"
                exit
        fi
done
```

**Shell-case分支结构**  

```shell
#1. 特点
根据变量值的不同，执行不同的操作

#2.语法格式

case  in 
模式1)
  代码块
  ;;
模式2)
  代码块
  ;;
*）
  代码块
  ;;
esac

#示例
#!/bin/bash
echo "+------------------------------+"
echo "|     Welcome(q to quit)       |"
read -p "请输入1个字符:" char
if [ ${#char} -ne 1 ]; then
        echo "$char不是一个字符"
        exit
elif [ $char == "q" ]; then
        echo "程序退出"
        exit
fi
case $char in
[a-z]|[A-Z])
        echo "字母"
        ;;
[0-9])
        echo "数字"
        ;;
*)
        echo "其他字符"
        ;;
esac


#示例nginx启动停止重启脚本
#!/bin/bash
read -p "请选择操作(stop|start|restart):" operation

case $operation in
"start")
        /etc/init.d/nginx start
        ;;
"stop")
        /etc/init.d/nginx stop
        ;;
"restart")
        /etc/init.d/nginx restart
        ;;
*)
        echo "Usage: nginx {start|stop|restart}"
        ;;
esac
```

## 知识点总结
```shell
#1. 获取字符串长度
${#变量名}

#2. 字符串切片
${string:index:number}
key='ABCDE'
${key:0:1} #A 获取下表索引为0的因素
${key:1:2} #BC

#3. vim批量缩进
1. 进入命令行模式 shift + :
2. 1,3> Enter # 1-3行缩进
3. 1,3< Enter #1-3行回缩进
```

## Shell 实战

**1.每两秒检测一次Mysql数据库的连接数量**

```shell
#mysqladmin
mysql服务器管理任务的工具，他可以检查mysql服务器的配置和当前工作状态

#代码实现
#!/bin/bash
user="root"
passwd="123456"
while :
do
        count=`mysqladmin -u$user -p$passwd status | awk '{print$4}'`
        echo "`date +%H%M%S`" 并发连接数为: $count
        sleep 2

done
```
**2.根据md5校验码，检测文件是否被修改**
```shell
#1. 生成md5的文件校验码,命令如下
md5sum filename

#2. 将/etc目录下的所有的.conf文件生成校验码 shell如下，校验码写入到r1.txt中
#!/bin/bash
for file in $(ls /etc/*.conf)
do
        md5sum $file >> /test/r1.txt
done

#3. 修改/etc/test.conf
#4. 再次将/ect目录下的文件生成校验码，写入到r2.txt

#5.查看两个文件的不同
diff r1.txt r2.txt
#结果
# 1. test.conf发生了变化
#2. 第25行发生了变化(change)
25c25
< 6ee424a3d5e3891e425a0459fd61c870  /etc/test.conf
---
> 7c4555df960371a6a845e7dd05ff439e  /etc/test.conf
```

**3.备份MySQL数据库**

```shell
#!/bin/bash
user='root'
passwd='123456'
dbname='mysql'
filename=$(date +%F)_mysql.sql
#1. 创建目录
if [ ! -d "/home/kql/back" ];then
        mkdir -p /home/kql/back
fi
#2.备份
mysqldump -u$user -p$passwd $dbname > /home/kql/back/$filename
```
**4.随机生成8位密码-数字-字母-下划线**

```shell
#设置变量为key，存储密码的所有可能性（密码库），如果还有需要其他字符请自行添加其他密码字符
#使用$#统计密码库的长度
#!/bin/bash
key="_0987654321qwertyuioplkhgfdsazxcvbnmZXCVBNMLKJHGFDSAQWERTYUIOP"
length=${#key}
for i in {1..8}
do
        index=$[RANDOM%length]
        pass=$pass${key:$index:1}
done
echo $pass
```
**随机密码生成-python**
```python
import string
import random

key = string.ascii_letters + string.digits + '_'
passwd = ''

for i in range(8):
    one = random.choice(key)
    passwd += one
print(passwd)
```

**Shell函数**
```shell
#1. 语法格式
函数名(){
  
}
#2. 调用
函数名

#示例，使用函数进行算术的加减运算
#!/bin/bash
sumn(){
        echo $[n1 + n2]
}
subn(){
        echo $[n1 - n2]
}
read -p "First:" n1
read -p "Second:" n2
read -p "Operation(+|-):" op
case $op in
"+")
        sumn
        ;;
"-")
        subn
        ;;
*)
        echo "Invalid"
        ;;
esac
```