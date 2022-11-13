from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from smartphone_parser.items import VersionItem


class SmartphoneSpider(CrawlSpider):
    name = 'test'
    allowed_domains = ('ozon.ru',)
    start_urls = (
        'https://www.ozon.ru/category/smartfony-15502/?sorting=rating',
        'https://www.ozon.ru/category/smartfony-15502/?page=2&sorting=rating',
        'https://www.ozon.ru/category/smartfony-15502/?page=3&sorting=rating',
        )
    rules = (Rule(LinkExtractor(allow=r'product/smartfon.*'), callback='parse_item'),)
    
    def parse_item(self, response):
        version = response.xpath('//dd/a[text()[re:test(., "iOS\s")]]/text()').get()
        if version is None:
            version = response.xpath('//dd[text()[re:test(., "iOS\s")]]/text()').get()
        if version is None:
            version = response.xpath('//dd[text()[re:test(., "Android\s")]]/text()').get()
        if version is None:
            version = 'Didnt get OC data'
        item = VersionItem()
        item['version'] = version
        item['link'] = response.url
        yield item