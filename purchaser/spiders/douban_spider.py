import scrapy
import logging

from purchaser.items import HotSerachItem

logger = logging.getLogger(__name__)


class DoubanSpider(scrapy.Spider):
    name = "douban"
    source = "豆瓣"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "https://movie.douban.com/top250",
    ]

    def parse(self, response, **kwargs):
        logger.debug(response.body.decode("utf-8"))
        horizon = response.css(".Xc-ec-L::text").get().strip().replace(" ", "")
        if response.css("tbody")[0]:
            for tr_dom in response.css("tbody")[0].css("tr"):
                item = HotSerachItem(self.source, horizon)
                item["number"] = tr_dom.css("td").css("td::text").get().replace(".", "")
                item["title"] = tr_dom.css("td")[1].css("a::text").get()
                if tr_dom.css("td")[2].css("td::text").get():
                    item["count"] = tr_dom.css("td")[2].css("td::text").get().replace(" 万热度", "w")
                item["link"] = tr_dom.css("td")[3].css("a::attr(href)").get()
                yield item
        if response.css("tbody")[1]:
            for index, tr_dom in enumerate(response.css("tbody")[1].css("tr")):
                item = HotSerachItem(self.source, horizon + "历史")
                item["number"] = str(index + 1)
                item["title"] = tr_dom.css("td")[1].css("a::text").get()
                if tr_dom.css("td")[2].css("td::text").get():
                    item["count"] = tr_dom.css("td")[2].css("td::text").get().replace(" 万热度", "w")
                item["link"] = tr_dom.css("td")[3].css("a::attr(href)").get()
                yield item
