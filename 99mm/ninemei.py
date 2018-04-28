#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author:  Gaterny
# @Github:  https://github.com/Gaterny

import os 
import random
import requests
from bs4 import BeautifulSoup

class Ninemei():

	'''构造requests请求，返回response对象'''
	def request(self, url):
		headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
		response = requests.get(url, headers=headers)
		response.encoding = 'utf-8'
		return response

	def dirpath(self, path):
		path =path.strip()
		filename = os.path.join("D:\99mm", path)
		print('正在创建', path)
		if not os.path.exists(filename):
			os.makedirs(filename)
			os.chdir(filename)
			return True
		else:
			print('已存在',path,'目录')
			return False

	def all_url(self, url):
		html = self.request(url)
		all_urls = BeautifulSoup(html.text, 'lxml').find('ul', id='piclist').find_all('dd')
		#url_list = []
		for d in all_urls:
			a = d.find_all('a')
			for url in a:
				title = url.get_text()
				# print(title)				
				# print(url['href'])
				path = str(title)
				if not self.dirpath(path):
					print('跳过目录：', title)
					continue
				href = url['href']
				urls = 'http://www.99mm.me/' + href
				self.detail_url(urls)

	def detail_url(self,urls):
		html = self.request(urls)
		page_num = BeautifulSoup(html.text,'lxml').find('div', class_='column').find('span').get_text().replace('.P','').strip()
		print(page_num,'张')
		for num in range(1, int(page_num) + 1):
			short_url = urls + '?url='
			page_url = short_url + str(num)
			self.img(page_url, short_url, num)

	def img(self, page_url,short_url, num):
		html = self.request(page_url)
		src = BeautifulSoup(html.text, 'lxml').find_all('script', type='text/javascript')[-2].get_text()[12:].split('%')
		img_url =  'http://img.99mm.net/{}/{}/'.format(src[4], src[5]) + str(num) + '-{}.jpg'.format(src[num + 7].replace("';", '').lower())
		refer_url = short_url + str(num-1)
		self.save_img(img_url, refer_url, num)

	def save_img(self, img_url, refer_url, num):
		name = str(num)
		try:
			imgs = self.requestpic(img_url, Referer=refer_url).content
			f = open(name + '.jpg', 'ab')
			f.write(imgs)
			f.close()
		except FileNotFoundError as e:
			print('图片找不到，跳过', img_url)
			return False

	def requestpic(self, url, Referer): ##这个函数获取网页的response 然后返回
		user_agent_list = [ \
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
			"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
		]
		ua = random.choice(user_agent_list)
		headers = {'User-Agent': ua,"Referer":Referer} ##较之前版本获取图片关键参数在这里
		response = requests.get(url, headers=headers)
		response.encoding = 'utf-8'
		return response			

if __name__ == '__main__':
	Ninemei = Ninemei()
	for i in range(1, 69):
		if i <= 1:
			Ninemei.all_url('http://www.99mm.me/') 
		else:
			url = 'http://www.99mm.me/hot/mm_4_' + str(i) + '.html'
			Ninemei.all_url(url)
