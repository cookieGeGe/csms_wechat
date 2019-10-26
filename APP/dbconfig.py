# -*- coding: utf-8 -*-
# @Time : 2019/7/24 14:28
# @Author :
# @Site :
# @File : AppConfig.py
# @Software: PyCharm
from APP.settings import DATABASE, DATABASE_P, redisInfo, redisInfo_p, env


class DBConfig(object):
    # env = 'dev'
    # env = 'project'

    @staticmethod
    def get_mysql_config():
        if env == 'dev':
            return DATABASE
        else:
            return DATABASE_P

    @staticmethod
    def get_redis_config():
        if env == 'dev':
            return redisInfo
        else:
            return redisInfo_p
