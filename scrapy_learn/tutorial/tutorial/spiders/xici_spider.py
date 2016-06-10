#_*_coding:utf-8 _*_
__author__ = 'sylar'

import scrapy
from tutorial.items import xcdlItem

class xcdl(scrapy.Spider):
    name = 'xcdl'
    allowed_domains = ['xicidaili.com']   #限制爬虫的网址
    start_urls = [
        'http://www.xicidaili.com/nn/',
        'http://www.xicidaili.com/nt/',
        'http://www.xicidaili.com/wn/',
        'http://www.xicidaili.com/wt/'
    ]
    def parse(self,response):  #还需要去除response的空格和回车
        '''
        sel = scrapy.Selector(response)  #将response导入选择器.以免数据太大.做异步处理



        sites = sel.xpath('//td/text()').extract()
        items = []

        for i in sites:

            item = xcdlItem()
            item['ip'] = sites[0]
            item['port'] = sites[1]
            item['addr'] = sites[2]
            item['protocol'] = sites[4]
            del sites[:6]
            items.append(item)
        return items
        '''
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)











