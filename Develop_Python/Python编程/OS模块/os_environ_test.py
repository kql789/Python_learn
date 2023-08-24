# @Author : Kql
# @Time : 2023/8/24 16:47
# @FileName : os_environ_test.py
# @Blog ：https://blog.csdn.net/weixin_56175042
import os

# 1. 定义
"""
通过 os.environ 获取环境变量，什么是环境变量呢？环境变量是程序和操作系统之间的通信方式。
有些字符不宜明文写进代码里，比如数据库密码，个人账户密码，如果写进自己本机的环境变量里，
程序用的时候通过 os.environ.get() 取出来就行了。这样开发人员本机测试的时候用的是自己本机的一套密码，
生产环境部署的时候，用的是公司的公共账号和密码，这样就能增加安全性。os.environ 是一个字典，是环境变量的字典。
“HOME” 是这个字典里的一个键，如果有这个键，返回对应的值，如果没有，则返回 none

"""
# 主目录下所有的 key
print(os.environ.keys())

# 2. 常见key字段
'''
windows下
os.environ['HOMEPATH']:当前用户主目录。
os.environ['TEMP']:临时目录路径。
os.environ["PATHEXT"]:可执行文件。
os.environ['SYSTEMROOT']:系统主目录。
os.environ['LOGONSERVER']:机器名。
os.environ['PROMPT']:设置提示符。

Linux下
os.environ['USER']:当前使用用户。
os.environ['LC_COLLATE']:路径扩展的结果排序时的字母顺序。
os.environ['SHELL']:使用shell的类型。
os.environ['LAN']:使用的语言。
os.environ['SSH_AUTH_SOCK']:ssh的执行路径。

'''
print(os.environ['USER'])

# 3. os.environ.get()
"""
os.environ 是一个字典，是环境变量的字典，可以通过 get 方法获取键对应的值
注意 os.environ 的类型并不是 <class ‘dict’>，不是所有字典的函数都能用

os.environ.get() 是 python 中 os 模块获取环境变量的一个方法，如果有这个键，返回对应的值，
如果没有，则返回 none。
也可以设置默认值，当键存在时返回对应的值，不存在时，返回默认值

"""

print(os.environ.get('USER'))
# 环境变量USW不存在，则返回设置的默认值default
print(os.environ.get("USW", "default"))

# 4. 环境变量用法总结–设置、修改、获取、删除、判断

# 4.1 设置系统环境变量
'''
os.environ['环境变量名称']='环境变量值' #其中key和value均为string类型
os.putenv('环境变量名称', '环境变量值')
os.environ.setdefault('环境变量名称', '环境变量值')
'''
os.environ['XHS_HOME'] = 'local'
print(os.environ.get('XHS_HOME', 'None'))
os.putenv('xhs_user', 'kanqilu')
print(os.environ.get('xhs_user', 'no'))
os.environ.setdefault('xhs_email', 'kanqilu@xiaohongshu.net')
print(os.environ.get('xhs_email', 'no'))

# 4.2 修改系统环境环境变量
# os.environ['环境变量名称']='新环境变量值'

# 4.3 删除系统环境变量
del os.environ['环境变量名称']
del(os.environ['环境变量名称'])

# 4.5 判断系统环境变量是否存在
# '环境变量值' in os.environ   # 存在返回 True，不存在返回 False


