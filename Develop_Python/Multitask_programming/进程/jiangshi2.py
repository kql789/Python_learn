# Author :   Kql_unicorn
# Date   :   2023/7/31 21:56
"""
信号处理僵尸进程
"""
import os, sys
import signal

# 子进程退出时父进程忽略退出行为，子进程交系统处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()
if pid == 0:
    print("Child PID", os.getpid())
    sys.exit()
else:
    while True:
        pass
