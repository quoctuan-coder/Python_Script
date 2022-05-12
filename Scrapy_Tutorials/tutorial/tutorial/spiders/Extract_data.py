
import scrapy
# scrapy crawl data -O quotes.json
class ExtractData(scrapy.Spider):
    name = 'data'

    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text':quote.css('span.text::text').get(),
                'author':quote.css('small.author::text').get()
            }