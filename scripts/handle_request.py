# -*- coding:utf-8 -*-
# @Time     : 2019-07-06 13:05
# @Author   : davis
# @Email    : jjwxy627911@163.com
# @File     : handle_request.py
# @Software : PyCharm

import requests
import json

from json import JSONDecodeError

from scripts.handle_log import logger


class HandleRequest:
    """
    发送请求
    """

    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, url, data=None, is_json=False, **kwargs):
        """

        :param method:
        :param url:
        :param data:
        :param headers:
        :param is_json: 请求数据是否是json
        :return:
        """
        method = method.upper()

        if isinstance(data, str):

            try:
                data = json.loads(data)
            except JSONDecodeError:
                data = eval(data)

        if method == "GET":  # get请求
            try:
                response = self.session.get(url=url, params=data, **kwargs)
            except Exception as e:
                logger.error("执行get请求报错,错误是{}".format(e))
                return

        elif method == "POST":

            try:
                if is_json:
                    # json
                    response = self.session.post(url=url, json=data, **kwargs)
                else:
                    # form表单
                    response = self.session.post(url=url, data=data, **kwargs)
            except Exception as e:
                response = None
                logger.error("执行post请求报错,错误是{}".format(e))
        else:
            response = None
            logger.error("请求方法错误, 错误是{}".format(method))

        logger.info("请求url: {}, 请求参数: {}, 请求头: {}".format(url, data, self.session.headers))
        logger.info("响应状态码: {}, 响应结果: {}, 请求头: {}".format(response.status_code, response.text, response.headers))
        self.close()
        return response

    def close(self):
        self.session.close()


if __name__ == "__main__":
    request = HandleRequest()

    host = "http://test.lemonban.com:8080"

    register_url = "/futureloan/mvc/api/member/register"
    register_data = {'mobilephone': '13884106352', 'pwd': '123456'}

    ret = request.send_request("post", host + register_url, register_data, is_json=True)
    print(ret.json())

    # login_url = "/futureloan/mvc/api/member/login"
    # login_data = {"mobilephone": "17800001111", "pwd": "123456"}
    #
    # recharge_url = "/futureloan/mvc/api/member/recharge"
    # recharge_data = {"mobilephone": "", "amount": -10000}

    # 发送注册请求
    # login_res = request.send_request("post", host + login_url, login_data, headers={"User-Agent": "Mozilla/5.0"})
    # recharge_res = request.send_request("post", host + recharge_url, recharge_data)

    # 发送登录请求

    # 发送充值请求
    # print(recharge_res.json())
    # print(recharge_res.json())
