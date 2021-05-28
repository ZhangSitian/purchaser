# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from enum import Enum


class NewsStatus(Enum):
    DEFAULT = "DEFAULT"
    NEW = "NEW"
    RECOMMEND = "RECOMMEND"
    HOT = "HOT"
    BOIL = "BOIL"
