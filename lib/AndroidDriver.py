#!/usr/bin/env python
# 此文件，是把Appium API的常用方法封装成一个类
# 这样可以很方便地进行调用。
# 把 Appium 的操作封装成各种函数
import sys
import traceback
from appium import webdriver
from config import woody_app_desired_caps


class AndroidDriver(object):
    def __init__(self):
        """初始化各种参数，并连接Appium Server等等"""
        appium_url = 'http://127.0.0.1:4723/wd/hub'  # hub 服务器
        self.driver = webdriver.Remote(appium_url, woody_app_desired_caps)

    @staticmethod
    def print_exception_message():
        """定义一个静态方法，用于输出标准的错误信息"""
        print("Exception in AndroidDriver:")
        print('-' * 30 + '错误信息请看下方' + '-' * 30)
        print(traceback.print_exc(file=sys.stdout))

    def type_by_id(self, locator, text):
        """根据id找到要输入的位置，并向其发送文本"""
        try:
            self.driver.find_element_by_id(locator).send_keys(text)
            return True
        except Exception as e:
            AndroidDriver.print_exception_message()
            return False

    def type_by_xpath(self, locator, text):
        """根据xpath找到要输入的位置，并向其发送文本"""
        try:
            self.driver.find_element_by_xpath(locator).send_keys(text)
            return True
        except Exception as e:
            AndroidDriver.print_exception_message()
            return False

    def click_by_xpath(self, locator):
        """点击xpath"""
        try:
            self.driver.find_element_by_xpath(locator).click()
            return True
        except Exception as e:
            AndroidDriver.print_exception_message()
            return False

    def swipe_to_down(self, duration=200):
        """向下滑动的操作"""
        # 注释
        driver = self.driver
        starty = driver.get_window_size()['height'] * 4/5
        # print(starty)
        endy = driver.get_window_size()['height'] * 1/5
        x = driver.get_window_size()['width'] * 1/2

        try:
            self.driver.swipe(x, starty, x, endy, duration)
            return True
        except Exception:
            # 如何出现异常，就转到这里
            AndroidDriver.print_exception_message()
            return False

    def quit(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    ad = AndroidDriver()   # 初始化 AndroidDriver对象
    # ad.swipe_to_down()
    # ad.type_by_id("cc.liushi.testapp:id/my_text_field", '啄木鸟')  # 向指定的位置，发送文本
    ad.click_by_xpath("//*[@resource-id='cc.liushi.testapp:id/my_text_field']")

    ad.quit()   # 对象销毁
    print("执行完毕")


