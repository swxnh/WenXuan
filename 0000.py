#!/usr/bin/env python
# -*-coding:utf-8-*-


# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字

from PIL import Image, ImageDraw, ImageFont


def img_fun(file):
    img = Image.open(file)      # 打开图片
    dr = ImageDraw.Draw(img)        # 创建管道
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', size=40)        # 获取字体
    x, y = img.size     # 获取尺寸
    dr.text((x - 40, 0), '4', font=font, fill='#ff0000')        # 加入红色字“4”
    img.save('result.jpg', 'jpeg')      # 保存图片
    img.close()


if __name__ == '__main__':
    img_fun('0.jpg')
