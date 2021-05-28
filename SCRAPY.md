# SCRAPY

## 爬取数据
        scrapy crawl baidu
        scrapy crawl weibo
        scrapy crawl hot

## 调试
### BaiduSpider
        scrapy shell "http://top.baidu.com/buzz?b=1&fr=topindex"
        item_table = response.css("table.list-table")
        item_tr = response.css("table.list-table tr")
        item_hideline = response.css("table.list-table .hideline")
        
        
### WeiboSpider
        scrapy shell "https://s.weibo.com/top/summary?cate=realtimehot"
        response.xpath("//tbody/tr").css(".td-02 a::attr(href)")

        
        
        http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b341_c513
        http://top.baidu.com/buzz?b=42&c=513&fr=topbuzz_b341_c513
    
爬取数据导出到json文件
        scrapy crawl baidu -o items.json


## Selector语法
xpath
.css
.attrib
.get
.getall
get(default='not-found')

  