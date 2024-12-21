import pymysql


class MysqlDB(object):

    def __init__(self, host='127.0.0.1', port=3306, username=None,
                 password=None, database=None, charset="utf8"):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.charset = charset
        self.conn = None
        self.cur = None

    def connection(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            database=self.database,
            charset=self.charset
        )
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

        return self.cur

    # 关闭数据库
    def close(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 增 删 改
    def execute(self, sql, params=None):
        result = None
        try:
            if self.conn and self.cur:
                result = self.cur.execute(sql, params)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()

        return result

    def execute_many(self, sql, params=None):
        result = None
        try:
            if self.conn and self.cur:
                result = self.cur.executemany(sql, params)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()

        return result

    #
    def fetch_one(self, sql, params=None):

        result = None

        try:
            self.execute(sql, params)
            result = self.cur.fetchone()

        except:
            self.conn.rollback()

        return result

    def fetch_all(self, sql, params=None):

        result = None

        try:
            self.execute(sql, params)
            result = self.cur.fetchall()

        except:
            self.conn.rollback()

        return result




