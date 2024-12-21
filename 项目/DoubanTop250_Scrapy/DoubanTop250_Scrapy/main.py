

# from scrapy.cmdline import execute
# #
# # execute("scrapy crawl Top250".split())

import time
from scrapy.cmdline import execute


from DoubanTop250_Scrapy.const import DB_CONFIG, CSV_NAME
from DoubanTop250_Scrapy.utils.mysql_util import MysqlDB
from DoubanTop250_Scrapy.utils.file_util import FileHandle


def deal_csv():

    file_content = FileHandle().read_csv(CSV_NAME)

    insert_content = []
    file_header = file_content[0]

    for movie_info in file_content[1:]:

        movie_dict = dict(zip(file_header, movie_info))
        insert_content.append(
            (
                movie_dict.get('movie_name'), movie_dict.get('movie_date'), movie_dict.get('movie_score'),
                movie_dict.get('movie_num'),
                movie_dict.get('movie_time'), movie_dict.get('movie_type'), movie_dict.get('movie_director'),
                movie_dict.get('movie_actors'),
                movie_dict.get('movie_url'), movie_dict.get('movie_picture'), movie_dict.get('movie_Introduction')
            )
        )

    return insert_content


def content_to_db(content):

    db = MysqlDB(**DB_CONFIG)
    db.connection()

    sql = """
        INSERT INTO douban_movie(movie_name, movie_date, movie_score, movie_num, movie_time, movie_type, 
        movie_director, movie_actors, movie_url, movie_picture, movie_Introduction) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    res = db.execute_many(sql, content)
    print(res)


if __name__ == "__main__":

    # execute("scrapy crawl Top250".split())
    #
    # time.sleep(5)

    content = deal_csv()
    print(content)
    print("content to db")
    content_to_db(content)


