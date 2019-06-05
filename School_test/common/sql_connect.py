# -*- coding:utf-8 -*-
# Author:wangjian

import pymssql
import pymysql
from common import config as C

#连接数据库-测试环境
class SQL_conn(object):
    def __init__(self,sql):
        self.host = C.sql_server
        self.user = C.sql_user
        self.pwd = C.sql_pwd
        self.db = C.test_db
        self.port = 16033
        self.sql = sql
    def sql_conn(self):
        self.conn = pymysql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,port=self.port)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.sql)
    def sql_search(self):
        row = self.cursor.fetchall()
        List = []
        for i in row:
            List.append(i)
        return List
    def sql_close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    sql = "select * from city"
    S = SQL_conn(sql)
    S.sql_conn()
    t = S.sql_search()
    S.sql_close()
