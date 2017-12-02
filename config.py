#!/usr/bin/env python

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