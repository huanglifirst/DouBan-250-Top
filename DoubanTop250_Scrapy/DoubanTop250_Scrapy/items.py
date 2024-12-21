# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class DoubanTop250Item(scrapy.Item):
#     rank = scrapy.Field()
#     score = scrapy.Field()
#     title_CN = scrapy.Field()
#     title_EN = scrapy.Field()
#     url = scrapy.Field()
#     detail = scrapy.Field()
#     pass
class DoubanTop250Item(scrapy.Item):
    movie_url = scrapy.Field()
    movie_picture = scrapy.Field()
    movie_name = scrapy.Field()
    movie_date = scrapy.Field()
    movie_score = scrapy.Field()
    movie_num = scrapy.Field()
    movie_time = scrapy.Field()
    movie_director = scrapy.Field()
    movie_actors = scrapy.Field()
    movie_type = scrapy.Field()
    movie_Introduction = scrapy.Field()
    news_id = scrapy.Field()
