# DouBan-250-Top
# 项目简介
本项目是对豆瓣排名前250的电影进行分析，并将分析结果可视化，并可用过浏览器访问实现查看可视化结果。本项目依托于Python的Scrapy和Flask框架，其中使用Scrapy框架去爬取豆瓣电影250的数据，将影片的信息获取出来并存到mysql数据里。使用Python的Flask框架实现浏览器对服务的访问，根据请求的url的访问不同的功能，从数据库中取出已爬取的数据，根据条件进行筛选，并通过python的可视化工具Pyecharts对数据进行可视化处理，本项目相对于目前已有的电影爬取项目，在可视化的美观程度和人机交互性上大幅提升
# 运行方法
先点开文件夹DoubanTop250_Scrapy中的run.py（在const.py中存放了数据库的配置），然后再打开文件夹EcharCode里的app.py，就可以生成网页了
