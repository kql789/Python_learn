# @Author : Kql
# @Time : 2023/8/14 18:52
# @FileName : select_test.py

from select import select
from socket import *

s = socket()
# Bind the socket to a local address and port
s.bind(("127.0.0.1", 8888))
# Listen for incoming connections
s.listen(5)
# Open a file to log the IO
f = open("./photo/log.txt", 'r+')
# Print the IO status
print("监控IO")
# Select the sockets
rs, ws, xs = select([s], [f], [], 3)

# Print the IO status
print("rlist:", rs)
print("wlist:", ws)
print("xlist:", xs)
