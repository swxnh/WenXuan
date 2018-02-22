#!/usr/bin/env python
# -*-coding:utf-8-*-


# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
# 导入模块：
import mysql.connector


def write_table(file, table):
    '''
    将path中的数据逐行写入至表table
    path = '', table = ''
    '''
    conn = mysql.connector.connect(user='root', password='password', database='test')     # 创建通道
    cursor = conn.cursor()
    fp = open(file, 'r')    # 打开文件
    # 执行写入：
    for i in fp.readlines():
        cursor.execute("INSERT INTO %s(name) value(%s)", [table, i])
    # 提交并关闭：
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    write_table('ActivationCode.txt', 'user')
