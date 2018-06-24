#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import time
import hmac
import base64
import json


session = requests.Session()
headers = {
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary2rH4t4XAo9fcDuO2',
            'origin': 'https://www.zhihu.com',
            'referer': 'https://www.zhihu.com/signin?next=%2Fexplore',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36',
            'x-requested-with': 'Fetch'
}
# login page
login_url = 'https://www.zhihu.com/signin?next=%2Fexplore'
login_api = 'https://www.zhihu.com/api/v3/oauth/sign_in'
captcha_url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'
form_data = {
            'client_id': 'c3cef7c66a1843f8b3a9e6a1e3160e20',
            'grant_type': 'password',
            'source': 'com.zhihu.web',
            'lang': 'en',   # en字母验证码，cn是倒立汉字验证码
            'ref_source': 'explore',
            'utm_source': ''
        }


def get_captcha():
    response = session.get(captcha_url, headers=headers)
    print(response.text)
    show_captcha = re.findall(r'{"show_captcha":(\w+)}', response.text)[0]
    # 如果为true则需要输入验证码，反之则不需要
    if show_captcha == 'true':
        response2 = session.put(captcha_url, headers=headers)
        print(response2.text)
        # img_base64 = re.findall(r'{"img_base64":"(.*?)"}', response2.text)[0]
        img_base64 = json.loads(response2.text)['img_base64']
        # print(img_base64)
        with open('captcha.jpg', 'wb') as f:
            f.write(base64.b64decode(img_base64))
        captcha = input('请输入验证码：')
        session.post(captcha_url, headers=headers, data={"input_text": captcha})
        return captcha
    return ''


def get_xsrf():
    response = session.get(login_url, headers=headers)
    xsrf = response.cookies['_xsrf']
    udid = response.cookies['d_c0'].split('|')[0].strip('"')
    return xsrf, udid


def get_signature():
    """
    function r(e, t) {
        var n = Date.now(),
        r = new i.a("SHA-1", "TEXT");
        return r.setHMACKey("d1b964811afb40118a12068ff74a12f4", "TEXT"),
        r.update(e),
        r.update(s),
        r.update("com.zhihu.web"),
        r.update(String(n)),
        u({
            clientId: s,
            grantType: e,
            timestamp: n,
            source: "com.zhihu.web",
            signature: r.getHMAC("HEX")
        },
        """
    h = hmac.new(key="d1b964811afb40118a12068ff74a12f4".encode('utf8'), digestmod='sha1')
    timestamp = str(int(time.time()*1000))
    h.update(
        (form_data['client_id']+form_data['grant_type']+timestamp+form_data['source']).encode('utf8')
    )
    signature = h.hexdigest()
    print(signature)
    return signature, timestamp


def login_verify():
    # 账户设置页面
    my_url = 'https://www.zhihu.com/settings/account'
    r = session.get(my_url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        print('login successfully!')
    else:
        print('未登录，开始登录...')
        login()


def login():
    x_xsrf, x_udid = get_xsrf()
    signature, timestamp = get_signature()
    captcha = get_captcha()
    username = input('请输入用户名：')
    password = input('请输入密码：')
    form_data.update({
        'timestamp': timestamp,
        'username': username,
        'password': password,
        'signature': signature,
        'captcha': '',
         })
    headers.update({
        'x-udid': x_udid,
        'x-xsrftoken': x_xsrf
    })
    print(headers)
    print(form_data)
    start_login = session.post(login_api, data=form_data, headers=headers)
    print(start_login.text)


if __name__ == '__main__':
    login_verify()
