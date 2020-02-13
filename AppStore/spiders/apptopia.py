# -*- coding: utf-8 -*-
import os
import json
import html
import random
import urllib.parse
import urllib.request
from scrapy import signals
import random
import requests
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from AppStore.items import AppstoreCrawlerItem_cn,AppstoreCrawlerItemLoader_cn
from tqdm import tqdm
import re

app_store_home = 'https://apptopia.com/store-insights/top-charts/itunes-connect'
# https://doc.scrapy.org/en/latest/topics/spiders.html#crawlspider-example
class AppstoreSpider(CrawlSpider):
    name = 'apptopia'
    allowed_domains = ['apptopia.com']
    start_urls = [app_store_home]

    # proxy = random.choice(proxy_list)
    # header = random.choice(my_headers)
    # custom_settings = {
    #     'LOG_FILE': 'logs/scrapy_%d.log' % random.randrange(10000, 100000),
    # }
    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('https://apptopia.com/store-insights/top-charts/itunes-connect',)),callback='parse_item', follow=False),)

    # category is passed from command line argument
    # scrapy crawl appstore -a category=productivity

    def parse_item(self, response):
        self.logger.info('URL: %s', response.url)
        text1_ld = response.css('div.table-responsive.pos-rel > table > tbody ').extract()
        print(text1_ld)
        text_ld = response.xpath(
            '//script[@type="application/ld+json"]/text()')
        json_ld = json.loads(text_ld.extract_first())
        print(json_ld)
        item = AppstoreCrawlerItem_cn()

        return item
