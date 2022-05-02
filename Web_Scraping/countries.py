import scrapy

class CountriesSpider(scrapy.Spider):
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        