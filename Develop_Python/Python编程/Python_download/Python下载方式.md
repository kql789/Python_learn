```Shell

url = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.tDlhQ4ZG18uyo1LsG1PilAHaHa?rs=1&pid=ImgDetMain'
```

## 1.requests方式

```python
import requests
url = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.tDlhQ4ZG18uyo1LsG1PilAHaHa?rs=1&pid=ImgDetMain'
mydata = requests.get(url)
open('/Users/user/Desktop/data/photo.jpg','wb').write(mydata.content)

```

## 2.wget方式

```python
# pip install wget

import wget

url = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.tDlhQ4ZG18uyo1LsG1PilAHaHa?rs=1&pid=ImgDetMain'
wget.download(url,''/Users/user/Desktop/data/photo1.jpg'')

```

## 3.下载重定向文件
**HTTP 重定向是指在发出请求后，服务器返回一个指示浏览器或客户端前往另一个 URL 的响应。**

```python
import requests
url = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.tDlhQ4ZG18uyo1LsG1PilAHaHa?rs=1&pid=ImgDetMain'
mydata = requests.get(url,allow_redirects=True)
open('/Users/user/Desktop/data/photo.jpg','wb').write(mydata.content)
# 当 allow_redirects 参数为 True 时（默认值），requests.get 方法会自动处理重定向，跟随重定向响应，最终获取重定向后的内容。如果
#  allow_redirects 参数为 False，则 requests.get 方法不会自动处理重定向，而是返回包含重定向信息的响应对象，用户可以根据需要对重定向进行处理。

```

## 4.分块下载大文件
requests中有stream属性。该属性用于控制是否立即下载响应内容，而是通过流式传输的方式来获取响应数据。当 stream 属性为 True 时，  
表示以流的方式获取响应内容，可以逐步获取响应的数据流，而不需要一次性将所有数据加载到内存中。这对于处理大型响应数据或者需要逐步处理数据的场景非常有用。  
**在指定目录下创建一个名为book.pdf的文件，并打开进行写入，我们指定每次下载的块大小，将其设置为1024字节，接着遍历每个块，并在文件中写入这些块，直到结束**

```python
import requests
url = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.tDlhQ4ZG18uyo1LsG1PilAHaHa?rs=1&pid=ImgDetMain'
reponse = requests.get(url,stream=True)
with open('./book.pdf','wb') as f:
    for chunk in reponse.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

```

## 5.并行下载/批量下载 
os 和time模块来检查下载文件的需要时间。ThreadPool模块可以使用线程池运行多个线程或进程。  

```python

import os
import requests
from time import time
from multiprocessing.pool import ThreadPool

# 创建一个函数，将响应分块发送到一个文件
def url_response(url):
    path,url = url
    r = requests.get(url,stream=True)
    with open(path,'wb') as f:
        for ch in r:
            f.write(ch)

# 二维数组，指定了需要下载的路径和url
urls = [
('Events1','https://qsh-cos-wh-biaozhu-1251524319.cos.ap-shanghai.myqcloud.com/v4_240202_%E5%9B%BE%E7%89%87/0003c6f4-c117-11ee-bc1b-00163e0477d2.jpg'),
('Events2','https://qsh-cos-wh-biaozhu-1251524319.cos.ap-shanghai.myqcloud.com/v4_240202_%E5%9B%BE%E7%89%87/00065e78-c117-11ee-bc1b-00163e0477d2.jpg'),
('Events3','https://qsh-cos-wh-biaozhu-1251524319.cos.ap-shanghai.myqcloud.com/v4_240202_%E5%9B%BE%E7%89%87/000fd336-c117-11ee-bc1b-00163e0477d2.jpg'),
('Events4','https://qsh-cos-wh-biaozhu-1251524319.cos.ap-shanghai.myqcloud.com/v4_240202_%E5%9B%BE%E7%89%87/00175f48-c117-11ee-bc1b-00163e0477d2.jpg'),
('Events5','https://qsh-cos-wh-biaozhu-1251524319.cos.ap-shanghai.myqcloud.com/v4_240202_%E5%9B%BE%E7%89%87/001e47fe-c117-11ee-bc1b-00163e0477d2.jpg')
    
]
start = time()
# 调用前面封装的函数，并开始计算时间
# 顺序下载
for x in urls:
    url_response(x)
print(f"Time to download:{time() -start}")

# 并发下载，创建9个线程的线程池，并使用imap_unordered函数并发地应用到urls列表中的每个元素上。
ThreadPool(9).imap_unordered(url,urls)

```

## 5. 进度条下载

clint模块中的一个ui组件中有进度条。
```Shell
pip install clint
```

```python
import requests
from clint.textui import progress

url = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.tDlhQ4ZG18uyo1LsG1PilAHaHa?rs=1&pid=ImgDetMain'
response = requests.get(url,stream=True)
with open("/Users/user/Desktop/data/phopt3.jpg",'wb') as f:
    total_length = int(response.headers.get('content-length'))
    # expected_size参数表示预期的迭代次数，根据总长度来预期迭代次数
    # response.iter_content(chunk_size=1024) 返回一个生成器，逐块读取响应内容，每次读取1024字节
    for ch in progress.bar(response.iter_content(chunk_size=1024),expected_size=(total_length/1024)+1):
        if ch:
            f.write(ch)
```

## 6.urllib下载

