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

## 6. 进度条下载

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

## 7.urllib下载

**在python中urllb是一个内置的模块，用于处理URLs(统一资源定位符)，包括打开、读取、解析和操作URLs。**
- urllib.request：用于打开和读取URLs，支持HTTP、HTTPS和FTP协议。
- urllib.parse：用于解析URLs，包括拆分URLs、构建URLs和编码/解码URL参数。
- urllib.error：定义了urllib模块可能引发的异常，例如HTTPError、URLError等。
- urllib.robotparser：用于解析robots.txt文件，以便程序可以遵守网站的爬取规则。

```python
import urllib.request

url = 'https://www.baidu.com/index.htm'

#使用urllib下载一个网页
urllib.request.urlretrieve(url, '/Users/user/Desktop/data/python.html')
print("下载完成!")
```

## 8. 代理下载
```python
import urllib.request

url = 'https://www.baidu.com/index.htm'

my_proxy = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:1080'})
openproxy = urllib.request.build_opener(my_proxy)
reponse = openproxy.open(url)
print(reponse.read().decode('utf-8'))

```

## 9. urllib3下载
urllib3是是urllib模块的改进版本，它提供了一个高级的HTTP库，可以用来替代urllib。urllib3具有以下优点：
- 支持连接池，可以重用已经建立的连接，提高性能。
- 支持自动处理重定向，避免手动处理。    
- 支持连接超时和读取超时，可以避免由于网络问题导致的下载失败。
- 支持SSL证书验证，可以避免由于证书问题导致的下载失败。


```python

import urllib3
import shutil

# 创建一个连接池管理器，可以维持多个连接
http = urllib3.PoolManager()

# 设置代理
proxy_url = 'http://127.0.0.1:1080'
http = urllib3.ProxyManager(proxy_url)

# 下载文件
url = 'https://example.com/file.zip'

local_file = '/path/to/save/file.zip'
reponse = http.request('GET', url)

with open(local_file, 'wb') as f:
    # 将文件对象内容复制到另一个文件对象中
    shutil.copyfileobj(reponse, f)

# 关闭连接
http.clear()
```
## 10. 使用asyncio下载
asyncio模块主要用于处理系统事件。它围绕一个事件循环进行工作，该事件循环会等待事件发生，然后对该事件作出反应。这个反应可以是调用另一个函数。这个过程称为事件处理。asyncio模块使用协同程序进行事件处理。

```python

import asyncio
import aiohttp

async def download_file(url,file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(file_name, 'wb') as file:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        file.write(chunk)
                        print(f"Downloaded {file_name} from {url}")
            else:
                print(f"Failed to download {url}")

async def main():
    tasks = [
        download_file('https://www.example.com/file1', 'file1.dat'),
        download_file('https://www.example.com/file2', 'file2.dat'),
    ]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
```

在上面的示例中，我们定义了一个名为 download_file 的异步函数，用于下载单个文件。然后，我们定义了一个主函数 main，该函数创建了多个下载任务，然后使用 asyncio.gather 来并行运行这些任务。
当运行这段代码时，它将使用 asyncio 来异步下载文件，并且能够同时下载多个文件而无需阻塞。这使得你能够更有效地利用网络和系统资源来完成文件下载任务。
在实际的应用中，你可能需要根据自己的需求进行一些调整和优化，比如添加错误处理、限制并发下载的数量等等。