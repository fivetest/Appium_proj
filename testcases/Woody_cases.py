#!/usr/bin/env python
import time
from appium import webdriver
import unittest


class WoodyApps(unittest.TestCase):
    def setUp(self):
        woody_app_desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5',
            'deviceName': 'android',
            'appPackage': 'cc.liushi.testapp',
            'appActivity': '.HomeScreenActivity',
            # 'app': r'F:\GitHub\Appium_demo\app-debug.apk',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'newCommandTimeout': 600
        }
        appium_url = 'http://127.0.0.1:4723/wd/hub'  # hub 服务器
        self.driver = webdriver.Remote(appium_url, woody_app_desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_send_keys(self):
        self.assertEqual(1, 1)
