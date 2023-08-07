# 线程编程（Thread）

## 线程基本概念

1. 什么是线程

- 线程被称为轻量级的进程
- 线程也可以使用计算机的多核资源，是多任务编程方式
- 线程是系统分配内核的最小单元
- 线程可以理解为进程的分支任务

2. 线程特征

- 一个进程可以包含多个线程
- 线程也是一个运行行为，消耗计算机资源
- 一个进程中的所有线程共享这个进程的资源
- 多个线程之间的运行互不影响各自远行
- 线程的创建和销毁消耗资源远小于进程
- 各个线程也有自己的ID等特征

## Threading 模块创建线程

            from threading import Thread
            t = Thread()
            功能：创建线程对象
            参数；target 绑定线程函数
                 args 元组 给线程函数位置传参
                 kwargs 字典 给线程函数键值传参

            t.start() 
            启动线程
            t.join([timeout])
            回收线程

## 线程对象属性

            t.name 线程名称
            t.setName()设置线程名称
            t.getName() 获取线程名称
            t.is_alive() 查看线程是否在生命周期
            t.daemon() 设置主线程和分支线程的退出关系
            t.setDaemon() 设置daemon属性值
            t.isDaemon() 查看daemon属性值
                daemon为True时，主线程退出，分支线程也退出。要在start前设置，通常
                不和join一起使用。