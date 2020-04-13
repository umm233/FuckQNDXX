#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-24 13:56:55
# @Author  : emmmmm

from PIL import Image, ImageDraw, ImageFont
import random, os


def get_chinese(s):
    digit = {
        '0': '零',
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '七',
        '8': '八',
        '9': '九'
    }
    return digit[s]


def get_random_font():
    font_list = os.listdir("./font")
    font_name = font_list[random.randint(0, len(font_list) - 1)]
    return font_name


def draw_head(season, episode):
    img = Image.new('RGB', (828, 78), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    font_type = "./font/" + get_random_font()
    color = "#000000"

    no = "×"
    title = '“青年大学习”第{}季第{}期'.format(season, episode)
    dots = "..."
    font = ImageFont.truetype(font_type, 28)
    font_no = ImageFont.truetype(font_type, 38)
    font_dot = ImageFont.truetype(font_type, 35)
    draw.text((23, 15), no, color, font=font_no)
    draw.text((60, 20), title, color, font=font)
    draw.text((750, 9), dots, color, font=font_dot)
    # img.show()
    img.save("./static/img/qndxx/head.jpg")


def merge(img1, down_path):
    img1, down_img = Image.open(img1), Image.open(down_path)
    size1, size2 = img1.size, down_img.size

    merge_img = Image.new('RGB', (size1[0], size1[1] + size2[1]))
    loc1, loc2 = (0, 0), (0, size1[1])
    merge_img.paste(img1, loc1)
    merge_img.paste(down_img, loc2)
    merge_img.save("./static/img/qndxx/latest.jpg")


def make_head(down_img, season, episode):
    draw_head(season, episode)
    head_img = "./static/img/qndxx/head.jpg"
    merge(head_img, down_img)


if __name__ == '__main__':
    make_head()
