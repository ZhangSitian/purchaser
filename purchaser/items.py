# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json


class HotSerachItem(scrapy.Item):
    # 来源
    source = scrapy.Field()
    # 时间段
    horizon = scrapy.Field()
    # 类别
    type = scrapy.Field()
    # 编号
    number = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 描述
    desc = scrapy.Field()
    # 关注数
    count = scrapy.Field()
    # 新闻状态
    news_status = scrapy.Field()
    # 表情
    emoji = scrapy.Field()
    # 链接
    link = scrapy.Field()
    # 图片
    picture = scrapy.Field()

    def __init__(self, source, horizon):
        super().__init__()
        self["source"] = source
        self["horizon"] = horizon

    def to_json_string_line(self):
        item_json_str = json.dumps(dict(self), ensure_ascii=False)
        item_json = json.loads(item_json_str)
        item_json.pop("source")
        item_json.pop("horizon")
        item_json_str = json.dumps(item_json, ensure_ascii=False)
        return item_json_str + "\n"
