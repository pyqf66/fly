# -*- coding: utf-8 -*-
import scrapy
from ..items import FlyItem
import logging


class EnterurlsspiderSpider(scrapy.Spider):
    name = 'EnterUrlsSpider'
    allowed_domains = ['guozhivip.com']
    start_urls = ['http://guozhivip.com/rank/']

    def parse(self, response):
        item = FlyItem()
        urls_l = response.xpath("//div[@class='content']/ul/li/a//@href")
        names_l = response.xpath("//div[@class='content']/ul/li/a//text()")
        for url, name in zip(urls_l, names_l):
            item['enter_urls'] = url.extract()
            item['web_names'] = name.extract()
            yield item