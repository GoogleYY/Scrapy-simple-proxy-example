# -*- coding: utf-8 -*-
import scrapy

# Enable proxy middleware in settings.py. by uncommenting DOWNLOADER_MIDDLEWARES and add user-agent in it
# Add proxy ip within process_request function in middleware.py
class BotSpider(scrapy.Spider):
    name = 'bot'
    start_urls = ['https://dictionary.cambridge.org/dictionary/english-chinese-simplified/test',]
    # request.meta['proxy'] = "http://162.243.107.45:3128"

    def parse(self, TextResponse):
        with open(".//output.html", "a+", encoding="UTF-8", newline='') as text_file:
            print(f"{TextResponse.text}", file=text_file)
