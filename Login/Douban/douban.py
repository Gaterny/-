#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 模拟登陆豆瓣

import requests
from bs4 import BeautifulSoup


session = requests.Session()
headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Referer': 'https://accounts.douban.com/',
}
login_url = 'https://www.douban.com/accounts/login'


def get_captcha():
    """获取验证码"""

    response = session.get(login_url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    captcha_image = soup.select('#captcha_image')

    # 验证是否需要输入验证码
    if captcha_image:
        captcha_url = captcha_image[0]['src']
        # print(captcha_url)
        captcha_content = session.get(captcha_url, headers=headers).content
        # 验证码图片存储到本地，手动输入验证码
        with open('captcha.gif', 'wb') as f:
            f.write(captcha_content)

        captcha = input('请输入验证码：')
        captcha_id = soup.find('input', attrs={'type': "hidden", 'name': "captcha-id"})['value']
        return captcha, captcha_id
    else:
        return '', ''


def login():
    """登录"""

    username = input('用户名：')
    password = input('密码：')
    data = {
        'source': 'index_nav',
        'redir': 'https://www.douban.com/',
        'form_email': username,
        'form_password': password,
        'login': '登录',
    }
    captcha, captcha_id = get_captcha()
    # 向data中添加字段
    data['captcha-solution'] = captcha
    data['captcha-id'] = captcha_id
    start_login = session.post(login_url, headers=headers, data=data)
    print(start_login.text)


def login_verify():
    """验证是否已在登录状态"""

    my_url = 'https://www.douban.com/mine/wallet/'
    # 禁止重定向，否则会出错
    # 访问我的钱包，status_code为200表示已登录，302表示未登录
    res = session.get(my_url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        print(res.text)
        print('login successfully!')
    else:
        print("login failed! restart login...")
        login()


if __name__ == '__main__':
    login_verify()
