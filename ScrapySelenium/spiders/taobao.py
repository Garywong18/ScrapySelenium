# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']
    base_url = 'https://s.taobao.com/search?q='

    def start_requests(self):
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            url = self.base_url + quote(self.settings.get('KEYWORDS'))
            yield scrapy.Request(
                url,
                callback=self.parse,
                meta={'page':page},
                dont_filter=True
            )
    def parse(self, response):
        product_list = response.xpath("//div[@id='mainsrp-itemlist']//div[@class='items']/div")
        for product in product_list[1:]:
            item = {}
            item['title'] = ''.join(product.xpath(".//div[contains(@class,'title')]//text()").extract()).strip()
            item['price'] = ''.join(product.xpath(".//div[contains(@class,'price')]//text()").extract()).strip()
            item['deal'] = product.xpath(".//div[contains(@class,'deal-cnt')]//text()").extract_first()
            item['shop'] = product.xpath(".//div[@class='shop']/a/span[2]/text()").extract_first()
            item['location'] = product.xpath(".//div[@class='location']/text()").extract_first()
            yield item