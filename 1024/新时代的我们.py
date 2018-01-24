# -*- coding: utf-8 -*-

# @Author:  Gaterny
# @Github:  https://github.com/Gaterny
# @爬取草榴社区新时代的我们板块图片

import requests
import re
import os

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
	'(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
def get_index(index_url):
	res = requests.get(index_url, headers=headers)
	res.encoding = 'gbk'
	html = res.text
	pattern = re.compile(r'<h3>.*?href="(.*?)".*?P]</a></h3>')
	href = re.findall(pattern, html)
	for link in href:
		url = 'https://t66y.com/' + link
		get_url(url)

def get_url(url):
	res = requests.get(url, headers=headers)
	res.encoding = 'gbk'  #这里是因为网页编码是gbk
	html = res.text
	save_img(html)

def save_img(html):
	pattern1 = re.compile(r'<h4>(.*?)</h4>',re.S)
	title = re.findall(pattern1, html)
	pattern2 = re.compile(r"input\ssrc='(.*?)'.*?>&nbsp")
	img_urls = re.findall(pattern2, html)

	root_dir = 'path'  #本地根目录路径
	file_path = root_dir + str(title[0])                 #图集目录路径
	os.mkdir(file_path)

	i = 1
	for img_url in img_urls:
		img = requests.get(img_url, headers=headers).content
		img_name = str(i) + '.jpg'
		with open(file_path + '\\' + img_name, 'wb') as f:
			f.write(img)
			f.close()
			i += 1


if __name__ == '__main__':
	for i in range(20):
		index_url = 'https://t66y.com/thread0806.php?fid=8&search=&page=' + str(i)
		get_index(index_url)
