# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from courtcases.items import CourtcasesItem

# list of urls from http://instante.justice.md/

class CasesSpider(CrawlSpider):
    name = "Cases"
    start_urls =["http://cac.instante.justice.md/ro/hot",
                "http://jc.instante.justice.md/ro/hot",
                "http://jcm.instante.justice.md/ro/hot",
                "http://jcr.instante.justice.md/ro/hot",
                "http://jhn.instante.justice.md/ro/hot",
                "http://jor.instante.justice.md/ro/hot",
                "http://jst.instante.justice.md/ro/hot",
                "http://jan.instante.justice.md/ro/hot",
                "http://jcs.instante.justice.md/ro/hot",
                "http://cab.instante.justice.md/ro/hot",
                "http://jbl.instante.justice.md/ro/hot",
                "http://jdr.instante.justice.md/ro/hot",
                "http://jed.instante.justice.md/ro/hot",
                "http://jsr.instante.justice.md/ro/hot",
                "http://jun.instante.justice.md/ro/hot",
                "http://cach.instante.justice.md/ro/hot",
                "http://jch.instante.justice.md/ro/hot",
                "http://cacm.instante.justice.md/ro/hot",
                "http://jco.instante.justice.md/ro/hot",]

                    # "http://www.jbt.instante.justice.md/ro/hot",
                    # "http://www.jbu.instante.justice.md/ro/hot",
                    # "http://www.jci.instante.justice.md/ro/hot",
                    # "http://www.jcn.instante.justice.md/ro/hot",
                    # "http://www.jrsc.instante.justice.md/ro/hot",
                    # "http://www.jbs.instante.justice.md/ro/hot",
                    # "http://www.jcl.instante.justice.md/ro/hot",
                    # "http://www.jcm.instante.justice.md/ro/hot",
                    # "http://www.jcr.instante.justice.md/ro/hot",
                    # "http://www.jhn.instante.justice.md/ro/hot",
                    # "http://www.jil.instante.justice.md/ro/hot",
                    # "http://www.jnd.instante.justice.md/ro/hot",
                    # "http://www.jor.instante.justice.md/ro/hot",
                    # "http://www.jrz.instante.justice.md/ro/hot",
                    # "http://www.jst.instante.justice.md/ro/hot",
                    # "http://www.jan.instante.justice.md/ro/hot",
                    # "http://www.jcs.instante.justice.md/ro/hot",
                    # "http://www.jdb.instante.justice.md/ro/hot",
                    # "http://www.jgr.instante.justice.md/ro/hot",
                    # "http://www.jsv.instante.justice.md/ro/hot",
                    # "http://www.jbe.instante.justice.md/ro/hot",
                    # "http://www.jec.instante.justice.md/ro/hot",
                    # "http://www.jmi.instante.justice.md/ro/hot",
                    # "http://cab.instante.justice.md/ro/hot",
                    # "http://www.jbl.instante.justice.md/ro/hot",
                    # "http://www.jbr.instante.justice.md/ro/hot",
                    # "http://www.jdn.instante.justice.md/ro/hot",
                    # "http://www.jdr.instante.justice.md/ro/hot",
                    # "http://www.jed.instante.justice.md/ro/hot",
                    # "http://www.jfl.instante.justice.md/ro/hot",
                    # "http://www.jfr.instante.justice.md/ro/hot",
                    # "http://www.jgl.instante.justice.md/ro/hot",
                    # "http://www.joc.instante.justice.md/ro/hot",
                    # "http://www.jrsr.instante.justice.md/ro/hot",
                    # "http://www.jsg.instante.justice.md/ro/hot",
                    # "http://www.jsr.instante.justice.md/ro/hot",
                    # "http://www.jsd.instante.justice.md/ro/hot",
                    # "http://www.jtl.instante.justice.md/ro/hot",
                    # "http://www.jun.instante.justice.md/ro/hot",
                    # "http://cach.instante.justice.md/ro/hot",
                    # "http://www.jch.instante.justice.md/ro/hot",
                    # "http://www.jcnt.instante.justice.md/ro/hot",
                    # "http://www.jlv.instante.justice.md/ro/hot",
                    # "http://www.jtrc.instante.justice.md/ro/hot",
                    # "http://cacm.instante.justice.md/ro/hot",
                    # "http://www.jco.instante.justice.md/ro/hot",
                    # "http://www.jcdl.instante.justice.md/ro/hot",
                    # "http://www.jvl.instante.justice.md/ro/hot"]
    rules = (
        # Extract links for next pages
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//li[contains(@class, "pager-next")]/a')), follow=True, callback='parse_listings'),
    )

    def parse_start_url(self, response):
        '''
        Crawl start URLs
        '''
        return self.parse_listings(response)    

    def parse_listings(self, response):
        sel = Selector(response)
        decisions = sel.xpath('//table/tbody/tr')
        courtName = sel.xpath('//h2[contains(@class,"site-name")]/a/text()').extract()[0].strip()
        for decision in decisions:
            item = CourtcasesItem()
            item['courtName'] = courtName
            item['caseNumber'] = decision.xpath('.//td[contains(@class, "views-field views-field-solr-document-4")]/text()').extract()[0].strip()
            item['deliveryDate'] = decision.xpath('.//td[@class="views-field views-field-solr-document"]/text()').extract()[0].strip()
            # taking [1] as xpath returns all the td elements, my guess is the class-name contains "views-field-solr-document" in other names as well
            item['createdDate'] = decision.xpath('.//td[contains(@class, "views-field views-field-solr-document-2")]/text()').extract()[0].strip()
            item['publishedDate'] = decision.xpath('.//td[contains(@class, "views-field views-field-solr-document-3")]/text()').extract()[0].strip()
            item['title'] = decision.xpath('.//td[contains(@class, "views-field views-field-solr-document-5")]/text()').extract()[0].strip()
            item['caseType'] = decision.xpath('.//td[contains(@class, "views-field views-field-solr-document-6")]/text()').extract()[0].strip()
            item['theme'] = decision.xpath('.//td[contains(@class, "views-field views-field-solr-document-7")]/text()').extract()[0].strip()
            item['pdfBase64'] = decision.xpath('.//td[contains(@class, "views-field views-field-base-url")]/form/input/@value').extract()[0].strip()
            yield item
