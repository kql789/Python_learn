# Shell编程

- [Shell编程](#shell编程)
  - [一、语法格式](#一语法格式)
  - [二、执行方式](#二执行方式)
  - [三、变量](#三变量)
    - [**1. 自定义变量**](#1-自定义变量)
    - [**2. 环境变量+位置变量+预设变量**](#2-环境变量位置变量预设变量)
    - [**3. 变量赋值**](#3-变量赋值)
  - [算术运算符](#算术运算符)
  - [四、比较运算符](#四比较运算符)
  - [五、Shell-if分支](#五shell-if分支)
  - [六、Shell-for循环](#六shell-for循环)
  - [七、Shell-while循环](#七shell-while循环)
  - [八、Shell-case分支结构](#八shell-case分支结构)
  - [九、Shell函数](#九shell函数)
  - [十、知识点总结](#十知识点总结)
  - [十一、Shell 实战](#十一shell-实战)
    - [1. 检测数据连接数量](#1-检测数据连接数量)
    - [2. md5文件校验](#2-md5文件校验)
    - [3. 数据库备份](#3-数据库备份)
    - [4. 随机密码生成-Shell](#4-随机密码生成-shell)
    - [5. 随机密码生成-Python](#5-随机密码生成-python)

## 一、语法格式

```shell
1. xxx.sh
2. 正文第一行必须指定解释器: #!/bin/bash
```

## 二、执行方式
```shell
#方式一、加权限 ./xxx.sh执行
1. chmod +x xxx.sh
2. ./xxx.sh

#方式二手动指定解释器
bash xxx.sh
```

## 三、变量
### **1. 自定义变量**
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
### **2. 环境变量+位置变量+预设变量**

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

### **3. 变量赋值**
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

## 算术运算符  

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

## 四、比较运算符  
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

## 五、Shell-if分支
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

## 六、Shell-for循环
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

## 七、Shell-while循环 
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

## 八、Shell-case分支结构  

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

## 九、Shell函数
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

## 十、知识点总结
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

## 十一、Shell 实战
### 1. 检测数据连接数量
**说明：每两秒检测一次Mysql数据库的连接数量**

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
### 2. md5文件校验
**说明：根据md5校验码，检测文件是否被修改**
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
### 3. 数据库备份
**说明：备份MySQL数据库**

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
### 4. 随机密码生成-Shell
**说明：随机生成8位密码-数字-字母-下划线**

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
### 5. 随机密码生成-Python
**说明：使用Python相关模块，随机密码生成-python**
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

