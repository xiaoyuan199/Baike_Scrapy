# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql

class BaikePipeline(object):
    def process_item(self, item, spider):
        with open(r'E:\python3\mywork\pachong\baike\duanzi.txt','a+') as f:
            f.write("作者：{}\n{}\n点赞：{}\t评论：{}\n\n".format(item['author'].strip(),item['body'],item['funNum'],item['comNum']))
        return item

class Baike2json(object):
    def process_item(self,item,spider):
        # 打开json文件，向里面以dumps的方式吸入数据
        # 注意需要有一个参数ensure_ascii=False ，不然数据会直接为utf编码的方式存入比如:“/xe15”
        with open(r'E:\python3\mywork\pachong\baike\duanzi.json','a+') as f:
            line = json.dumps(dict(item),ensure_ascii=False)+'\n'
            f.write(line)
            
        return item

class Baike2mysql(object):
    def process_item(self,item,spider):
        '''
        将爬取的信息保存到mysql
        '''
        # 将item里的数据拿出来
        author = item['author']
        body = item['body']
        funNum = item['funNum']
        comNum = item['comNum']

        #和本地的scrapyDB数据库建立连接
        connection = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            user='root',        # 自己的mysql用户名
            passwd='',  # 自己的密码
            db='test1',      # 数据库的名字
            charset='utf8mb4',     # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)
            
        try:
            with connection.cursor() as cursor:
                #创建更新值的sql语句
                sql = """insert into duanzi(author,body,funNum,comNum)
                values(%s,%s,%s,%s)
                """
                #执行sql语句
                #excute 的第二个参数可以将sql缺省语句补全，一般以元组的格式
                cursor.execute(sql,(author,body,funNum,comNum))
            #提交本次插入的记录
            connection.commit()
        finally:
            ## 关闭连接
            connection.close()
            
        return item
        
        
        
        