import scrapy


class ScrapSpider(scrapy.Spider):
    name = 'scrap'
    allowed_domains = ['myanimelist.netscramyan']
    start_urls = ['https://myanimelist.net/topanime.php?type=airing']

    def parse(self, response):
        for scraper in response.css(".ranking-list"):
            yield {
                'classificacao':scraper.css("span::text").extract_first(),
                'titulo':scraper.css("h3 a::text").extract_first(),
            } 
        

