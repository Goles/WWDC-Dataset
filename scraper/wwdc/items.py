# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WWDCNoTranscriptItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    abstract = scrapy.Field()
    code = scrapy.Field()
    tags = scrapy.Field()
    year = scrapy.Field()
    hd_video = scrapy.Field()
    sd_video = scrapy.Field()
    slides = scrapy.Field()
    pass

class WWDCItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    abstract = scrapy.Field()
    code = scrapy.Field()
    tags = scrapy.Field()
    year = scrapy.Field()
    hd_video = scrapy.Field()
    sd_video = scrapy.Field()
    slides = scrapy.Field()
    transcript = scrapy.Field()
    pass

