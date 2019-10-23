# -*- coding:utf-8 -*-
# @Time     : 2019-10-16 23:03
# @Author   : davis
# @Email    : jjwxy627911@163.com
# @File     : handle_log.py
# @Software : PyCharm

import os
import logging
import datetime

from scripts.constance import LOGS_DIR
from scripts.handle_configure import cf


class HandleLog:
    def __init__(self):
        # 日志收集器,
        self.case_logger = logging.getLogger(cf.get_value("log", "log_name"))

        # 日志等级
        self.case_logger.setLevel(cf.get_value("log", "log_level"))

        # 日志输出渠道
        # 控制台
        console_handle = logging.StreamHandler()
        console_handle.setLevel(cf.get_value("log", "console_level"))  # 控制台输入日志等级

        # 文件
        # 在当前目录下创建  年-月-日.log文件并写入日志
        log_filename = datetime.datetime.now().strftime(cf.get_value("log", "file_name_format"))
        log_path = os.path.join(LOGS_DIR, log_filename + ".log")
        file_handle = logging.FileHandler(log_path, encoding="utf-8")
        file_handle.setLevel(cf.get_value("log", "file_level"))  # 文件输入日志等级

        # 日志格式
        simple_formatter = logging.Formatter(cf.get_value("log", "simple_formatter"))
        verbose_formatter = logging.Formatter(cf.get_value("log", "verbose_formatter"))

        console_handle.setFormatter(simple_formatter)
        file_handle.setFormatter(verbose_formatter)

        # 收集器与渠道对接
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        """
        获取日志对象
        :return:
        """
        return self.case_logger


logger = HandleLog().get_logger()

if __name__ == "__main__":
    logger.debug("aaa")
    logger.info("aaa")
    logger.warning("aaa")
    logger.error("aaa")
    logger.critical("aaa")
