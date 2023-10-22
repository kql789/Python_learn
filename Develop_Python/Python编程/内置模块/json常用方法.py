# @Author :Kql
# @Time    : 2023/10/22 14:59
# @FileName: json常用方法.py
# @Blog    ：https://blog.csdn.net/weixin_56175042
import json

'''
在 Python 中，json 模块用于处理 JSON（JavaScript Object Notation）数据。JSON是一种轻量级的数据交换格式，常用于数据传输和配置文件。以下是一些 json 模块中常用的方法：

1. json.dumps(obj, indent=None, separators=None, ensure_ascii=True):

    将 Python 对象转换为 JSON 格式的字符串。
    obj 是要转换为 JSON 的对象。
    indent 用于定义缩进的格式，通常为整数，用于美化输出。
    separators 是一个元组，包含分隔不同部分的字符（如 (',', ':')）。
    ensure_ascii 是一个布尔值，用于控制是否确保所有非ASCII字符都被转义为 \\uXXXX格式。
    
2. json.loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None):
    将 JSON 格式的字符串解析为 Python 对象。
    
    s 是包含 JSON 数据的字符串。
    encoding 用于指定字符串的编码。
    cls 用于指定自定义的 JSON 解析类。
    object_hook 是一个可调用对象，用于在解析 JSON 时自定义对象的创建。
    parse_float、parse_int、parse_constant 可以用于自定义浮点数、整数和常量的解析。
    object_pairs_hook 用于在解析 JSON 时自定义对象的创建，但只适用于对象是 JSON 对象的情况。

3. json.dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw):

    将 Python 对象序列化为 JSON 格式并写入文件对象 fp。
    obj 是要序列化的对象。
    fp 是已打开的文件对象。
    其他参数与 json.dumps 方法类似。

4. json.load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None):

    从文件对象 fp 中读取 JSON 数据并将其解析为 Python 对象。
    fp 是已打开的文件对象。
    其他参数与 json.loads 方法类似。
这些方法使您能够方便地在 Python 中处理 JSON 数据，包括序列化（将 Python 对象转换为 JSON 格式）和反序列化（将 JSON 数据解析为 Python 对象）操作。
JSON在Web开发、API通信和配置文件中广泛使用，因此 json 模块是 Python 中非常重要的工具。
'''

# 1. 将python对象转换为字符串
data = {"name": "zhangsan", "age": 18, "sex": "male"}
print(json.dumps(data))

# 2. 将字符串转换为python对象
json_str = '{"name": "zhangsan", "age": 18, "sex": "male"}'
print(json.loads(json_str))

# 3. 将Python对象写入json文件
data = {"name": "zhangsan", "age": 20}

with open("./data.json", "w") as f:
    json.dump(data, f)

# 4. 从json文件中读取数据并解析为python对象
with open("./data.json", "r") as f:
    json.load(f)

# 5. 设置JSON格式化选项（缩进、分隔符）等
json_str = json.dumps(data, indent=4, separators=(",", ":"))

# 6. 处理特殊书类型(日期时间)的编码和解码
from datetime import datetime


# 自定义日期时间编码器
def datetime_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()


da = {"name": "zahngdan", "birthdate": datetime(1990, 1, 1)}

josn_str = json.dumps(da, default=datetime_encoder)


# 自定义时间编码器
def datetime_decoder(dic):
    if "birthdate" in dic:
        dic["birthdate"] = datetime.fromisoformat(dic["birthdate"])
    return dic


data = json.loads(json_str, object_hook=datetime_encoder)

# 7. 处理json中的异常情况

try:
    data = json.loads(json_str)
except json.JSONDecodeError as e:
    print(f'JSON decoding error: {e}')

# 8. 生成漂亮的json字符串适用于调试
data = {"name": "zhangsan", "age": 18, "sex": "male"}
json_str = json.dumps(data, indent=4, sort_keys=True)

