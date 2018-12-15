#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    'Host': 'github.com',
    'Referer': 'https://github.com/',
           }


class GithubLogin:
    def __init__(self):
        self.index_url = 'https://github.com/login'
        self.login_url = 'https://github.com/session'
        self.profile = 'https://github.com/settings/profile'
        self.session = requests.Session()

    # get authenticity-token, 一个隐藏表单，在网页源代码中查看
    def get_token(self):
        response = self.session.get(self.index_url, headers=headers)
        pattern = re.compile(r'authenticity_token" value="(.*?)"')
        authenticity_token = re.findall(pattern, response.text)[0]
        return authenticity_token

    def run(self):
        form_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_token(),
            'login': 'your username',
            'password': 'your email',
        }
        response = self.session.post(self.login_url, data=form_data, headers=headers)
        if response.status_code == 200:
            self.verify()

    def verify(self):
        response = self.session.get(self.profile, headers=headers)
        if response.status_code == 200:
            print('You have successfully logged in !')
        else:
            print('Login failed !')


if __name__ == "__main__":
    login = GithubLogin()
    login.run()

