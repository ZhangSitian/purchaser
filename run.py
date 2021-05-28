from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from purchaser.spiders.baidu_spider import BaiduSpider
from purchaser.spiders.hot_spider import HotSpider
from purchaser.spiders.weibo_spider import WeiboSpider

process = CrawlerProcess(get_project_settings())

process.crawl(BaiduSpider)
process.crawl(HotSpider)
process.crawl(WeiboSpider)

process.start()
