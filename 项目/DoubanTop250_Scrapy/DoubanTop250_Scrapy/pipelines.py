# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from scrapy import signals
from scrapy.exporters import CsvItemExporter

from DoubanTop250_Scrapy.const import DB_CONFIG
from DoubanTop250_Scrapy.utils.mysql_util import MysqlDB


class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('top250.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return ite


    def spider_closed(self, spider):
        self.file.close()


class CSVPipeline(CsvItemExporter):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        savefile = open('douban_top250_export.csv', 'wb+')
        self.files[spider] = savefile
        self.exporter = CsvItemExporter(savefile)

        self.exporter.fields_to_export = [
            'movie_url',
            'movie_picture',
            'movie_name',
            'movie_date',
            'movie_score',
            'movie_num',
            'movie_time',
            'movie_director',
            'movie_actors',
            'movie_type',
            'movie_Introduction',
        ]
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        savefile = self.files.pop(spider)
        savefile.close()

    def process_item(self, item, spider):
        print(type(item))
        self.exporter.export_item(item)
        return item


class MySQLPipeline:
    # 初始化mongodb
    def __init__(self):
        self.db = MysqlDB(**DB_CONFIG)
        self.db.connection()

    def process_item(self, item, spider):
        movie_dict = dict(item)
        if movie_dict and movie_dict.get('movie_name'):

            movie_name = movie_dict.get('movie_name')

            # movie不存在就添加
            sql = "SELECT * FROM douban_movie WHERE movie_name = %s"
            print("========fetch")
            if self.db.fetch_one(sql, (movie_name, )):
                return item
            print("----------insert{}".format(movie_name))
            # 靠它把数据导入数据库
            sql = """     
                INSERT INTO douban_movie(movie_name, movie_date, movie_score, movie_num, movie_time, movie_type, 
                movie_director, movie_actors, movie_url, movie_picture, movie_Introduction) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            content = [
            (
                movie_dict.get('movie_name'), movie_dict.get('movie_date'), movie_dict.get('movie_score'),
                movie_dict.get('movie_num'),
                movie_dict.get('movie_time'), movie_dict.get('movie_type'), movie_dict.get('movie_director'),
                movie_dict.get('movie_actors'),
                movie_dict.get('movie_url'), movie_dict.get('movie_picture'), movie_dict.get('movie_Introduction')
             )
            ]

            res = self.db.execute_many(sql, content)
            print(res)

        return item
