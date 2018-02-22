#!/usr/bin/env python
# -*-coding:utf-8-*-


#  你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词


import glob


def glob_txt(path):
    # 匹配目录下所有文本文件
    return glob.iglob(path + r'/*.txt')


def key_word(file, n):
    '''返回文本file中单词频率前n的元组列表
    [(word1, word1_count), ......]
    '''
    word_dict = {}      # key = word        value = count
    fp = open(file, 'r')
    fr = fp.read()
    sp = fr.split()     # 利用单词间的空格进行分词
    for i in sp:
        if i not in word_dict:
            word_dict[i] = 1        # 新单词初始化并赋值为1
        else:
            word_dict[i] += 1       # 单词已存在则令值加1
    count_rank = sorted(word_dict.items(), key=lambda item: (-item[1], item[0]))        # 先用值排序，后用键排序
    top_n = count_rank[:n]
    fp.close()
    return top_n


if __name__ == '__main__':
    L = glob_txt('6')
    # 格式化输出：
    print('%-10s%-10s%s' % ('文件', '单词', '频率'))
    for f in L:
        for i in key_word(f, 3):
            print('%-12s%-12s%d' % (f, i[0], i[1]))