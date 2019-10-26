import functools

import pymysql
import time
from DBUtils.PooledDB import PooledDB

from APP.dbconfig import DBConfig
from APP.functions import db


class MysqlDB(object):

    def __init__(self):
        self.db = db
        self._session = self.db.session

    def close(self):
        self._session.remove()
        self._session.close()

    def query(self, sql):
        db_exe = self._session.execute(sql)
        data_list = list(map(lambda x: dict(zip(db_exe.keys(), x)), db_exe.fetchall()))
        return data_list

    def delete(self, sql):
        self._session.execute(sql)
        self._session.commit()

    def update(self, sql):
        self._session.execute(sql)
        self._session.commit()

    def insert(self, sql):
        db_exe = self._session.execute(sql)
        self._session.commit()
        return db_exe.lastrowid

    def execute(self, sql):
        sql_list = sql.split(';')
        for one_sql in sql_list:
            if one_sql != '':
                self._session.execute(one_sql + ';')
        self._session.commit()

    def __del__(self):
        self.close()


class OPMysql(object):
    __pool = None

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.pool = OPMysql.getmysqlconn()
        # self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)

    # 数据库连接池连接
    @staticmethod
    def getmysqlconn():
        if OPMysql.__pool is None:
            DATABASE = DBConfig.get_mysql_config()
            __pool = PooledDB(creator=pymysql,
                              mincached=2,
                              maxconnections=5,
                              blocking=True,
                              host=DATABASE['HOST'],
                              user=DATABASE['USER'],
                              passwd=DATABASE['PASSWORD'],
                              db=DATABASE['NAME'],
                              port=int(DATABASE['PORT']),
                              charset='utf8')
            # print(__pool)
        # return __pool.connection()
        return __pool

    def connection(self):
        coon = self.pool.connection()
        cur = coon.cursor(cursor=pymysql.cursors.DictCursor)
        return coon, cur

    # 插入\更新\删除sql
    def insert(self, sql, *args):
        coon, cur = self.connection()
        insert_num = cur.execute(sql, *args)
        coon.commit()
        self.close(cur, coon)
        return insert_num

    def update(self, sql, *args):
        coon, cur = self.connection()
        cur.execute(sql, *args)
        coon.commit()
        self.close(cur, coon)

    def delete(self, sql, *args):
        coon, cur = self.connection()
        cur.execute(sql, *args)
        coon.commit()
        self.close(cur, coon)

    # 查询
    def query(self, sql, *args):
        coon, cur = self.connection()
        cur.execute(sql, *args)  # 执行sql
        select_res = cur.fetchall()  # 返回结果为字典
        self.close(cur, coon)
        return select_res

    def execute(self, sql):
        coon, cur = self.connection()
        sql_list = sql.split(';')
        for one_sql in sql_list:
            if one_sql != '':
                coon.execute(one_sql + ';')
        coon.commit()
        self.close(cur, coon)

    def close(self, cur, coon):
        cur.close()
        coon.close()


def coon_mysql(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        one_coon = MysqlDB()
        result = fn(one_coon, *args, **kwargs)
        one_coon.close()
        return result

    return wrapper


def calc_time(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result

    return wrapper
