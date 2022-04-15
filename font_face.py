#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:font_face.py
# 创建日期:2022/4/15 10:16
# 作者:XU
# 联系邮箱:iswongx@163.com


import requests
import re
from fontTools.ttLib import TTFont


# 获取原页面
def get_html(url):
    '''

    :param url: 字体加密原始页面连接
    :return: 字体加密原始页面
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        # print(res.text)
        return res.text


# 下载字体文件
def get_download(html, file_name):
    '''

    :param html: 原始页面html
    :return: None
    下载字体文件到本地
    '''
    url = re.findall("src: url\('(.*?)'\) format", html, re.S)[1]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(res.content)


def font_to_xml(file_name):
    '''

    :param file_name: 字体文件存放位置
    :return: 返回xml格式字体文件
    '''
    font = TTFont(file_name)
    font.saveXML("font.xml")
    return font


def get_true_font_data(font):
    '''
    # 获取字体映射关系
    :param font: xml格式字体
    :return: 字体对应字典
    for example {100054: 'nine', 100056: 'two', 100057: 'eight', 100058: 'zero', 100059: 'period', 100060: 'one', 100061: 'six', 100062: 'four', 100063: 'five', 100064: 'three', 100065: 'seven'}
    '''

    font_cmap = font['cmap'].getBestCmap()
    print(font_cmap)
    return font_cmap


def change_font_map(font_cmap):
    '''

    :param font_cmap: xml中字体对应关系
    :return: 改变后的字体对应关系
    '''
    # 基础映射
    base = {'period': '.', 'four': 4, 'three': 3, 'six': 6, 'zero': 0,
            'one': 1, 'eight': 8, 'seven': 7, 'nine': 9, 'five': 5, 'two': 2}
    # 更改映射
    for key in font_cmap:
        font_cmap[key] = base[font_cmap[key]]
    print(font_cmap)
    return font_cmap


def replace_font_map(font_cmap, new_html):
    '''

    :param font_cmap: 字体映射字典
    :param new_html: 要替换的html原始页面
    :return: 替换后的页面数据
    '''
    # 替换映射
    for key in font_cmap:
        new_html = new_html.replace('&#' + str(key) + ';', str(font_cmap[key]))
    # print(html_data)
    return new_html


# 最终调用字体解密完成
def main(url):
    # url 要解密的网页链接
    html_data = get_html(url=url)
    get_download(html=html_data, file_name='font.woff')
    font = font_to_xml(file_name='font.woff')
    font_cmap = get_true_font_data(font=font)
    font_change = change_font_map(font_cmap=font_cmap)
    new_html = replace_font_map(font_cmap=font_change, new_html=html_data)
    print(new_html)
