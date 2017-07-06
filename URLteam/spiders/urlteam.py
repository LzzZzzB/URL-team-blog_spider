# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from URLteam.items import UrlteamItem

class URLteamSpider(Spider):
    name = "urlteam"
    download_delay = 1
    allowed_domains = ["urlteam.org"]
    start_urls = [
        "https://www.urlteam.org/2016/06/scrapy%E7%AC%94%E8%AE%B0%E4%B8%89-%E8%87%AA%E5%8A%A8%E5%A4%9A%E7%BD%91%E9%A1%B5%E7%88%AC%E5%8F%96-%E6%9C%ACwordpress%E5%8D%9A%E5%AE%A2%E6%89%80%E6%9C%89%E6%96%87%E7%AB%A0/"
    ]

    def parse(self, response):
        sel = Selector(response)
        item = UrlteamItem()

        article_url = response.url
        article_name = sel.xpath('//h1/text()').extract()

        item['article_name'] = article_name
        item['article_url'] = article_url

        yield item

        urls  = sel.xpath('//div[@class="nav-previous"]/a/@href').extract()


        for url in urls:
            #print (url)
            yield Request(url, callback=self.parse)
