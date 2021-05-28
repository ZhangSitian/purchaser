import scrapy
import logging

from purchaser.enums import NewsStatus
from purchaser.items import HotSerachItem

logger = logging.getLogger(__name__)


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    source = "百度"
    allowed_domains = ["top.baidu.com"]
    start_urls = [
        "http://top.baidu.com/buzz?b=1&fr=topindex",
        "http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b1",
        "http://top.baidu.com/buzz?b=42&c=513&fr=topbuzz_b341_c513"
    ]

    def parse(self, response, **kwargs):
        logger.debug(response.body.decode("gb2312"))
        horizon = self.source + response.css(".hblock .se::text").get()
        if horizon:
            for tr_dom in response.css("table.list-table tr"):
                title = tr_dom.css(".list-title::text").get()
                if title:
                    item = HotSerachItem(self.source, horizon)
                    item["number"] = tr_dom.css(".num-top::text,.num-normal::text").get()
                    item["title"] = tr_dom.css(".list-title::text").get()
                    item["count"] = tr_dom.css(".icon-fall::text,.icon-rise::text,.icon-fair::text").get()
                    if tr_dom.css(".icon.icon-new").get():
                        item["news_status"] = NewsStatus.NEW.value
                    elif tr_dom.css(".icon-rise").get():
                        item["news_status"] = NewsStatus.HOT.value
                    item["link"] = tr_dom.css(".list-title::attr(href)").get()
                    yield item
