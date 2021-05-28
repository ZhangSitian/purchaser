# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging

logger = logging.getLogger(__name__)


class BaiduCurrentHotSearchPipeline(object):

    def __init__(self):
        self.files = {}

    def process_item(self, item, spider):
        file = item["horizon"]
        if file not in self.files:
            self.files[file] = open("log/%s.jl" % file, 'w', encoding="utf-8")
        self.files[file].write(item.to_json_string_line())
        return item

    def close_spider(self, spider):
        for i in self.files:
            self.files[i].close()
        logger.info("HotSearchPipeline结束")
