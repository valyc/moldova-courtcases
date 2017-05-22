# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class CourtcasesItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class CourtcasesItem(scrapy.Item):
    courtName = scrapy.Field()
    caseNumber = scrapy.Field()
    deliveryDate = scrapy.Field()
    createdDate = scrapy.Field()
    publishedDate = scrapy.Field()
    title = scrapy.Field()
    caseType = scrapy.Field()
    theme = scrapy.Field()
    pdfFile = scrapy.Field()
    pdfBase64 = scrapy.Field()