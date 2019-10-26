# -*- coding: utf-8 -*- 
# @Time : 2019/6/25 15:23 
# @Author :  
# @Site :  
# @File : reload_jsonencode.py
# @Software: PyCharm

import decimal

from flask import json


class DecimalEncoder(json.JSONEncoder):
    """
    重写flask.json.JSONEncoder json解析类，实现对数据库Decimal数据类型的序列化
    """

    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)

# class BaseModel(object):
#
#     def add_update(self):
#         db.session.add(self)
#         db.session.commit()
#
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#
#     def bade_to_dict(self):
#         columns = [c.key for c in class_mapper(self.__class__).columns]
#         return dict((c, getattr(self, c) if getattr(self, c) is not None else '') for c in columns)
