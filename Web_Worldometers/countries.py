import re
import scrapy

class CountriesSpider():
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.name = 'countries'
        self.allowed_domains = ['www.worldometers.info/']
        self.start_urls = 'https://www.worldometers.info/world-population/population-by-country/'
        self.response = scrapy.Request(self.start_urls) 

    def parse(self):
        title = self.response.xpath('//h1/text()').get()
        countries  = self.response.xpath('//td/a/text()').getall()
        
        for country in countries:
            name = country
            print(name)


objCountry = CountriesSpider()
objCountry.parse()
