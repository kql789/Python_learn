# @Author :Kql
# @Time    : 2023/10/22 14:31
# @FileName: sys常用方法.py
# @Blog    ：https://blog.csdn.net/weixin_56175042
import sys

"""
sys 模块是 Python 标准库中的一个重要模块，用于与解释器进行交互以及访问系统相关的功能。以下是一些 sys 模块中常用的方法和属性：
"""

# 1. sys.argv 获取命令行参数,这是一个包含命令行参数的列表。sys.argv[0] 是脚本的名称，其余元素是传递给脚本的参数。
sys.argv

# 2. 终止程序的执行，可选参数arg是返回给调用进程的退出状态码
arg = 0
sys.exit([arg])

# 3.返回当前运行python的操作系统的平台名称
sys.paltform

# 4. 返回python解释器的版本
sys.version

# 5. 这是一个包含用于搜索模块的目录的列表。您可以将自定义目录添加到 sys.path 中，以便 Python 解释器能够找到您自己编写的模块。
sys.path

# 6. 一个包含当前已导入的模块的字典。您可以使用它来查询已导入的模块。
sys.modules

# 7. 分别是标准输入和标准输出的对象。您可以重定向这些对象来改变输入和输出。
sys.stdin
sys.stdout

# 8. 标准错误输出的对象。用于将错误信息写入。
sys.stderr

# 9. 返回当前的异常信息，一个包含异常类型、异常值和回溯信息的元组。
sys.exc_info()

# 10. 返回对象的内存大小（字节数）。如果对象不支持 sys.getsizeof，可以提供一个默认值。
default = 20
sys.getsizeof(object[default])

# 11. 用于获取和设置递归调用的最大深度。默认值为 1000。
sys.getrecursionlimit()
sys.setrecursionlimit(limit)

# 12. 返回文件系统编码，它用于在文件名和路径中编码非ASCII字符。字符
sys.getfilesystemencoding()

# 13. 返回默认的字符串编码（通常是 'utf-8'）
sys.getdefaultencoding()

# 14.将字符串写入标准错误输出。
sys.stdout.write(str)

# 15. 从标准输入中读取一行文本。可选参数 size 用于指定最大读取字节数。
sys.stdin.readline([size])
