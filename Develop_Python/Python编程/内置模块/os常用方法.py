# @Author :Kql
# @Time    : 2023/10/22 14:12
# @FileName: os常用方法.py
# @Blog    ：https://blog.csdn.net/weixin_56175042

import os

# 1. 获取当前工作目录的路径
print(os.getcwd())

# 2. 改变当前工作目录到指定目录
#os.chdir(path)

# 3. 返回指定目录中的文件和子目录列表
path = '/Users/'
print(os.listdir(path))

# 4. 创建一个目录
print(os.mkdir('/Users/Kql/Desktop/test01'))

# 5. 递归创建多级目录
os.makedirs(path)

# 6. 删除指定目录
os.rmdir(path)
# 7. 删除指定文件
os.remove(path)

# 8. 重命名文件和 目录
os.rename(old, new)

# 9. 检查指定路径是否存在
os.path.exists(path)

# 10. 获取指定路径的绝对路径
os.path.abspath(path)

# 11. 检查指定路径是否为文件
os.path.isfile(path)

# 12. 检查指定路径是否为目录
os.path.isdir(path)

# 13. 将多个路径部分连接成一个完整的路径
os.path.join(path1, path2)

# 14. 分割路径为目录和文件名的元组
os.path.split(path)

# 15. 分割路径为文件名和后缀名
os.path.splitext(path)

# 16. 获取文件的大小
os.path.getsize(path)

# 17. 获取文件或路径的创建时间
os.path.getctime(path)

# 18. 获取文件或路径的修改时间
os.path.getmtime(path)

# 19. 检查指定路径是否为绝对路径
os.path.isabs(path)

# 20. 递归删除多级目录，如果目录为空的话
os.removedirs(path)

# 21. 删除目录
os.rmdir(path)

# 22. 获取环境变量的值
os.getenv(key,default=None)

# 23. 设置环境变量的值
os.putenv(key,value)

