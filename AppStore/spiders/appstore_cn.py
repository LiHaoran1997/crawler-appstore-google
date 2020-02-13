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

app_store_home = 'https://apps.apple.com/cn/genre/ios/id36'
# https://doc.scrapy.org/en/latest/topics/spiders.html#crawlspider-example
class AppstoreSpider(CrawlSpider):
    name = 'appstore_cn'
    allowed_domains = ['apps.apple.com']
    start_urls = [app_store_home]

    # proxy = random.choice(proxy_list)
    # header = random.choice(my_headers)
    # custom_settings = {
    #     'LOG_FILE': 'logs/scrapy_%d.log' % random.randrange(10000, 100000),
    # }
    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/genre/ios-', deny=('letter='))),
        Rule(LinkExtractor(allow=('/app/',), deny=('ct=footer',)),callback='parse_item', follow=True),)

    # category is passed from command line argument
    # scrapy crawl appstore -a category=productivity

    def parse_item(self, response):
        self.logger.info('URL: %s', response.url)
        text1_ld = response.xpath(
            '//script[@type="application"]/text()')
        print(text1_ld)
        text_ld = response.xpath(
            '//script[@type="application/ld+json"]/text()')
        json_ld = json.loads(text_ld.extract_first())
        print(json_ld)
        item = AppstoreCrawlerItem_cn()
        item['category'] = json_ld['applicationCategory']
        item['name'] = json_ld['name']
        item['url']=response.url
        # item['subtitle'] = attributes.get('subtitle', '')
        item['description'] = json_ld['description']
        item['date_published'] = json_ld['datePublished']
        item['price_category'] = json_ld['offers'].get('category', '')
        item['price'] = json_ld['offers']['price']
        item['price_currency'] = json_ld['offers']['priceCurrency']
        item['operatingSystem'] = json_ld['operatingSystem']
        item['author_url'] = json_ld['author']['url']
        item['ratingValue'] = json_ld['aggregateRating']['ratingValue']
        item['reviewCount'] = json_ld['aggregateRating']['reviewCount']
        item['author_name'] = json_ld['author']['name']
        # fix &amp; to &

        item["size"] = response.xpath("//dt[text()='大小']/../dd/text()").extract_first()
        item["language"] = response.xpath("//dt[text()='语言']/..//p/text()").extract_first()
        item["age"] = response.xpath("//dt[text()='年龄分级']/../dd/text()").extract_first()
        item["Copyright"] = response.xpath("//dt[text()='Copyright']/../dd/text()").extract_first()
        # item["rank"] = response.xpath('//span[@class="we-customer-ratings__averages__display"]/text()').extract_first()
        item['name'] = html.unescape(item['name'])
        item['category'] = html.unescape(item['category'])
        return item
