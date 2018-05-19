# -*- coding: utf-8 -*-
import scrapy
from course.items import CourseItem

class MoocSpider(scrapy.Spider):
    name = 'mooc'
    allowed_domains = ['imooc.com']
    start_urls = ['http://www.imooc.com/course/list']

    def parse(self, response):
        item = CourseItem()
        for items in response.xpath('//div[@class="course-card-container"]'):
            item['name'] = items.xpath('.//h3[@class="course-card-name"]/text()').extract()[0].strip()
            item['url'] = 'http://www.imooc.com' + items.xpath('.//@href').extract()[0]
            item['img_url'] = 'http:' + items.xpath('.//@src').extract()[0]
            item['description'] = items.xpath('.//p[@class="course-card-desc"]/text()').extract()[0].strip()
            item['number'] = items.xpath('.//span/text()').extract()[1].strip()
            yield item

        # acquire next page url
        url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
        if url:
            page_url = 'http://www.imooc.com' + url[0]
            yield scrapy.Request(page_url, callback=self.parse)
