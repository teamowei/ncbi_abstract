# -*- coding: utf-8 -*-
import scrapy
from ncbi_abstract.items import NcbiAbstractItem
import ncbi_abstract.openxl

class AbstractSpider(scrapy.Spider):
    name = 'abstract'
    allowed_domains = ['NCBI.com']
    start_urls =ncbi_abstract.openxl.getOpenxls()

    def parse(self, response):
        def parse(self, response):
            item = NcbiabstractItem()
            infos = response.xpath('//div[@class="rprt abstract"]')
            item['article_abstract'] = infos.xpath('./div[@class="abstr"]/text()').all().extract()[0]
            item['pmid'] = infos.xpath('./div[@class="aux"]/div[@class="resc"]/dl/dd/text()').extract()[0]
            item['article_name'] = infos.xpath('./h1/text()').extract()[0]

            yield item
