#!/usr/bin/env python
# -*-coding:utf-8-*-


'''
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''


import random  # 导入随机数模块
import string  # 导入字符串模块
import os  # 导入OS模块


def activation_code(n):
    # 该函数用于生成激活码
    lis = list(string.ascii_letters + string.digits)
    L = []
    for i in range(n):
        # 生成不重复字符串
        str1 = ''.join((random.sample(lis, 18)))
        L.append(str1)
    return L


'''
test
'''

if __name__ == '__main__':
    L = activation_code(200)
    # 保存到文件ActivationCode.txt：
    if os.path.exists('ActivationCode.txt'):
        os.remove('ActivationCode.txt')
    fp = open('ActivationCode.txt', 'w')
    for i in L:
        fp.write(i + '\n')