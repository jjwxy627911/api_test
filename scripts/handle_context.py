# -*- coding:utf-8 -*-
# @Time     : 2019-10-20 13:43
# @Author   : davis
# @Email    : jjwxy627911@163.com
# @File     : handle_context.py
# @Software : PyCharm

import re
from scripts.handle_mysql import HandleMysql
from scripts.handle_configure import HandleConfigure
from scripts.constance import USER_ACCOUNT_FILE_PATH

cf = HandleConfigure(USER_ACCOUNT_FILE_PATH)
handle_mysql = HandleMysql()


class Context:
    # 替换规则
    not_exists_mobile_pattern = r'\$\{not_exists_phone\}'
    exists_mobile_pattern = r'\$\{exists_phone\}'

    invest_user_phone_pattern = r'\$\{invest_user_phone\}'
    invest_user_pwd_pattern = r'\$\{invest_user_pwd\}'
    admin_user_phone_pattern = r'\$\{admin_user_phone\}'
    admin_user_pwd_pattern = r'\$\{admin_user_pwd\}'

    borrow_id_pattern = r'\$\{borrow_id\}'
    borrow_id_not_exists_pattern = r'\$\{borrow_id_not_exists\}'

    invest_id_pattern = r'\$\{invest_id\}'
    invest_id_not_exists_pattern = r'\$\{invest_id_not_exists\}'
    loan_id_pattern = r'\$\{loan_id\}'
    loan_id_not_exists_pattern = r'\$\{loan_id_not_exists\}'

    @classmethod
    def not_exists_mobile_replace(cls, data):
        """
        替换不存在的手机号
        :param data:
        :return:
        """
        if re.search(cls.not_exists_mobile_pattern, data):
            mobile_phone = HandleMysql().get_not_exists_mobile()
            data = re.sub(cls.not_exists_mobile_pattern, mobile_phone, data)

        return data

    @classmethod
    def exists_mobile_replace(cls, data):
        """
        替换存在的手机号
        :param data:
        :return:
        """
        if re.search(cls.exists_mobile_pattern, data):
            mobile_phone = HandleMysql().get_exists_mobile()
            data = re.sub(cls.exists_mobile_pattern, mobile_phone, data)

        return data

    @classmethod
    def invest_user_phone_replace(cls, data):
        mobile = cf.get_value("invest_user", "mobilephone")
        data = re.sub(cls.invest_user_phone_pattern, mobile, data)
        return data

    @classmethod
    def invest_user_pwd_replace(cls, data):
        pwd = cf.get_value("invest_user", "pwd")
        data = re.sub(cls.invest_user_pwd_pattern, pwd, data)
        return data

    @classmethod
    def admin_user_phone_replace(cls, data):
        mobile = cf.get_value("admin_user", "mobilephone")

        data = re.sub(cls.admin_user_phone_pattern, mobile, data)
        return data

    @classmethod
    def admin_user_pwd_replace(cls, data):
        pwd = cf.get_value("admin_user", "pwd")
        data = re.sub(cls.admin_user_pwd_pattern, pwd, data)
        return data

    @classmethod
    def borrow_id_replace(cls, data):
        id = cf.get_value("borrow_user", "id")
        data = re.sub(cls.borrow_id_pattern, id, data)
        return data

    @classmethod
    def invest_id_replace(cls, data):
        id = cf.get_value("invest_user", "id")
        data = re.sub(cls.invest_id_pattern, id, data)
        return data

    @classmethod
    def invest_id_not_exists_replace(cls, data):
        id = cf.get_int("invest_user", "id")
        data = re.sub(cls.invest_id_not_exists_pattern, str(id + 10000), data)
        return data

    @classmethod
    def loan_id_replace(cls, data):
        if re.search(cls.loan_id_pattern, data):
            loan_id = getattr(cls, "loan_id")
            data = re.sub(cls.loan_id_pattern, str(loan_id), data)

        return data

    @classmethod
    def loan_id_not_exists_replace(cls, data):
        if re.search(cls.loan_id_not_exists_pattern, data):
            loan_id = getattr(cls, "loan_id")
            data = re.sub(cls.loan_id_not_exists_pattern, str(loan_id + 10000), data)

        return data

    @classmethod
    def borrow_id_not_exists_replace(cls, data):

        sql = "select id from member order by id desc limit 0,1"
        ret = handle_mysql.select(sql)
        if ret:
            max_id = ret.get("id")

            data = re.sub(cls.borrow_id_not_exists_pattern, str(max_id + 10000), data)

        return data

    @classmethod
    def register_parameterization(cls, data):
        """
        请求数据正则替换
        :param data:
        :return:
        """
        data = cls.not_exists_mobile_replace(data)

        data = cls.exists_mobile_replace(data)

        return data

    @classmethod
    def login_parameterization(cls, data):
        """
        请求数据正则替换
        :param data:
        :return:
        """
        data = cls.invest_user_phone_replace(data)

        data = cls.invest_user_pwd_replace(data)

        return data

    @classmethod
    def recharge_parameterization(cls, data):
        """
        请求数据正则替换
        :param data:
        :return:
        """
        data = cls.invest_user_phone_replace(data)
        data = cls.invest_user_pwd_replace(data)
        data = cls.not_exists_mobile_replace(data)

        return data

    @classmethod
    def add_parameterization(cls, data):
        """
        请求数据正则替换
        :param data:
        :return:
        """
        data = cls.admin_user_phone_replace(data)
        data = cls.admin_user_pwd_replace(data)
        data = cls.borrow_id_replace(data)
        data = cls.borrow_id_not_exists_replace(data)

        return data

    @classmethod
    def invest_parameterization(cls, data):
        """
        请求数据正则替换
        :param data:
        :return:
        """
        data = cls.admin_user_phone_replace(data)
        data = cls.admin_user_pwd_replace(data)
        data = cls.borrow_id_replace(data)

        data = cls.invest_user_phone_replace(data)
        data = cls.invest_user_pwd_replace(data)

        data = cls.invest_id_replace(data)
        data = cls.invest_id_not_exists_replace(data)

        data = cls.loan_id_replace(data)
        data = cls.loan_id_not_exists_replace(data)

        return data


if __name__ == '__main__':
    data1 = '{"mobilephone":"${not_exists_phone}","pwd":"123456"}'
    data2 = '{"mobilephone":"${exists_phone}","pwd":"123456","regname":"davis"}'
    data3 = '{"mobilephone":"175210050581","pwd":"1234511","regname":"davis"}'
    data4 = "{'mobilephone': '${invest_user_phone}', 'pwd': '${invest_user_pwd}'}"
    data5 = '{"memberId":"${borrow_id_not_exists}","title":"上海买房","amount":100000,"loanRate":18.0,"loanTerm":4,"loanDateType":0,"repaymemtWay":4,"biddingDays":12}'
    data6 = '{"mobilephone":"${admin_user_phone}","pwd":"${admin_user_pwd}"}'
    data7 = '{"memberId":"${borrow_id}","title":"上海买房","amount":-100000,"loanRate":18.0,"loanTerm":4,"loanDateType":0,"repaymemtWay":4,"biddingDays":16}'
    # print(Context.register_parameterization(data1))
    # print(Context.register_parameterization(data2))
    # print(Context.register_parameterization(data3))

    print(Context.add_parameterization(data7))
