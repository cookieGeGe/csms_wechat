# -*- coding: utf-8 -*- 
# @Time : 2019/6/26 17:24 
# @Author :  
# @Site :  
# @File : reload_werkzeug_log.py 
# @Software: PyCharm
# from werkzeug._internal import _log
from werkzeug._internal import _log
from werkzeug.serving import WSGIRequestHandler


class ReloadWSGIRequestHandler(WSGIRequestHandler):

    def log(self, type, message, *args):
        _log(
            type,
            "%s - - %s\n"
            % (self.address_string(), message % args),
        )
