from sys import stdout, stderr

import os

from APP.settings import BASE_DIR

LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.exists(LOG_DIR):
    # 新建目录
    os.makedirs(LOG_DIR)

# 日志配置
LOGGING_CONFIG_LOCAL = dict(
    version=1,
    disable_existing_loggers=False,

    loggers={
        "flask.app": {  # flask运行view日志
            "level": "INFO",  # 等级
            "handlers": ["console", "root_file", "error_file"],
        },
        "werkzeug": {  # flask框架日志记录
            "level": "INFO",  # 等级
            "handlers": ["console", "access_file", "error_file"],
        },
    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": stdout,
        },
        "error_console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": stderr,
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": stdout,
        },
        "root_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "generic",
            "filename": os.path.join(LOG_DIR, 'zhyd_root_log.txt'),
            "when": "D",
            "interval": 1,
            "backupCount": 30,
            "encoding": "utf8",
        },
        "access_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "generic",
            "filename": os.path.join(LOG_DIR, 'zhyd_acc_log.txt'),
            "when": "D",
            "interval": 1,
            "backupCount": 30,
            "encoding": "utf8",
        },
        "error_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "ERROR",
            "formatter": "generic",
            "filename": os.path.join(LOG_DIR, 'zhyd_err_log.txt'),
            "when": "D",
            "interval": 30,
            "backupCount": 15,
            "encoding": "utf8",
        }
    },
    formatters={
        "generic": {
            "format": "[%(asctime)s] - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "class": "logging.Formatter"
        },
    }
)
