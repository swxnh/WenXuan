#!/usr/bin/env python
# -*-coding:utf-8-*-


#  你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
# iPhone5分辨率 = 1136*640(高*宽)


import glob
from PIL import Image


def img_resize(file, arg):
    '''该函数用于按比例图片尺寸以适配不同分辨率
    path = 文件名
    arg = 分辨率二元组(宽， 高)
    '''
    size_m, size_n = arg
    # 打开图片，获取尺寸：
    img = Image.open(file)
    x, y = img.size
    # 比较图片尺寸与需求分辨率并改变
    if x > size_m or y > size_n:
        if x/y > size_m/size_n:
            img = img.resize((size_m, int(size_m*y/x)), Image.ANTIALIAS)
        else:
            img = img.resize((int(size_n*x/y), size_n), Image.ANTIALIAS)
        img.save(file)
    img.close()


if __name__ == '__main__':
    # 获取目录"5"下的所有图片，执行改变尺寸操作
    for i in glob.glob(r'5/*.jpg') + glob.glob(r'5/*.png'):
        img_resize(i, (640, 1136))