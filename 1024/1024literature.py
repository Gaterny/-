#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author:  Gaterny
# @Github:  https://github.com/Gaterny
# @爬取1024成人文学区，并存储到mongodb
# @1024文学区网页规则较乱，部分爬取不到，待解决中...

import re
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['1024novel']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def get_index(index_url):
    res = requests.get(index_url, headers=headers)
    res.encoding = 'gbk'
    index_html = res.text
    # print(res.text)
    pattern = re.compile(r'<td class="tal".*?id="">(.*?)<h3>.*?href="(.*?)".*?id="">(.*?)</a></h3>', re.S)
    items = re.findall(pattern, index_html)[4:]
    # print(items)
    for item in items:
        data = {
            'id': item[0].strip(),
            'href': item[1],
            'title': item[2]
        }
        # return data
        get_text(data)


def get_text(data):
    url = 'https://t66y.com/' + data['href']
    print('---------正在获取文章--------')
    res = requests.get(url, headers=headers)
    res.encoding = 'gbk'
    html = res.text
    texts = re.findall(r'<div class="tpc_content do_not_catch.*?>(.*?)</div>', html)
    text = texts[0].replace('<br>', '\n').replace('&nbsp', '')
    data['content'] = text
    save_to_mongo(data)


def save_to_mongo(result):
    try:
        if db['1024novel'].insert(result):
            print('存储到数据库成功!')
    except Exception:
        print('存储到数据库失败!')


def main():
    for i in range(1):
        index_url = 'https://t66y.com/thread0806.php?fid=20&search=&page=' + str(i)
        get_index(index_url)


if __name__ == '__main__':
    main()
