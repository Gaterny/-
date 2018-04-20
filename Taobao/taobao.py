#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author:  Gaterny
# @Github:  https://github.com/Gaterny
# @selenium和PhantomJS爬取淘宝

# 搜索关键词，得到查询后的商品列表
# 得到商品页码数，模拟翻页
# 利用pyquery分析源码，解析得到商品列表
# 存储到mongodb

import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
from config import *
import pymongo

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


browser = webdriver.Chrome()
#browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
wait = WebDriverWait(browser, 10)
#browser.set_window_size(1400, 900)

def search():
	print('正在搜索')
	try:
		browser.get('https://www.taobao.com')
		inpu = wait.until(
			EC.presence_of_element_located((By.ID, "q"))
		)
		search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
		inpu.send_keys('KEYWORD')
		search.click()
		total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
		get_products()
		return total.text
	except TimeoutException:
		return search()

#网页翻页
def next_page(page_number):
	print('正在翻页', page_number)
	try:
		inpu = wait.until(
				EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
			)
		search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
		inpu.clear()
		inpu.send_keys(page_number)
		search.click()
		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
		get_products()
	except TimeoutException:
		next_page(page_number)

def get_products():
	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
	html = browser.page_source
	doc = pq(html)
	items = doc('#mainsrp-itemlist .items .item').items()
	for item in items:
		product = {
			'image': item.find('.pic .img').attr('src'),
			'price': item.find('.price').text(),
			'deal': item.find('.deal-cnt').text()[:-3],
			'title': item.find('.title').text(),
			'shop': item.find('.shop').text(),
			'location': item.find('.location').text()
		}
		print(product)
		save_to_mongo(product)

def save_to_mongo(result):
	try:
		if db[MONGO_TABLE].insert(result):
			print('存储到数据库成功!', result)
	except Exception:
		print('存储到数据库失败!', result)


def main():
	try:
		total = search()
		total = int(re.compile(r'.*?(\d+).*?').match(total).group(1))
		for i in range(2, total + 1):
			next_page(i)
	except Exception:
		print('出错了！')
	finally:
		browser.close()

if __name__ == '__main__':
	main()
