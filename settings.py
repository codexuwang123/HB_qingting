#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 文件名:settings.py
# 创建日期:2022/3/10 10:18
# 作者:XU
# 联系邮箱:iswongx@163.com


import time
import logging
import re


# 万能请求头格式化
def set_headers(string_new):
    '''

    :param string_new: 需要被格式化的请求头
    :return: None
    '''

    pattern = '^(.*?):(.*)$'
    for line in string_new.splitlines():
        print(re.sub(pattern, '\'\\1\':\'\\2\',', line).replace(' ', ''))


# 爬虫程序请求头集合

ua = {
    'user_agent': [
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
        'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0',
        'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0',
        'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
        'Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0',
        'Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Firefox/22.0',
        'Mozilla/5.0 (Microsoft Windows NT 6.2.9200.0); rv:22.0) Gecko/20130405 Firefox/22.0',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:21.0.0) Gecko/20121011 Firefox/21.0.0',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20130514 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.2; rv:21.0) Gecko/20130326 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130401 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130330 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130401 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130331 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 5.0; rv:21.0) Gecko/20100101 Firefox/21.0',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64;) Gecko/20100101 Firefox/20.0',
        'Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/19.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/18.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0)  Gecko/20100101 Firefox/18.0',

    ]}

# 正式库地址
true_sql = {
    'host': '',
    'port': 3306,
    'user': '',
    'password': '',
    'db': ''
}
# 测试库地址
test_sql = {
    'host': '101.200.79.65',
    'port': 12345,
    'user': 'pythonr_eptile',
    'password': 'BBnmNabyEHa6YMCN',
    'db': 'pythonr_eptile'
}

# 本地sql 测试地址
localhost_sql = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'data_info'
}

# 测试redis库地址
test_redis = {

    'host': '127.0.0.1',
    'port': 6379,
    'user': '',
    'password': '123456',
    'db': 8
}

# 正式库redis地址
true_redis = {
    'host': '',
    'port': 6379,
    'user': '',
    'password': '',
    'db': ''
}


