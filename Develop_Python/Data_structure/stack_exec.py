# Author :   Kql_unicorn
# Date   :   2023/7/17 09:20
"""
逆波兰表达式
"""
from sstack import *

st = SStack()

while True:
    exp = input()
    tmp = exp.split(" ")
    for i in tmp:
        if i not in ['+', '-', '*', '/', 'p']:
            st.push(float(i))
        elif i == '+':
            y = st.pop()
            x = st.pop()
            st.push(y + x)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(y - x)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(y * x)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(y / x)
        elif i == 'p':
            print(st.top())
