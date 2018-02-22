#!/usr/bin/env python
# -*-coding:utf-8-*-


#  任一个英文的纯文本文件，统计其中的单词出现的个数


def text_count(file, str):
    '''
    该函数用于统计文本中某个单词的出现频率
    path = 需要被统计的文本 str = 需要统计的单词
    '''
    fp = open(file, 'r')
    fr = fp.read()
    fp.close()
    return fr.count(str)


if __name__ == '__main__':
    print(text_count('One Hundred Years of Solitude.txt', 'YEARS'))