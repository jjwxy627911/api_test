# -*- coding:utf-8 -*-
# @Time     : 2019-10-20 13:44
# @Author   : davis
# @Email    : jjwxy627911@163.com
# @File     : test_01_register.py
# @Software : PyCharm

import json
import unittest
from libs.ddt import ddt, data

from scripts.handle_excel import HandleExcel
from scripts.handle_request import HandleRequest
from scripts.handle_mysql import HandleMysql
from scripts.handle_context import Context
from scripts.handle_configure import cf
from scripts.handle_log import logger
from scripts.constance import CASES_FILE_PATH
from main import conf_env

do_excel = HandleExcel(CASES_FILE_PATH, "invest")
cases = do_excel.get_cases()


@ddt
class TestInvest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.request = HandleRequest()
        cls.handler_mysql = HandleMysql()
        logger.debug("\n{:=^40s}".format("开始执行测试"))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.request.close()
        logger.debug("\n{:=^40s}".format("结束测试"))

    @data(*cases)
    def test_invest(self, item):
        case_id = item["case_id"]
        title = item["title"]
        url = cf.get_value(conf_env, "prefix_url") + item["url"]
        method = item["method"]
        expected = item["expected"]
        data = item["data"]

        new_data = Context.invest_parameterization(data)  # 将数据中进行参数替换

        check_sql = item["check_sql"]
        if check_sql:
            new_sql = Context.invest_parameterization(check_sql)
            result = self.handler_mysql.select(new_sql)
            loan_id = result.get("id")
            setattr(Context, "loan_id", loan_id)

        msg = "测试" + title
        success_msg = cf.get_value("case", "success")
        fail_msg = cf.get_value("case", "fail")

        ret = self.request.send_request(method, url, new_data)

        try:
            self.assertIn(str(expected), ret.text, msg)

            do_excel.write_value(case_id + 1, cf.get_int("case", "actual_col"), ret.text)
            do_excel.write_value(case_id + 1, cf.get_int("case", "result_col"), success_msg)
            logger.debug("{}, 执行结果为:{}".format(msg, success_msg))
        except AssertionError as e:
            do_excel.write_value(case_id + 1, cf.get_int("case", "actual_col"), ret.text)
            do_excel.write_value(case_id + 1, cf.get_int("case", "result_col"), fail_msg)
            logger.error("{}, 执行结果为:{}, 异常结果为:{}".format(msg, fail_msg, e))
            raise e


if __name__ == '__main__':
    unittest.main()
