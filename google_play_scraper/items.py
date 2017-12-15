# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GooglePlayScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = Field()
    Link = scrapy.Field()
    Item_name = scrapy.Field()
    Updated = scrapy.Field()
    Author = scrapy.Field()
    Filesize = scrapy.Field()
    Downloads = scrapy.Field()
    Version = scrapy.Field()
    Compatibility = scrapy.Field()
    Content_rating = scrapy.Field()
    Author_link = scrapy.Field()
    Genre = scrapy.Field()
    Price = scrapy.Field()
    Rating_value = scrapy.Field()
    Review_number = scrapy.Field()
    Description = scrapy.Field()
    IAP = scrapy.Field()
    Developer_badge = scrapy.Field()
    Physical_address = scrapy.Field()
    Video_URL = scrapy.Field()
    Developer_ID = scrapy.Field()
    Num_Five_Star_Reviews = scrapy.Field()
    Num_Four_Star_Reviews = scrapy.Field()
    Num_Three_Star_Reviews = scrapy.Field()
    Num_Two_Star_Reviews = scrapy.Field()
    Num_One_Star_Reviews = scrapy.Field()
    Reviews = scrapy.Field()
