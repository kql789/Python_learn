# 进程间通信(IPC)

1. 必要性：进程间空间独立，资源不共享，此时在需要进程间数据传输时就需要特定的手段进行数据通信。
2. 常用进程间通信方法

        管道、消息队列、共享内存、信号、信号量、套接字

## 管道通信(Pipe)

1. 通信原理  
   在内存中开辟管道空间，生成管道操作对象，多个进程使用同一个管道对象进行读写即可实现通信。

2. 实现方法

        from multiprocessing import Pipe
        fd1,fd2 = Pipe(duplex=True)
        功能：创建管道
        参数：默认表示双向管道，若为False表示单向管道
        返回值：表示管道两端的读写对象
         如果是单向管道，fd1只读，fd2只写
         如果是双向管道，两端均可读写。



         fd.recv()
         功能：从管道获取内容
         返回值：获取到数据
         
         fd.send(data)
         功能：向管道写入内容
         参数：要写入的数据

## 消息队列

1. 通信原理 在内存中建立队列模型，进程通过队列将消息存入，或者从队列取出完成进程间通信。

2. 实现方法

         from multiprocessing import Queue
         q = Queue(maxsize=0)
         功能：创建队列对象
         参数：最多存放消息个数
         返回值：队列对象
         

         q.put(data,[block,timeout])
         功能：向队列存入消息
         参数：data,要存入的内容
         block 设置是否则色 False 为非阻塞
         timeout 超时检测

         q.get([block,timeout])
         功能：从队列取出消息
         参数：block 设置是否阻塞 False为非阻塞
         timeout:超时检测
         返回值：返回获取到的内容

         q.full()判断队列是否为满
         q.empty() 判断队列是否为空
         q.qsize() 获取队列中消息个数
         q.close() 关闭队列

## 共享内存

1. 通信原理： 在内存中开辟一块空间，进程可以写入内容和读取内容完成通信，但是每次写入内容会覆盖之前内容。

2. 实现方法

         from multiprocessing import Value,Array
         obj = Value(ctype,data)
         功能：开辟共享内存
         参数：ctype 表示共享内存空间类型 'i','f','c'
         data 共享内存空间初始数据
         返回值：共享内存对象
         obj.value 对该属性的修改查看即对共享内存读写。

         obj = Array(ctype,data)
         功能： 开辟共享内存空间
         参数：ctype 表示共享内存数据类型
               data 整数则表示开辟空间的大小，其他数据类型表示开辟空间
         返回值：共享内存对象

         Array共享内存读写，通过遍历obj可以得到每个值，直接可以通过索引进行访问和修改
         可以使用obj.value 直接打印共享内存中的字节串

## 信号量

1.通信原理  
给定一个数量对多个进程可见。多个进程都可以操作该数量增减，并根据数量决定自己的行为。

2. 实现方法

         from multiprocess import Semaphore
         sem = Semaphore(num)
         功能：创建信号量对象
         参数：信号量的初始值
         返回值：信号量对象

         sem.acquire() 将信号量减1，当信号量为0时阻塞
         sem.release() 将信号量加1
         sem.get_value() 获取信号量数量
         

         