# Import the library for this project
import re
import json
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor as sle
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider

class youtube_trendingSpider(Spider):
    name = 'youtube_trending'
    allowed_domains = ['youtube.com']
    start_urls = ['https://www.youtube.com/feed/trending']

    rules = [
        Rule(sle(allow=("feed/trending$")), callback='parse', follow=True),
    ]

    list_css_rules = { 
        '.yt-lockup-content': {
            'video_title': '.yt-lockup-title a::text',
            'author': '.yt-lockup-byline a::text',
        }   
    }

    def parse(self,response):
        title = response.xpath('//*[@id="video-title/text()"]').get()
        print(title)