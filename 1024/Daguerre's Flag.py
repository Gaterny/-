#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author:  Gaterny
# @Github:  https://github.com/Gaterny
# @Daguerre's Flag
# @在新时代的我们基础上改了部分正则以匹配高亮帖，后期会加上多进程

import requests
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def request_page(page_url):
    res = requests.get(page_url, headers=headers)
    res.encoding = "gbk"
    html = res.text
    return html


def get_index(index_url):
    html = request_page(index_url)
    pattern = re.compile(r'<h3>.*?href="(.*?)".*?P].*?</h3>')
    href = re.findall(pattern, html)
    for link in href:
        url = 'https://dd.etet.men/' + link
        index_html = request_page(url)
        save_img(index_html)


def save_img(index_html):
    pattern1 = re.compile(r'<h4>(.*?)</h4>', re.S)
    title = re.findall(pattern1, index_html)
    pattern2 = re.compile(r"<input.*?data-src='(.*?)'.*?>&nbsp", re.S)
    img_urls = re.findall(pattern2, index_html)

    root_dir = 'E:/1024/'
    file_path = root_dir + str(title[0])

    if os.path.exists(file_path):
        print("文件夹已存在，跳过")
    else:
        os.mkdir(file_path)

    n = 1
    for img_url in img_urls:
        img = requests.get(img_url, headers=headers).content
        img_name = str(i) + '.jpg'
        with open(file_path + '\\' + img_name, 'wb') as f:
            f.write(img)
            f.close()
            n += 1


if __name__ == '__main__':
    for i in range(1, 20):
        index_url = 'https://dd.etet.men/thread0806.php?fid=16&search=&page=' + str(i)
        get_index(index_url)
