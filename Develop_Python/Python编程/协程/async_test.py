# @Author : Kql
# @Time : 2023/8/16 18:04
# @FileName : async_test.py
# @Blog ：https://blog.csdn.net/weixin_56175042
import asyncio


# 定义两个异步函数，分别用于打印和暂停1秒


async def func1():
    print("start1....")
    await asyncio.sleep(1)
    print("end1....")


async def func2():
    print("start2....")
    await asyncio.sleep(1)
    print("end2....")


# 创建两个异步任务
cor1 = func1()
cor2 = func2()

# 将两个异步任务添加到事件循环中并等待它们完成
tasks = [asyncio.ensure_future(cor1), asyncio.ensure_future(cor2)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
