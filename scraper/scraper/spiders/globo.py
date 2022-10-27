import scrapy


class GloboSpider(scrapy.Spider):
    name = 'globo'
    allowed_domains = ['globo.com']
    start_urls = ['http://globo.com/']

    def parse(self, response):
        for scraper in response.css('.post__link'):
            yield{
                'manchetes':scraper.css('h2::text').get()
            }
