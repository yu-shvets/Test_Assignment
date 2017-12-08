import scrapy

#Scrapy spider
class ProxiesSpider(scrapy.Spider):
    name = "proxies"
    start_urls = ['http://spys.one/proxies/']

    def parse(self, response):
        for proxy in response.css('table tr'):
            yield {
                'host': proxy.css('font.spy14::text').extract_first()
            }

