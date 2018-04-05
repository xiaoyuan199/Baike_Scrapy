# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:44:55 2018

@author: Administrator
"""

'''
自定义scrapy框架的
user-agent头
从一个被良好维护的user-agent列表里
随机筛选合适的user-agent 
防止封锁

这样就能每次发起访问请求的时候，随机选择一个user-agent了。
当然，我们需要在settings.py里激活我们的下载中间件：
'''

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

import random

#一个不容易被封锁的user-agent列表
agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']

class RandomUserAgent(UserAgentMiddleware):
    
    def process_request(self,request,spider):
        '''
        定义下载中间件，
        必须要写这个函数，
        这是scrapy数据流转的一个环节
        具体可以看文档:
        http://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/downloader-middleware.html
        '''
        ua = random.choice(agents)
        request.headers.setdefault('User-agent',ua)









