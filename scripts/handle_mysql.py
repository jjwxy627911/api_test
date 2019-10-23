# -*- coding:utf-8 -*-
# @Time     : 2019-07-09 20:49
# @Author   : davis
# @Email    : jjwxy627911@163.com
# @File     : handle_mysql.py
# @Software : PyCharm

import string
import pymysql
import random

from scripts.handle_configure import cf


# host = tj.lemonban.com
# user = test
# password = test
# port = 3306
# db = future

class HandleMysql:

    def __init__(self):
        # 创建连接
        self.conn = pymysql.connect(
            host=cf.get_value("mysql", "host"),
            user=cf.get_value("mysql", "user"),
            password=cf.get_value("mysql", "password"),
            port=cf.get_int("mysql", "port"),
            charset="utf8",
            db=cf.get_value("mysql", "db"),
            cursorclass=pymysql.cursors.DictCursor  # sql语句返回结果是字典类型
        )

        # 创建游标
        self.cursor = self.conn.cursor()

    def select(self, sql, args=None, is_all=False):
        """

        :param sql:
        :param args:
        :param is_all:是否查询多条记录
        :return:
        """
        self.cursor.execute(sql, args=args)

        # 提交请求，执行sql
        self.conn.commit()

        if is_all:
            # 返回多条数据
            data = self.cursor.fetchall()
        else:
            # 返回一条数据
            data = self.cursor.fetchone()

        # self.close()
        return data

    @staticmethod
    def create_mobile():
        prefix_mobile = ["138", "133", "158", "189"]
        mobile_num = f'{random.choice(prefix_mobile)}{"".join(random.sample("0123456789", 8))}'

        return mobile_num

    def mobile_exists(self, mobile):
        """
        判断手机号是否存在
        :return:
        """
        sql = "select id from member where mobilephone=%s limit 10 "
        ret = self.select(sql, args=(mobile,))
        if ret:  # 如果手机号存在返回True, 不存在返回False
            return True
        return False

    def get_not_exists_mobile(self):
        """
        获取不存在的手机号
        :return:
        """
        while True:
            mobile = self.create_mobile()
            if not self.mobile_exists(mobile):
                break

        return mobile

    def get_exists_mobile(self):
        """
        获取已存在的手机号
        :return:
        """
        sql = "select mobilephone from member limit 0,1 "
        ret = self.select(sql)
        return ret["mobilephone"]

    def close(self):
        """
        关闭连接
        :return:
        """
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    mysql = HandleMysql()
    # print(mysql.get_not_exists_mobile())
    # print(mysql.get_exists_mobile())

    # mysql.close()

    import decimal
    ret = mysql.select("SELECT  LeaveAmount  FROM  member  where  MobilePhone=17800001111")
    # ret = mysql.select("select id from member where id between %s and %s limit 10", args=(2, 10), is_all=True)

