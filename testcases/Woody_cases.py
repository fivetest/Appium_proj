#!/usr/bin/env python
import time
import unittest
from appium import webdriver
from config import woody_app_desired_caps


class WoodyApps(unittest.TestCase):
    def setUp(self):
        appium_url = 'http://127.0.0.1:4723/wd/hub'  # hub 服务器
        self.driver = webdriver.Remote(appium_url, woody_app_desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_swipe_down(self):
        driver = self.driver
        x = driver.get_window_size()['width']
        # 获取屏幕宽
        y = driver.get_window_size()['height']
        # 向下滑动
        driver.swipe(1 / 2 * x, 6 / 7 * y, 1 / 2 * x, 1 / 7 * y, 200)

        # 验证拖到地了，查看日期的按钮可见
        elem = driver.find_element_by_id("cc.liushi.testapp:id/date_button")
        self.assertTrue(elem)
        driver.get_screenshot_as_file(filename='./screen_shots/woody_%s.png' % time.strftime("%Y-%m-%d %H-%M-%S"))
