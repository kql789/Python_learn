# Author :   Kql_unicorn
# Date   :   2023/7/30 22:17
import os
from time import sleep

a = 1
# 创建子进程
pid = os.fork()
# 返回小于0的值表示创建子进程失败
if pid < 0:
    print("Error")
# 子进程执行部分
elif pid == 0:
    print("Create new proocess")
    print("a= ", a)
    a = 10000
# 父进程执行部分
else:
    sleep(1)
    print("The old precess")
    print("a:", a)
# 父子进程都会执行
print("Fork test over")
