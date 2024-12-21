# -*- coding: utf-8 -*-
import re
import scrapy

from DoubanTop250_Scrapy.items import DoubanTop250Item


class Top250Spider(scrapy.Spider):
    name = 'Top250'
    start_urls = []

    base_url = 'https://movie.douban.com/top250?start=%i' + '&filter='
    for i in range(0, 10):
        i = i * 25
        start_urls.append(base_url % i)

    # print(start_urls)

    def parse(self, response):
        '''
        请求第一个页面，获取每个电影的url链接
        :param response:
        :return:
        '''
        # 获取每个页面中的每个电影的url
        all_urls = response.xpath('//ol[@class="grid_view"]/li/div/div[1]/a/@href').extract()

        # 发送二次请求
        for url in all_urls:
            yield scrapy.Request(url, callback=self.parse_detail, encoding='utf-8')

    def parse_detail(self, response):
        '''
        解析详情页，获取信息
        :param response:
        :return:
        '''
        # 电影连接
        movie_url = response.url
        # 图片链接
        movie_picture = response.xpath('//div[@id="mainpic"]/a/img/@src').extract_first()  # 直接获取到列表中的字段
        # 电影名称

        movie_name = response.xpath('//h1/span/text()').extract_first()
        movie_name = movie_name.split(" ")[0].strip()

        # 电影上映时间
        movie_date = response.xpath('//h1/span[2]/text()').extract_first().replace('(', '')
        movie_date = movie_date.replace(')', '')

        # 导演
        movie_director = response.xpath('//div[@id="info"]/span[1]/span[2]/a/text()').extract_first()

        # 主演
        movie_actors = response.selector.re(r'rel="v:starring">(.*?)</a>', re.S)
        movie_actors = ','.join(movie_actors)

        # 类型
        movie_types = response.xpath('//div[@id="info"]/span[@property="v:genre"]/text()').extract()
        movie_type = ','.join(movie_types)

        # 电影时长
        movie_time = response.xpath('//*[@id="info"]/span[@property="v:runtime"]/text()').extract_first()
        movie_time = movie_time.split("分钟")[0].strip()
        # 电影剧情简介
        try:
            movie_Introduction = response.xpath(
                '//*[@id="link-report"]/span[@property="v:summary"]/text()').extract_first().strip()

        except Exception:
            movie_Introduction = None
        # 电影评分
        movie_score = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract_first()

        # 评价人数
        movie_num = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()').extract_first()

        item = DoubanTop250Item()

        item['movie_url'] = movie_url
        item['movie_picture'] = movie_picture
        item['movie_name'] = movie_name
        item['movie_date'] = movie_date
        item['movie_score'] = movie_score
        item['movie_num'] = movie_num
        item['movie_time'] = movie_time
        item['movie_director'] = movie_director
        item['movie_actors'] = movie_actors
        item['movie_type'] = movie_type
        item['movie_Introduction'] = movie_Introduction
        # print(item)

        yield item