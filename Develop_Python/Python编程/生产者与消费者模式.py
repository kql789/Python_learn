# @Author : Kql
# @Time : 2023/6/8 17:53
import threading
import time
import queue

'''
利用多线程和队列可以实现生产者消费者模式。该模式通过平衡生产线程和消费线程的工作能力来提高程序整体处理数据的速度。

什么是生产者和消费者？

在线程世界里，生产者就是生产数据（或者说发布任务）的线程，消费者就是消费数据（或者说处理任务）的线程。在任务执行过程中，
如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，
如果消费者的处理能力大于生产者，那么消费者就必须等待生产者提供更多的任务，本质上，这是一种供需不平衡的表现。
为了解决这个问题，我们创造了生产者和消费者模式。

生产者消费者模式的工作机制：

生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，
而是通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不直接找生产者要数据，
而是从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力，解耦了生产者和消费者。
生产者消费者模式的核心是‘阻塞队列’也称消息队列。在生产环境中有很多大名鼎鼎的分布式消息队列，
例如RabbitMQ，RocketMq，Kafka等等。在学习过程中，我们没必要使用这么大型的队列，
直接使用Python内置的queue模块中提供的队列就可以了。
'''
'''下面是一个利用threading和queue模块，模拟一个简单的厨师做包子，顾客吃包子的例子，是生产者消费者模式的典型例子。'''

q = queue.Queue(10)  # 生成一个队列，用来保存“包子”，最大数量为10


def prodeucer(i):
    # 厨师不停的没2秒做一个包子
    while True:
        q.put("厨师%s做的包子" % i)
        time.sleep(2)


def consumer(j):
    # 顾客每秒吃一个包子
    while True:
        print("顾客%s吃了一个%s" % (j, q.get()))
        time.sleep(1)


# 实例化3个生产者 （厨师）
for i in range(3):
    t = threading.Thread(target=prodeucer, args=(i,))
    t.start()
# 实例化了10个消费者（顾客）
for j in range(10):
    v = threading.Thread(target=consumer, args=(j,))
    v.start()
