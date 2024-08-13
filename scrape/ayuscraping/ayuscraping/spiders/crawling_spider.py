from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = 'mycrawl'
    allowed_domains = ['daraz.com.np']
    start_urls = ['https://www.daraz.com.np/']

    rules = (
        Rule(LinkExtractor(allow=r'categories'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.logger.info(f'Parsing page: {response.url}')
        # Add your parsing logic here
