import os

import redis

from APP.functions import get_db_uri

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

templates_dir = os.path.join(BASE_DIR, 'templates')

static_dir = os.path.join(BASE_DIR, 'static')

upload_dir = os.path.join(static_dir, 'media')

# DATABASE = {
#     # 用户
#     'USER': 'root',
#     # 主机
#     'HOST': '127.0.0.1',
#     # 密码
#     'PASSWORD': 'admin123',
#     # 端口
#     'PORT': '3306',
#     # 数据库类型
#     'DB': 'mysql',
#     # 数据库驱动
#     'DRIVER': 'pymysql',
#     # 使用的数据库
#     'NAME': 'zhyd',
# }


DATABASE = {
    'USER': 'root',
    'HOST': '127.0.0.1',
    'PASSWORD': 'admin123',
    'PORT': '3306',
    'DB': 'mysql',
    'DRIVER': 'pymysql',
    'NAME': 'csms',
}

DATABASE_P = {
    'USER': 'root',
    'HOST': '47.92.138.195',
    'PASSWORD': 'admin123',
    'PORT': '3306',
    'DB': 'mysql',
    'DRIVER': 'pymysql',
    'NAME': 'csms',
}

SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
SQLALCHEMY_DATABASE_URI_P = get_db_uri(DATABASE_P)

SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_POOL_TIMEOUT = 20
SQLALCHEMY_POOL_RECYCLE = 60
SQLALCHEMY_MAX_OVERFLOW = 5
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True



redisInfo = {
    'host': '127.0.0.1',
    'password': 'admin123',
    'port': 6379,
    'db': 0,
    'minsize': 5,
    'maxsize': 30,
}

redisInfo_p = {
    'host': '47.92.138.195',
    'password': 'admin123',
    'port': 6379,
    'db': 0,
    'minsize': 5,
    'maxsize': 30,
}

env = 'dev'
# env = 'project'




