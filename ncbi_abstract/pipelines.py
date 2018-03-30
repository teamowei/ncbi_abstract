# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NcbiAbstractPipeline(object):
    def process_item(self, item, spider):
        with open(str(item["pmid"].encode("utf-8").decode())+".txt",'a') as fp:
            fp.write(item["article_name"].encode('utf-8').decode()+"\n"+item["article_abstract"].encode('utf-8').decode())
