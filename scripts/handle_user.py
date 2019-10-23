# -*- coding:utf-8 -*-
# @Time     : 2019-10-20 19:57
# @Author   : davis
# @Email    : jjwxy627911@163.com
# @File     : handle_user.py
# @Software : PyCharm

"""
生成测试账号

"""
from scripts.handle_mysql import HandleMysql
from scripts.handle_request import HandleRequest
from scripts.handle_configure import cf
from scripts.constance import USER_ACCOUNT_FILE_PATH


def create_new_user(regname, pwd="123456"):
    """
    生成一个用户
    :param regname:
    :param pwd:
    :return:
    """
    handle_mysql = HandleMysql()
    handle_request = HandleRequest()

    url = cf.get_value("api", "prefix_url") + "/member/register"

    sql = "select Id from member where mobilephone=%s;"

    while True:
        mobile = handle_mysql.get_not_exists_mobile()

        data = {
            "mobilephone": mobile,
            "pwd": pwd,
            "regname": regname
        }

        handle_request.send_request("post", url, data)

        ret = handle_mysql.select(sql, args=(mobile,))
        if ret:
            user_id = ret["Id"]
            break

    user_dict = {
        regname: {
            "Id": user_id,
            "regname": regname,
            "mobilephone": mobile,
            "pwd": pwd
        }
    }

    handle_mysql.close()
    handle_request.close()

    return user_dict


def generate_user_config():
    """
    生成三个用户信息写入配置文件
    :return:
    """
    user_datas_dict = {}
    user_datas_dict.update(create_new_user("admin_user"))
    user_datas_dict.update(create_new_user("invest_user"))
    user_datas_dict.update(create_new_user("borrow_user"))

    cf.write_config(USER_ACCOUNT_FILE_PATH, user_datas_dict)


if __name__ == '__main__':
    # print(create_new_user("admin_user"))
    generate_user_config()
