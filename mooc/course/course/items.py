# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # course name
    name = scrapy.Field()
    # course url
    url = scrapy.Field()
    # course image
    img_url = scrapy.Field()
    # course description
    description = scrapy.Field()
    # study nummber
    number = scrapy.Field()
    # category
    category = scrapy.Field()
