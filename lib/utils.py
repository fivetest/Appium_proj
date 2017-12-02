#!/usr/bin/env python
# 工具函数
# 此文件主要把一些常用的操作封装，方便使用
import os
import time


def capture_screen_shot(driver, file_path=None):
    """
    目的：对手机屏幕进行截图保存
    如果没有指定目录，则放到screen_shots目录下
    如果指定，则使用用户指定目录
    """
    if file_path is None:
        if not os.path.exists("./screen_shots"):
            # 判断截图目录是否存在，不存在则创建
            os.makedirs("./screen_shots")
        driver.get_screenshot_as_file(filename='./screen_shots/woody_%s.png'
                                           % time.strftime("%Y-%m-%d %H-%M-%S"))
    else:
        driver.get_screenshot_as_file(file_path)


def swipeToDown(driver, duration=200):
    """向下滑动，"""
    x = driver.get_window_size()['width']
    # 获取屏幕宽
    y = driver.get_window_size()['height']
    # 向下滑动
    driver.swipe(1 / 2 * x, 6 / 7 * y, 1 / 2 * x, 1 / 7 * y, duration)



def swipeToUp():
    """向下滑动，"""
    pass
