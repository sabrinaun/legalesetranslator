
#The purpose of this program is to scrape legal documents for commonly used terms and help users understand them.
#This is the API that will help scrape web-based leasing documents for word choice
import scrapy as scrapy

import os

os.chdir('scrubd')

scrapy startproject tutorial [project_dir]

cd project_dir

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')