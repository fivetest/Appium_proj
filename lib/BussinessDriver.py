#!/usr/bin/env python
# 业务的通用代码
from lib.AndroidDriver import AndroidDriver


class 啄木鸟App(object):
    def __init__(self):
        self.ad = AndroidDriver()

    def 打开首页(self):
        pass

    def 在登录页面输入用户名和密码(self, username, password):
        self.ad.type_by_id('cc.liushi.username', username)
        self.ad.type_by_id('cc.liushi.password', password)

    def 在点击注册按钮(self):
        pass

    def 输入指定的值(self):
        pass