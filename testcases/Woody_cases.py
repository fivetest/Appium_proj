#!/usr/bin/env python
import unittest
from lib.AndroidDriver import AndroidDriver


class WoodyApps(unittest.TestCase):
    def test_swipe_down(self):
        """打开啄木鸟的app， 向下滑动，然后检查日期的按钮是否能看见"""
        ad = AndroidDriver()
        ad.swipe_to_down()
        # 需要确认按钮能否找到
        self.assertTrue(ad.is_element_appearance('cc.liushi.testapp:id/date_button'))
        # 截图
        ad.capture_screenshots()