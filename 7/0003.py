#!/usr/bin/env python
# -*-coding:utf-8-*-


# 第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中

import redis


def main():
    # 创建数据库管道：
    r = redis.Redis(host='localhost', port=6379, db=0)
    # 打开文件：
    fp = open('ActivationCode.txt', 'r')
    # 执行写入：
    for i in fp.readlines():
        r.sadd('ActivationCode', i.strip())


'''
test
'''
if __name__ == '__main__':
    main()