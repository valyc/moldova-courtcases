# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class CourtcasesPipeline(object):
#     def process_item(self, item, spider):
#         return item


from peewee import *
from moldova_courtcases_db import *
import base64, os
import time

class MysqlStorePipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):    
        case = Courtcase(
            courtName = item['courtName'],
            caseNumber = item['caseNumber'],
            deliveryDate = item['deliveryDate'],
            createdDate = item['createdDate'],
            publishedDate = item['publishedDate'],
            title = item['title'],
            caseType = item['caseType'],
            theme = item['theme'],
            pdfFile = item['pdfFile'],
        )
        case.save();
        return item

class PdfGeneratorPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if item['pdfBase64'] == "" or len(item['pdfBase64']) < 10:
            item['pdfFile'] = ""
            return item
        directory = "files/" + item['courtName']
        if not os.path.exists(directory):
            os.makedirs(directory)        
        item['pdfFile'] = os.path.join(directory, item['caseNumber'].replace("/","-") + str(int(time.time())) + ".html")
        with open(item['pdfFile'],"w") as fout:
            fout.write(base64.decodestring(item['pdfBase64']))
        return item
