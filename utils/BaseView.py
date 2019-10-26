import datetime
from copy import deepcopy
from json import dumps

from flask import jsonify, request, session
from flask.views import View

from utils import status_code
from utils.sqlutils import coon_mysql
from abc import ABCMeta, abstractmethod


class BaseView(View, metaclass=ABCMeta):
    decorators = (coon_mysql,)

    def __init__(self):
        super(BaseView, self).__init__()
        self._permissions = None
        self.api_permission = None  # api 接口权限名称和数据库中的名称对应
        self._uid = None  # 用户uid
        self.db = None  # 数据库连接对象
        self.args = None  # 前端传过来的参数字典
        self.ids = None  # 用户可以查看的权限范围ID列表
        self.get_total_row = """SELECT FOUND_ROWS() as total_row;"""
        self.success = deepcopy(status_code.SUCCESS)

    def dispatch_request(self, db):
        """
            请求进入后台处理的初始函数
            :param db:
            :return:
        """
        self.get_args()
        self.db = db
        # return self.administrator()
        if request.path in self.whitelist:
            return self.administrator()
        try:
            tempint = session['AdminType']
        except:
            return jsonify(status_code.USER_NOT_LOGIN)
        self._uid = session['id']
        if int(session['AdminType']) == 0:
            return self.administrator()
        elif int(session['AdminType']) == 1:
            if not self.check_permission():
                return jsonify(status_code.PERMISSION_NOT_EXISTS)
            return self.admin()
        else:
            if not self.check_permission():
                return jsonify(status_code.PERMISSION_NOT_EXISTS)
            return self.guest()

    def get_args(self):
        """
        多种方式获取前端传过来的参数
        :return:
        """
        args = dict(request.form.items())
        if dict(args) == {}:
            args = request.args
        if dict(args) == {}:
            args = request.json
            if args is None:
                args = {}
        self.args = args

    def args_is_null(self, *args):
        """
        判断参数是否是空，传入一个不定常参数
        :param args:
        :return:
        """
        for i in args:
            if self.args.get(i, None) is None:
                return True
            if self.args.get(i, '') == '':
                return True
            if self.args.get(i, '') == 'null':
                return True
            if self.args.get(i, '') == 'NaN':
                return True
            if i in ('ProvinceID', 'CityID', 'DistrictID', 'PID', 'CID', 'DID', 'province', 'city', 'district'):
                if self.args.get(i, '') == '0':
                    return True
            if self.args.get(i) == 'undefined' or self.args.get(i) == '请选择':
                return True
        return False

    @abstractmethod
    def administrator(self):
        pass

    @abstractmethod
    def admin(self):
        pass

    # @abstractmethod
    def guest(self):
        return self.admin()

    def splice_sql(self, sql_list, method):
        """
        拼接where子句和set子句，返回拼好的字符串
        :param sql_list: 子句字符串组成的列表
        :param method: 拼接方式，where 或者update
        :return: 子句字符串
        """
        temp = ''
        for index, i in enumerate(sql_list):
            temp += str(i)
            if index < len(sql_list) - 1:
                if method == 'where':
                    temp += ' and '
                else:
                    temp += ','
        return temp

    def update_data(self, db_name, insert_dict, remove_list=['id', ]):
        """
        更新数据接口
        :param db_name: 更新的表名
        :param remove_list: 需要移除的一些项
        :param insert_dict: 要更新的字段列表
        :return:
        """
        update_sql = r"""update {} set """.format(db_name)
        id = insert_dict.get('id')
        for i in remove_list:
            if i in insert_dict.keys():
                del insert_dict[i]
        update_list = []
        for key in insert_dict.keys():
            update_list.append(r""" {}='{}' """.format(key, insert_dict[key]))
        if update_list:
            for index, i in enumerate(update_list):
                update_sql += i
                if index < len(update_list) - 1:
                    update_sql += ','
        limit_sql = r""" where id={};""".format(id)
        try:
            self.db.update(update_sql + limit_sql)
        except:
            return False
        return True

    def str_to_datetime(self, time_str):
        return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    def datetime_to_str(self, ob_datetime):
        return ob_datetime.strftime("%Y-%m-%d %H:%M:%S")

    def datetime_to_datestr(self, ob_datetime):
        return ob_datetime.strftime("%Y-%m-%d")

    def datetime_to_timestr(self, ob_datetime):
        return ob_datetime.strftime("%H:%M:%S")

    def get_where_sql(self, where_sql_list):
        """
        生成where子句格式化后的字符串
        :param where_sql_list: where子句字符串构成的列表
        :return: 组合好的where子句
        """
        temp = ''
        if where_sql_list:
            temp = ' where '
            temp += ' and '.join(where_sql_list)
        return temp

    def get_limit_sql(self, page, pagesize):
        return r""" limit {},{}; """.format((page - 1) * pagesize, pagesize)

    def set_ids(self, sql):
        """
        当用户不是superadmin时，获取管辖范围内的id（公司，项目，劳工）
        :param sql:
        :return:
        """
        result = self.db.query(sql)
        return [item['ID'] for item in result]

    def to_sql_where_ids(self):
        return ','.join(self.ids) if self.ids else ''

    def query_filter(self, result, field='ID'):
        """
        搜索查询过滤，将正常查询的结果和管辖范围内的ID进行对比，过滤掉不是管辖范围内的数据
        :param result:
        :return:
        """
        if self.ids:
            temp_result = []
            for item in result:
                if item[field] in self.ids:
                    temp_result.append(item)
            return temp_result
        else:
            return result

    def check_permission(self):
        """
        权限验证，有权限返回True，没有权限返回False
        :return:
        """
        if self.api_permission is not None:
            if self.api_permission not in session['Permission']:
                return False
        return True
    
    def has_data(self, table_name, field, data, db_id):
        if db_id is None:
            query_sql = r"""select id from {} where {}='{}';""".format(table_name, field, data)
        else:
            query_sql = r"""select id from {} where {}='{}' and id!={};""".format(table_name, field, data, db_id)
        result = self.db.query(query_sql)
        if result:
            return True
        return False

    def get_session_ids(self):
        """
        将session中的区域ID转换为sql语句中where中的条件格式
        :return:
        """
        return ','.join([str(aid) for aid in session['area_ids']]) if self['area_ids'] else ''

    def get_project_ids(self):
        """根据权限类型获取用户可以管理的项目ID列表"""
        if session['pertype'] == 1:
            project_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
            # self.project_ids = self.set_ids(project_sql)
        else:
            project_sql = r"""select t2.ID from tb_user_pro as t1
                                left join tb_project as t2 on t1.pid=t2.ID
                                where t1.uid={}""".format(session['id'])
        return self.set_ids(project_sql)

    def get_labor_ids(self):
        """根据权限获取用户可以管理的劳工列表"""
        if session['pertype'] == 1:
            labor_sql = r"""select t2.ID from tb_project as t1 
                            left join tb_laborinfo as t2 on t1.id = t2.projectid
                            where t1.did in ({})""".format(self.get_session_ids())
        else:
            labor_sql = r"""select t2.ID from tb_user_pro as t1
                            left join tb_laborinfo as t2 on t2.projectid = t1.pid
                            where t1.uid={};""".format(session['id'])
        return self.set_ids(labor_sql)

    def get_company_ids(self):
        """根据权限类型获取用户可以管理的企业列表"""
        if session['pertype'] == 1:
            company_sql = r"""select Build,Cons,subcompany from tb_project where DID in ({});""".format(
                self.get_session_ids())
        else:
            company_sql = r"""select t2.Build,t2.Cons,t2.subcompany from tb_user_pro as t1
                                left join tb_project as t2 on t1.pid=t2.ID
                                where t1.uid={}""".format(session['id'])
        self.company_ids = []
        result = self.db.query(company_sql)
        if result:
            for item in result:
                self.company_ids.append(item['Build'])
                self.company_ids.append(item['Cons'])
                if item['subcompany'] == '' or item['subcompany'] is None:
                    continue
                subcompanys = dumps(item['subcompany'])
                for subcom in subcompanys:
                    if not isinstance(subcom, dict):
                        continue
                    if 'id' in subcom.keys():
                        self.company_ids.append(subcom['id'])
        return self.company_ids
