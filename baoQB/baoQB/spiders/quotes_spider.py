import scrapy

from baoQB.items import QuoteItem


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'tocao'
    start_urls = [
         #'http://quotes.toscrape.com/',
        'https://kenh14.vn/toan-canh-le-an-hoi-hoa-hau-do-my-linh-co-dau-chu-re-ngot-ngao-quy-tu-dan-my-nhan-viet-20221017191143053.chn',
    ]
    def parse(self, response):
        item = QuoteItem()
        item['title']=response.xpath("//h1[@class='kbwc-title']/text()").get()
        item['content']=response.xpath("//div[@class='knc-content']/p[1]/text()").getall(),
        item['dateup']=response.xpath("//span[@class='kbwcm-time']/text()").getall(),
        item['img']=response.xpath(".//img/@src").get(),
        # title = response.xpath("//h1[@class='kbwc-title']/text()").get()
        # content = response.xpath("//div[@class='knc-content']/p[1]/text()").getall(),
        # Date = response.xpath("//span[@class='kbwcm-time']/text()").getall(),
        # Img = response.xpath(".//img/@src").get(),


        yield item