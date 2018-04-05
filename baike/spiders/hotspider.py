# -*- coding: utf-8 -*-
import scrapy
from baike.items import BaikeItem

class HotspiderSpider(scrapy.Spider):
    name = "hotspider"
    allowed_domains = ["qiushibaike.com"]
    start_urls = []
    for i in range(1,14):
        start_urls.append('http://www.qiushibaike.com/8hr/page/'+str(i)+'/')
        

    def parse(self, response):
        item = BaikeItem()
        
        # 找到热门段子主体
        main = response.xpath('//div[@id="content-left"]/div')
        
        for div in main:
             item['author'] = div.xpath('.//h2/text()').extract()[0].strip()
             #段子主体： 
             item['body'] = ''.join( div.xpath('.//div[@class="content"]/span[1]/text()').extract()).strip()
             #段子footer
             item['funNum']= div.xpath('.//span[@class="stats-vote"]/i/text()').extract()[0]
             item['comNum']= div.xpath('.//span[@class="stats-comments"]/a/i/text()').extract()[0]
             yield item
