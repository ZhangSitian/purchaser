import scrapy
import logging

from purchaser.items import HotSerachItem

logger = logging.getLogger(__name__)


class HotSpider(scrapy.Spider):
    name = "hot"
    source = "热榜"
    allowed_domains = ["tophub.today"]
    start_urls = [
        # 知乎
        "https://tophub.today/n/mproPpoq6O",
        # 微信
        "https://tophub.today/n/WnBe01o371",
        # 澎湃
        "https://tophub.today/n/wWmoO5Rd4E",
        # 百度
        "https://tophub.today/n/Jb0vmloB1G",
        # # bilibili
        # "https://tophub.today/n/74KvxwokxM",
        # # 知乎日报
        # "https://tophub.today/n/KMZd7VOvrO",
        # # 36Kr
        # "https://tophub.today/n/Q1Vd5Ko85R",
        # # 吾爱破解
        # "https://tophub.today/n/NKGoRAzel6",
        # # 好奇心日报
        # "https://tophub.today/n/Y3QeLGAd7k",
        # # 少数派
        # "https://tophub.today/n/Y2KeDGQdNP",
        # 雪球
        "https://tophub.today/n/X12owXzvNV",
        # 第一财经
        "https://tophub.today/n/0MdKam4ow1",
        # 财新网
        "https://tophub.today/n/3QeLGVPd7k",
        # 新浪财经新闻
        "https://tophub.today/n/rx9ozj7oXb",
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
