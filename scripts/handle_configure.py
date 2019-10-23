# -*- coding:utf-8 -*-
# @Time     : 2019-10-16 23:19
# @Author   : davis
# @Email    : jjwxy627911@163.com
# @File     : handle_configure.py
# @Software : PyCharm

from configparser import ConfigParser, NoSectionError, NoOptionError
from scripts.constance import CONFIG_FILE_PATH


class HandleConfigure:

    def __init__(self, file_path):
        self.file_path = file_path
        self.cf = ConfigParser()
        self.cf.read(self.file_path, encoding="utf-8")

    def get_value(self, section, option):
        """ 获取字符串类型配置 """
        try:

            return self.cf.get(section, option)

        except NoSectionError as e:
            print("section not exist : ", e)

        except NoOptionError as e:

            print("option not exist : ", e)

    def get_int(self, section, option):
        """ 获取int类型配置 """
        try:

            return self.cf.getint(section, option)

        except NoSectionError as e:
            print("section not exist : ", e)

        except NoOptionError as e:

            print("option not exist : ", e)

    def get_float(self, section, option):
        """ 获取float类型配置 """
        try:

            return self.cf.getfloat(section, option)

        except NoSectionError as e:
            print("section not exist : ", e)

        except NoOptionError as e:

            print("option not exist : ", e)

    def get_boolean(self, section, option):
        """
        getboolean()方法对大小写不敏感，能识别'yes'/'no', 'on'/'off', 'true'/'false'和'1'/'0'为对应的布尔值
        :return:
        """
        try:

            return self.cf.getboolean(section, option)

        except NoSectionError as e:
            print("section not exist : ", e)

        except NoOptionError as e:

            print("option not exist : ", e)

    def get_eval_data(self, section, option):
        """
        获取列表，元祖，字典类型的配置
        例如
            var = [1,2,3]
            var1 = (4,5,6)
            var2 = {"name":"alex", "age":20}
        """
        try:

            value = self.cf.get(section, option)
            return eval(value)
        except NoSectionError as e:
            print("section not exist : ", e)

        except NoOptionError as e:

            print("option not exist : ", e)

    @staticmethod
    def write_config(filename, data):
        """
            写入配置
            例如
            data = {
                "case": {"case_path": "cases.xlsx"},
                "log": {"log_name": "case"}
            }
        """
        config = ConfigParser()
        for key in data:
            print(data[key])
            config[key] = data[key]

        with open(filename, "w", encoding="utf-8") as file:
            config.write(file)


cf = HandleConfigure(CONFIG_FILE_PATH)

if __name__ == '__main__':
    # cf = HandleConfigure("config.ini")
    print(cf.get_value("log", "log_name"))

    # 读取
    # print(cf.get_value("case", "success"))
    # print(cf.get_eval_data("case", "var"))
    # print(cf.get_eval_data("case", "var1"))
    # print(cf.get_eval_data("case", "var2"))

    # 写入
    # data = {
    #     "case": {"case_path": "cases.xlsx"},
    #     "log": {"log_name": "case"}
    # }
    # cf.write_config("config_old.conf", data)
