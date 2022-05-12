# How to run: scrapy crawl quotes

import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url = url,callback=self.parse)
    def parse(self, response, **kwargs):
        page = response.url.split('/')[-2]
        fileName = f'quotes-{page}.html'
        with open(fileName,'wb') as file:
            file.write(response.body)
        self.log(f'save file {fileName}')

# ========================================================================
