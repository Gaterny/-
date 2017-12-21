# -*- coding:utf-8 -*-
'''
抓取单页内容,得到HTML代码
正则表达式分析
保存至文件
开启循环与多线程
'''
from multiprocessing import Pool
import requests
import re
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400 QQBrowser/9.7.12661.400'}
def get_page(url):
	response = requests.get(url, headers=headers)
	try:
		if response.status_code ==200:
			return response.text
	except:
		return None
def parse_page(html):
	pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?name"><a.*?'
		+ '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?score">.*?integer">'
		+ '(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)   # re.S 匹配任意字符，包括换行符
	items = re.findall(pattern,html)
	for item in items:
		yield {
			'排名':item[0],
			'影名':item[1].strip(),
			'主演':item[2].strip()[3:],
			'上映时间':item[3][5:],
			'评分':item[4]+item[5]
		}

def save_page(item):
	with open('C:/Users/scuso/Desktop/test/test.txt', 'a', encoding='utf-8') as f:
		f.write(json.dumps(item, ensure_ascii=False) + '\n')  #dict transfer to str
		f.close()
def main(offset):
	url = 'http://maoyan.com/board/4?offset=' + str(offset)
	html = get_page(url)
	for item in parse_page(html):
		save_page(item)
		print(item)

if __name__ == '__main__':
	pool = Pool()
	pool.map(main, [i*10 for i in range(10)])
