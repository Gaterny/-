# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem

class CoursePipeline(object):
    def __init__(self):
        self.file = open('mooc.json', 'a', encoding='utf-8')
    def process_item(self, item, spider):
        data = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(data)
        return item
