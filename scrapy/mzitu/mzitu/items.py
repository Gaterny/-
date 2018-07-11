# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MzituItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义想要抓取的字段
    title = scrapy.Field()
    img_url = scrapy.Field()
    url = scrapy.Field()

