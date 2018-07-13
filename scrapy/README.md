#### scrapy记录

###### 运行scrapy

```
scrapy runspider mingyanSpider.py -o mingyan.json   # 输出结果为json
scrapy crawl [项目名]  # cd到项目目录下执行
scrapy crawl [项目名] -a tag=[参数名]   # 传参
```

###### scrapy安装

```
windows:
	pip install scrapy

linux:
	sudo apt-get install python-pip
	pip install --upgrade pip
	pip install scrapy
	
scrapy version  # 查看scrapy版本
```

###### 创建项目

```
scrapy startproject [projectname]
spiders下创建spider文件就好了
```

###### 初始url简化

```
"""
    scrapy初始Url的两种写法，
    一种是常量start_urls，并且需要定义一个方法parse（）
    另一种是直接定义一个方法：star_requests()
"""
import scrapy
class simpleUrl(scrapy.Spider):
    name = "simpleUrl"
    start_urls = [  #另外一种写法，无需定义start_requests方法
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]
    # 另外一种初始链接写法
    # def start_requests(self):
    #     urls = [ #爬取的链接由此方法通过下面链接爬取页面
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # 如果是简写初始url，此方法名必须为：parse

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mingyan-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s' % filename)
```

###### scrapy调试工具

```
scrapy shell http://www.example.com   # 获取相应的界面，返回response
```
```
>>> scrapy shell https://www.baidu.com
>>> response.css('title')
 [<Selector xpath='descendant-or-self::title' data='<title>爬虫实验室 - SCRAPY中文网提供</title>'>]

>>> response.css('title').extract()
>>> ['<title>百度一下，你就知道</title>']

>>> response.css('title').extract_first()
>>> '<title>百度一下，你就知道</title>'

>>> response.css('title').extract()[0]
>>> '<title>百度一下，你就知道</title>'

>>> response.css('title::text').extract_first()  # 提取第一个元素，::text表示提取标签里面的数据
>>> '百度一下，你就知道'
```
###### 组件介绍

```
items:
	定义爬取的字段，用来存放爬取的信息
pipeline:
	中间件，把spider获取的连接执行下载
settings:
	定义设置，包括存储位置等
middleware:
	反爬措施
```


