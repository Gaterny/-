#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author:  Gaterny
# @Github:  https://github.com/Gaterny
# @抓取西刺代理高匿ip,并验证其有效性

from bs4 import BeautifulSoup
import requests
import random

headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
	'(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
def get_ip(url):
	html = requests.get(url, headers=headers).text
	soup = BeautifulSoup(html, 'lxml')
	trs = soup.find_all('tr')
	print(len(trs))
	ip_list = []
	for tr in trs[1:len(trs)+1]:
		ip = tr.find_all('td')[1].text
		#port = tr.find_all('td')[2].text
		ip_list.append(ip)
	ip_check(ip_list)
	#return ip_list
		
def ip_check(ip_list):
	ip_avaliable = []
	for ip in ip_list:
		print('正在验证%r是否可用' %ip)
		try:
			test = requests.get('https://www.baidu.com', proxies={'http': ip}, timeout=10)
			if test.status_code == 200:
				print('------%r验证通过------' %ip)
				ip_avaliable.append(ip)
			else:
				print('******%r验证失效******' %ip)
		except:
			return false
	get_random(ip_avaliable)
	#return ip_avaliable

def get_random(ip_avaliable):
	ip = random.choice(ip_avaliable)
	return ip


if __name__ == '__main__':
	for i in range(1,10):
		url = 'http://www.xicidaili.com/nn/' + str(i)
		get_ip(url)
