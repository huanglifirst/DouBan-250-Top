# 数据库配置
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "username": "root",
    "password": "huangli68",
    "database": "douban"
}


CSV_NAME = 'douban_top250_export.csv'

# from DoubanTop250_Scrapy.utils.mysql_util import MysqlDB
# from DoubanTop250_Scrapy.utils.file_util import FileHandle
#
# db = MysqlDB(**DB_CONFIG)
# db.connection()
#
# sql = "SELECT * FROM douban_movie"
# res = db.fetch_all(sql)
# print(res)
#
# file_content = FileHandle().read_csv("douban_top250_export.csv")
#
# insert_content = []
# file_header = file_content[0]
#
#
# for movie_info in file_content[1:]:
#
#     movie_dict = dict(zip(file_header, movie_info))
#     insert_content.append(
#         (
#             movie_dict.get('movie_name'), movie_dict.get('movie_date'), movie_dict.get('movie_score'),
#             movie_dict.get('movie_num'),
#             movie_dict.get('movie_time'), movie_dict.get('movie_type'), movie_dict.get('movie_director'),
#             movie_dict.get('movie_actors'),
#             movie_dict.get('movie_url'), movie_dict.get('movie_picture'), movie_dict.get('movie_Introduction')
#          )
#     )
#
# print(insert_content)
# sql = """
#     INSERT INTO douban_movie(movie_name, movie_date, movie_score, movie_num, movie_time, movie_type,
#     movie_director, movie_actors, movie_url, movie_picture, movie_Introduction)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# """
#
#
# res = db.execute_many(sql, insert_content)
# print(res)
