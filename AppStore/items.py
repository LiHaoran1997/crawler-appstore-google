# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class AppstoreCrawlerItemLoader_cn(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()

class AppstoreCrawlerItem_cn(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    date_published = scrapy.Field()
    price_category = scrapy.Field()
    price = scrapy.Field()
    price_currency = scrapy.Field()
    author_name = scrapy.Field()
    author_url = scrapy.Field()
    size=scrapy.Field()
    language=scrapy.Field()
    age=scrapy.Field()
    Copyright=scrapy.Field()
    # commentCount=scrapy.Field()
    # star=scrapy.Field()
    rank=scrapy.Field()
    operatingSystem=scrapy.Field()
    ratingValue=scrapy.Field()
    reviewCount=scrapy.Field()
    def get_insert_sql(self):
        insert_sql = """
             insert into app(name,category,url,description,date_published,price_category,price,price_currency,author_name,author_url,size,language,age,Copyright,operatingSystem,ratingValue,reviewCount)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
        """
        params = (self['name'], self['category'], self['url'], self['description'],self['date_published'], self['price_category'], self['price'],self['price_currency'], self['author_name'], self['author_url'],self['size'], self['language'], self['age'],self['Copyright'], self['operatingSystem'], self['ratingValue'],self['reviewCount'])
        return insert_sql, params

class QimaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'qimai_rank'

    rank = scrapy.Field()
    app_id = scrapy.Field()
    app_name = scrapy.Field()
    app_country = scrapy.Field()
    url=scrapy.Field()
    price = scrapy.Field()
    developer_name = scrapy.Field()
    comment_num = scrapy.Field()
    rating = scrapy.Field()
    company_id = scrapy.Field()
    company_name = scrapy.Field()
    update_time = scrapy.Field()
    category=scrapy.Field()
    subcategory=scrapy.Field()
