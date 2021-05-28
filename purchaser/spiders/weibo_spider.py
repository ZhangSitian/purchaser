import scrapy
import logging

from purchaser.enums import NewsStatus
from purchaser.items import HotSerachItem

logger = logging.getLogger(__name__)


class WeiboSpider(scrapy.Spider):
    name = "weibo"
    source = "微博"
    allowed_domains = ["s.weibo.com"]
    start_urls = [
        "https://s.weibo.com/top/summary?cate=realtimehot",
        "https://s.weibo.com/top/summary?cate=socialevent"
    ]

    def parse(self, response, **kwargs):
        logger.warning(response.body.decode("utf-8"))
        horizon = self.source + response.css(".menu .cur::text").get()
        for index, tr_dom in enumerate(response.xpath("//tbody/tr")):
            item = HotSerachItem(self.source, horizon)
            if tr_dom.css(".td-01 .icon-dot").get():
                item["number"] = str(index + 1)
            else:
                item["number"] = tr_dom.css(".td-01::text").get()
            if not item["number"]:
                item["number"] = "0"
            item["title"] = tr_dom.css(".td-02 a::text").get().replace("#", "")
            if tr_dom.css(".td-02 span::text").get():
                item["count"] = tr_dom.css(".td-02 span::text").get()
            if tr_dom.css(".icon-txt-new").get():
                item["news_status"] = NewsStatus.NEW.value
            if tr_dom.css(".icon-txt-recommend").get():
                item["news_status"] = NewsStatus.RECOMMEND.value
            if tr_dom.css(".icon-txt-hot").get():
                item["news_status"] = NewsStatus.HOT.value
            if tr_dom.css(".icon-txt-boil").get():
                item["news_status"] = NewsStatus.BOIL.value
            if tr_dom.css(".td-02 .face::attr(title)").get():
                item["emoji"] = tr_dom.css(".td-02 .face::attr(title)").get()
            if tr_dom.css(".td-02 a::attr(href_to)").get():
                item["link"] = "https://s.weibo.com" + tr_dom.css(".td-02 a::attr(href_to)").get()
            else:
                item["link"] = "https://s.weibo.com" + tr_dom.css(".td-02 a::attr(href)").get()
            yield item
