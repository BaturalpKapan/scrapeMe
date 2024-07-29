import scrapy


class NbaplayersSpider(scrapy.Spider):
    name = "nbaPlayers"
    allowed_domains = ["hashtagbasketball.com"]
    start_urls = ["https://hashtagbasketball.com/fantasy-basketball-rankings"]

    def parse(self, response):
        pass
