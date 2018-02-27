#!/usr/bin/env python
# -*-coding:utf-8-*-


# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。


import glob


def glob_py(path):
    # 匹配.py文件
    return glob.glob(path+'/*.py')


def count_lines(file):
    # 对传入代码文件进行注释、空行、代码行统计
    w = {'blank_lines': 0, 'notation_lines': 0, 'code_lines': 0}        # 字典用于储存行数信息
    fp = open(file, 'r', encoding='UTF-8')      # 以utf-8编码打开文件
    lines = (i.strip() for i in fp.readlines())     # 将每行行首去空格后生成生成器以使用next()方法
    for line in lines:
        if not line:        # 空行判断
            w['blank_lines'] += 1
        elif line.startswith('#'):      # '#'号开头的注释行判断
            w['notation_lines'] += 1
        elif line.startswith("'''"):      # 以三点号开头的注释行判断
            w['notation_lines'] += 2
            try:
                while not next(lines).startswith("'''"):      # 调用next()方法，直到匹配结尾三点号
                    w['notation_lines'] += 1
            except StopIteration:
                break
        elif line.startswith('"""'):        # 以双三点号开头的注释行判断
            w['notation_lines'] += 2
            try:
                while not next(lines).startswith('"""'):        # 调用next()方法，直到匹配结尾双三点号
                    w['notation_lines'] += 1
            except StopIteration:
                break
        else:       # 剩余即为代码行
            w['code_lines'] += 1
    fp.close()
    return w


if __name__ == '__main__':
    files = glob_py('7')
    for f in files:
        print(count_lines(f))