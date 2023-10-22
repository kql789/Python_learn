# @Author :Kql
# @Time    : 2023/10/22 14:45
# @FileName: datetime常用方法.py
# @Blog    ：https://blog.csdn.net/weixin_56175042

import datetime

"""
datetime类：

datetime 类是 datetime 模块中最常用的类，用于表示日期和时间。
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0):
用于创建一个具体的日期和时间对象。
参数 year, month, day 分别表示年、月、日。
可选参数 hour, minute, second, microsecond 表示时、分、秒、微秒，默认值为 0。
datetime.now():

返回当前日期和时间。
datetime.today():

返回当前日期和时间。
datetime.strptime(date_string, format):

从字符串中解析日期和时间，使用给定的格式。
datetime.strftime(format):

格式化日期和时间为字符串，使用给定的格式。
"""

# 1. 获取当前时间和日期
print(datetime.datetime.now())

# 2. 返回当前日期和时间
print(datetime.datetime.today())

# 3. 从字符串中解析日期和时间，使用给定的格式
print(datetime.datetime.strptime("2022-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"))

# 4. 格式化日期和时间为字符串，使用给定的格式
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# 5. 创建特定日期和时间
print(datetime.datetime(2022, 1, 1, 12, 0, 0))

"""
date类：

date 类用于表示日期，不包含时间信息。

date(year, month, day):

创建一个日期对象，参数为年、月、日。
date.today():
返回当前日期。
"""
# 1. 创建一个日期对象，参数为年、月、日。
print(datetime.date(2022, 1, 1))

# 2. 返回当前日期。
print(datetime.date.today())

"""
time类：

time 类用于表示时间，不包含日期信息。

time(hour=0, minute=0, second=0, microsecond=0):
创建一个时间对象，参数为时、分、秒、微秒。
"""
# 创建一个时间对象，参数为时、分、秒、微秒。
print(datetime.time(12, 0, 0))

"""
timedelta 类用于表示时间间隔。

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):

创建一个时间间隔对象。
datetime + timedelta:

可以用于日期时间对象的加法操作，用来增加时间间隔。
"""

#  创建一个时间间隔对象。
print(datetime.timedelta(days=1, hours=5))

#  日期时间对象 + 时间间隔对象
print(datetime.datetime.now() + datetime.timedelta(days=1, hours=5))

"""
strftime() 和 strptime()：
这两个方法允许您以指定格式将日期和时间对象转换为字符串，以及从字符串解析日期和时间。
"""
# 1. 格式化日期和时间为字符串，使用给定的格式
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 2. 从字符串中解析日期和时间，使用给定的格式
print(datetime.datetime.strptime("2022-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"))
