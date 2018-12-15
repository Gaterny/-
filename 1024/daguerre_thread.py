#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import re
import os
import threading
import queue


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


# 获取达盖尔的旗帜页面中帖子链接
def get_index(page_url):
    html = request_url(page_url)
    pattern = re.compile(r'<h3>.*?href="(.*?)".*?P].*?</h3>')
    href = re.findall(pattern, html)
    index_url_list = []
    for link in href:
        url = 'https://dd.etet.men/' + link
        index_url_list.append(url)

class DaguerreSpider(threading.Thread):
    """达盖尔的旗帜多线程爬虫"""
    def __init__(self, page_url):
        super(DaguerreSpider, self).__init__()
        self.url=page_url

    def request(self, url):
        res = requests.get(url, headers=headers)
        res.encoding = "gbk"
        html = res.text
        return html

    def get_index(self, page_url):
        html = self.request(page_url)
        pattern = re.compile(r'<h3>.*?href="(.*?)".*?P].*?</h3>')
        href = re.findall(pattern, html)
        index_url_list = []
        for link in href:
            url = 'https://dd.etet.men/' + link
            index_url_list.append(url)
        return index_url_list

    def run(self):
        while self.get_index(page_url) > 0:
            index_html = request_url(url)
            save_img(index_html)


def save_img(index_html):
    # 获取图集名称

    pattern1 = re.compile(r'<h4>(.*?)</h4>', re.S)
    title = re.findall(pattern1, index_html)
    # 获取图集所有图片地址
    pattern2 = re.compile(r"<input.*?data-src='(.*?)'.*?>&nbsp", re.S)
    img_urls = re.findall(pattern2, index_html)

    # 创建本地存储目录
    root_dir = 'E:/1024/'
    file_path = root_dir + str(title[0])
    if os.path.exists(file_path):
        print("文件夹已存在，跳过")
    else:
        os.mkdir(file_path)

    n = 1
    # 保存到本地
    for img_url in img_urls:
        img = requests.get(img_url, headers=headers).content
        img_name = str(n) + '.jpg'
        with open(file_path + '\\' + img_name, 'wb') as f:
            f.write(img)
            f.close()
            n += 1


def main(i):
    page_url = 'https://dd.etet.men/thread0806.php?fid=16&search=&page=' + str(i)
    get_index(page_url)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool(4)
    pool.map(main, (i for i in range(1, 20)))
    pool.close()
    pool.join()