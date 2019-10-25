# -*- coding:utf-8 -*-
# @Time     : 2019-10-20 19:38
# @Author   : davis
# @Email    : jjwxy627911@163.com
# @File     : main.py
# @Software : PyCharm

import os
import sys
import unittest
from datetime import datetime

from libs.HTMLTestRunnerNew import HTMLTestRunner

from scripts.constance import DATAS_DIR, REPORTS_DIR, USER_ACCOUNT_FILE_PATH
from scripts.handle_configure import cf
from scripts.handle_user import generate_user_config
from scripts.handle_log import logger

# from datas import test_05_invest

# 测试环境
test_env = sys.argv[1]
conf_env = f"api_{test_env}"
logger.debug(f"当前测试环境是：【{conf_env}】")


if not os.path.exists(USER_ACCOUNT_FILE_PATH):
    generate_user_config()


suites = unittest.defaultTestLoader.discover(DATAS_DIR)

# loader = unittest.TestLoader()
# suites = loader.loadTestsFromModule(test_05_invest)


report_name = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + "_testReport.html"
report_file_path = os.path.join(REPORTS_DIR, report_name)


with open(report_file_path, "wb") as file:
    runner = HTMLTestRunner(
        stream=file,
        title=cf.get_value("api", "title"),
        description=cf.get_value("api", "description"),
        tester=cf.get_value("api", "tester"),
        verbosity=cf.get_int("api", "verbosity"),
    )

    runner.run(suites)  # 开始执行测试
