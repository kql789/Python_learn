# @Author : Kql
# @Time : 2023/7/18 18:35
"""
一段文字中有() {} []，编写一个接口程序去判定括号是否匹配正确
"""
from lstack import *

text = "Functions Defined The core of (extensible programming) is defining functions. " \
       "Python allows (manda[tor]y) and optional arguments, keyword [arguments], and even " \
       "arbitrary argument lists. {More} about defining functions in {Python} 3"

# 待处理的字符集
parens = "(){}[]"
# 入栈字符集
left_parnes = "([{"

# 验证匹配关系
opposite = {'}': '{', ']': '[', ')': '('}

# 创建链式堆栈
ls = LStack()


# 编写生成器，用来遍历字符串，不断的提供括号及其位置
def parent(text):
    # 索引位置和文本的长度
    i, text_len = 0, len(text)
    while True:
        while i < text_len and text[i] not in parens:
            i += 1
        # 遍历到字符串结尾
        if i >= text_len:
            return
        else:
            yield text[i], i
            i += 1


# 功能函数，判断提供的括号是否匹配
def ver():
    for pr, i in parent(text):
        if pr in left_parnes:
            ls.push((pr, i))  # 左括号入栈
        elif ls.is_empty() or ls.pop()[0] != opposite[pr]:  # 如果一开始是右括号，那么则出错
            print("Unmatching is found at %d for %s" % (i, pr))
            break
    else:
        if ls.is_empty():
            print("All parentheses are matched")
        else:
            # 左括号多了
            d = ls.pop()
            print("Unmatching is found at %d for %s" % (d[1], d[0]))


if __name__ == '__main__':
    ver()
