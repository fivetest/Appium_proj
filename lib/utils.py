#!/usr/bin/env python
# 此文件主要把一些常用的操作封装，方便使用
import time


def capture_screen_shot(driver, file_path=None):
    """
    目的：对手机屏幕进行截图保存
    如果没有指定目录，则放到screen_shots目录下
    如果指定，则使用用户指定目录
    """
    if file_path is None:
        driver.get_screenshot_as_file(filename='./screen_shots/woody_%s.png'
                                           % time.strftime("%Y-%m-%d %H-%M-%S"))
    else:
        driver.get_screenshot_as_file(file_path)