#!/usr/bin/env python
import unittest
from lib.AndroidDriver import AndroidDriver


class WoodyApps(unittest.TestCase):
    # def test_swipe_down(self):
    #     """打开啄木鸟的app， 向下滑动，然后检查日期的按钮是否能看见"""
    #     ad = AndroidDriver()
    #     ad.swipe_to_down()
    #     # 需要确认按钮能否找到
    #     self.assertTrue(ad.is_element_appearance('cc.liushi.testapp:id/date_button'))
    #     # 截图
    #     ad.capture_screenshots()
    #
    #
    # def test_popup_window(self):
    #     """"点击按钮，指定文本会显示出来"""
    #     ad = AndroidDriver()
    #     ad.click_by_id('showPopupWindowButtonCD')
    #     ad.capture_screenshots()

    def test_text_is_visible(self):
        """点击一个按钮以后，文本会显出"""
        ad = AndroidDriver()
        # 检查目标文本没有出现
        self.assertFalse(ad.is_element_appearance("//android.widget.TextView[@text='文本会显示']"))
        ad.click_by_id("cc.liushi.testapp:id/visibleButtonTest")
        # 检查目标文本应该出现
        self.assertTrue(ad.is_element_appearance("//android.widget.TextView[@text='文本会显示']"))
        ad.capture_screenshots()