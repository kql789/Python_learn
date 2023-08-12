# Author :   Kql_unicorn
# Date   :   2023/8/10 22:41
"""
分别复制文件的上半部分和下半部分到一个新的文件中
"""

from multiprocessing import Process
import os

filename = "./photo/io操作.jpg"

size = os.path.getsize(filename)

# 父进程创建fr    两个子进程使用这个fr会互相影响
# fr = open(filename, 'rb')


# 复制上半部分
def top():
    fr = open(filename, 'rb')
    fw = open('./photo/top.jpg', 'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()


# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open('./photo/bot.jpg', 'wb')
    fr.seek(size // 2, 0)  # 文件偏移量，以0字节位置为参考，偏移至一半的位置
    fw.write(fr.read())
    fr.close()
    fw.close()


if __name__ == '__main__':
    p1 = Process(target=top)
    p2 = Process(target=bot)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
