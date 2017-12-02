#!/usr/bin/env python
import time
import unittest
from appium import webdriver
from config import woody_app_desired_caps
from lib.utils import *

class WoodyApps(unittest.TestCase):
    def setUp(self):
        appium_url = 'http://127.0.0.1:4723/wd/hub'  # hub 服务器
        self.driver = webdriver.Remote(appium_url, woody_app_desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_swipe_down(self):
        driver = self.driver
        swipeToDown(driver, 300)   # 向下滑动
        # 验证拖到地了，查看日期的按钮可见
        elem = driver.find_element_by_id("cc.liushi.testapp:id/date_button")
        self.assertTrue(elem)
        capture_screen_shot(driver)  # 截图
