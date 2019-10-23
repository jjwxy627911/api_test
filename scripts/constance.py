# -*- coding:utf-8 -*-
# @Time     : 2019-10-20 12:41
# @Author   : davis
# @Email    : jjwxy627911@163.com
# @File     : constance.py
# @Software : PyCharm

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
CONFIG_DIR = os.path.join(BASE_DIR, "conf")
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, "testcase_conf.ini")

# 测试用例xlsx
CASES_DIR = os.path.join(BASE_DIR, "cases")
CASES_FILE_PATH = os.path.join(CASES_DIR, "cases.xlsx")


DATAS_DIR = os.path.join(BASE_DIR, "datas")

# 日志
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# 测试报告
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

# 生成用户账号信息配置文件
USER_ACCOUNT_FILE_PATH = os.path.join(BASE_DIR, "conf", "test_user_info.ini")
