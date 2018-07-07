#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random
import time
import hashlib
import requests


class Translator(object):
    """基于有道翻译的翻译程序"""

    def __init__(self, keyword):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                      'like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
        self.url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        self.keyword = keyword
        self.form_data = {
            'i': keyword,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.get_salt(),
            'sign': self.get_sign(),
            'doctype': 'json',
            'version': 2.1,
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'false'
        }

    # 分析fanyi.min.js请求，获得salt的构造方式
    # r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
    # 当前时间戳 + 随记数
    def get_salt(self):
        current_time = time.time()
        salt = int(current_time * 1000) + int(random.random())  # int是为了取整
        return salt

    # i = n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!");
    # sign的值是几个数相加后得到的值再通过MD5加密获得
    def get_sign(self):
        t = self.keyword
        r = self.get_salt()
        md5_sign = "fanyideskweb" + str(t) + str(r) + 'ebSeFb%=XZ%T[KZ)c(sy!'
        m = hashlib.md5()
        m.update(md5_sign.encode('utf-8'))
        sign = m.hexdigest()
        return sign

    def translate(self):
        """这是一个post请求"""
        res = requests.post(self.url, params=self.form_data, headers=self.headers)
        html = json.loads(res.text, encoding='utf-8')
        print(html['translateResult'][0][0]['tgt'])


if __name__ == "__main__":
    while True:
        keyword = input('请输入想要翻译的内容(输入exit退出)：')
        if keyword == 'exit':
            break
        trans = Translator(keyword)
        trans.translate()