# 设置日志函数
def set_log():
    now = int(time.time())
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y%m%d", timeArray)
    logger2 = logging.getLogger('mylogger2')
    logger2.setLevel(logging.DEBUG)
    if not logger2.handlers:
        fh = logging.FileHandler('../log/{}.txt'.format(otherStyleTime), 'a', encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(process)d - %(message)s')
        fh.setFormatter(formatter)
        logger2.addHandler(fh)
    return logger2


# 基础配置

set_ = {
    'max_page': 2,  # 最大页数 200
    'max_workers': 4  # 最大线程数量
}

# 特殊符号解析列表
code_new = [':', '：', '，', '_', '?', '！',

            '？', '。', '↑', '-', '、', '…', '《',

            '》', '(', ')', '>', '.', '/', '�',

            '&', '#', ';', '【', '】', '（', '）',

            ',', '|', '“', '❤', '～', '丨', '😯',

            '”', "'", '+', 'nbsp', '·', '•', '▪',

            '[', ']', '{', '}', '｜', '——', '↓',

            'xe', '*', '；', '~', '!', '♂', '\\', '－', '"', '=']

if __name__ == '__main__':

    # Stryker = '999999'
    # import time
    #
    # s = time.time()
    # for i in range(1000000000):
    #     # 生成四位数密码
    #     pwd = str(i).zfill(6).replace(' ', '')
    #     print(pwd, '---')
    #     if pwd == Stryker:
    #         print(pwd, '揭秘了')
    #         print(time.time() - s, '总耗时')
    #         break

    # 安全

    import zipfile
    import itertools

    dictionaries = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z']  # 组成破解字典的关键字符（可以按照自己需求添加）


    def allkeyword():  # 排列出字符所有4个字符的组合
        allkey1 = itertools.product(dictionaries, repeat=4)
        print(allkey1, '00')
        allkey2 = (''.join(i) for i in allkey1)
        return allkey2


    def trypassword(password):
        try:
            str = 'wx9a'
            # ZIPFILE = zipfile.ZipFile(r'D:\123\1.zip')  # 定义对象，相当于定义一个压缩文件1.zip
            # ZIPFILE.extractall(path=r'D:\12', pwd=password.encode('utf-8'))
            if password == str:
                print(f"解压成功,正确密码为：{password}")
                print(password)
                return True
        except:
            print(f"解压失败,尝试密码为：{password}")
            return False


    # 用trypassword函数返回的True或者Flase来判定程序是否终止。
    # for pwd in allkeyword():
    #     print(pwd)
    #     if trypassword(pwd):
    #         break

    # def get_1():
    #     print('开始获取所有链接')
    #
    #     url = 'www.baidu.com/page={}'.format(1)
    #     yield url
    #     print('获取连接中==')
    #
    # for k in get_1():
    #     print(k,'00')

    # def test_yield_from(*iterables):
    #     for i in iterables:
    #         yield from i
    #
    #
    # for i in test_yield_from([1, 3, 4], '12344'):
    #     print(i)

    import requests
    from fontTools.ttLib import TTFont

    html = '''</p>
        
        <p class="intro">心潮澎湃，无限幻想，迎风挥击千层浪，少年不败热血！</p>
        <p><em><style>@font-face { font-family: OWclySow; src: url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.eot?') format('eot'); src: url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.woff') format('woff'), url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.ttf') format('truetype'); } .OWclySow { font-family: 'OWclySow' !important;     display: initial !important; color: inherit !important; vertical-align: initial !important; }</style><span class="OWclySow">&#100060;&#100062;&#100059;&#100063;&#100056;</span></em><cite>万字</cite><i>|</i>
            <!-- <em>-1</em><cite>阅文总点击</cite><i>|</i>
            <em><style>@font-face { font-family: OWclySow; src: url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.eot?') format('eot'); src: url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.woff') format('woff'), url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.ttf') format('truetype'); } .OWclySow { font-family: 'OWclySow' !important;     display: initial !important; color: inherit !important; vertical-align: initial !important; }</style><span class="OWclySow">&#100058;</span></em><cite>会员周点击</cite><i>|</i> -->
            <em><style>@font-face { font-family: OWclySow; src: url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.eot?') format('eot'); src: url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.woff') format('woff'), url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.ttf') format('truetype'); } .OWclySow { font-family: 'OWclySow' !important;     display: initial !important; color: inherit !important; vertical-align: initial !important; }</style><span class="OWclySow">&#100060;&#100059;&#100061;&#100056;</span></em><cite>万总推荐</cite><i>|</i><em><style>@font-face { font-family: OWclySow; src: url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.eot?') format('eot'); src: url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.woff') format('woff'), url('https://qidian.gtimg.com/qd_anti_spider/OWclySow.ttf') format('truetype'); } .OWclySow { font-family: 'OWclySow' !important;     display: initial !important; color: inherit !important; vertical-align: initial !important; }</style><span class="OWclySow">&#100064;&#100063;&#100064;&#100056;</span></em><cite>周推荐</cite></p>'''

    import re

    url = re.findall("src: url\('(.*?)'\) format", html, re.S)[1]
    print(url)


    def get_download(url):
        # url = 'https://qidian.gtimg.com/qd_anti_spider/HyAfVhpi.woff'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            with open('font.woff', 'wb') as f:
                f.write(res.content)


    get_download(url=url)


    font = TTFont('font.woff')
    font.saveXML("font.xml")

    # 获取字体映射关系
    font_cmap = font['cmap'].getBestCmap()
    print(font_cmap)

    f = {'period': '.', 'four': 4, 'three': 3, 'six': 6, 'zero': 0,
         'one': 1, 'eight': 8, 'seven': 7, 'nine': 9, 'five': 5, 'two': 2}
    # 更改映射
    for key in font_cmap:
        font_cmap[key] = f[font_cmap[key]]

    print(font_cmap)

    # html_data = get_html()

    # 替换映射
    for key in font_cmap:
        html = html.replace('&#' + str(key) + ';', str(font_cmap[key]))

    print(html)
