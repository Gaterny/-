# -*- coding: utf-8 -*-
import scrapy


class MzituspiderSpider(scrapy.Spider):
    name = 'mzituspider'
    allowed_domains = ['mzitu.com/']
    start_urls = [
        'http://www.mzitu.com/all/',
    ]

    def parse(self, response):
        items = response.css('.url a')
        for item in items:
            url = item.css('a::attr(href)').extract_first()
            title = item.css('a::text').extract_first()
            print(url, title)  # http://www.mzitu.com/124379 气质女神杨晨晨肤白貌美人见人爱
