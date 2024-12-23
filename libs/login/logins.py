#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import re
from pathlib import Path

from requests import request

from tools.files import write_file


class Login:
    def __init__(self, username, password, is_password):
        self.username = username
        self.password = password
        self.is_password = is_password

    def is_valid_email(self):
        # 定义邮箱的正则表达式
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        res = re.match(email_regex, self.username) is not None
        if res:
            return True
        else:
            return False

    def is_valid_password(self):
        # 检查密码长度是否在 6 到 30 位之间
        if not (6 <= len(self.password) <= 20):
            return False
        # 检查密码是否包含中文字符
        if re.search(r'[\u4e00-\u9fff]', self.password):
            return False
        return True

    def login(self):

        _file_path = "C:/CuteAide/login_info.txt"

        path = Path(_file_path)  # 创建文件
        if not path.is_file():  # 如果文件不存在, 则创建文件
            path.parent.mkdir(parents=True, exist_ok=True)  # 创建文件夹
            path.touch()  # 创建文件

        if self.is_valid_email() and self.is_valid_password():
            _url = "http://119.45.236.69:9527/login"
            _data = {"username": self.username, "password": self.password}
            if self.is_password:

                content = f"{self.username},{self.password},{self.is_password}"
                with open(_file_path, 'w+') as f:
                    f.write(content)
            else:
                content = f"{self.username},{self.password},False"
                with open(_file_path, 'w+') as f:
                    f.write(content)
            return request("POST", _url, json=_data).json()
        else:
            return {"code": "401", "message": "邮箱或密码错误"}


if __name__ == '__main__':
    login = Login("gdmuye@q0.com", "123444446", True)
    res = login.login()
    print(res["code"])

