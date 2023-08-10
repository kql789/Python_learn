# Author :   Kql_unicorn
# Date   :   2023/8/10 21:00
"""
event线程互斥方法演示
"""
from threading import Thread, Event

# 用于通信
s = None
e = Event()  # 事件对象


def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()  # 操作完共享资源 e设置


t = Thread(target=杨子荣)
t.start()
e.wait()  # 阻塞状态
print("说对口令就是自己人")
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他")

t.join()
