#!/usr/bin/env python
import time
import unittest

from lib.HTMLTestRunner import HTMLTestRunner
from testcases.WoodyApp.Woody_cases import WoodyApps


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(WoodyApps))
    return suite


if __name__ == "__main__":
    suite = get_suite()
    fp = open('./reports/results_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'啄木鸟移动APP测试报告',
        description=u"测试用例执行情况：")
    runner.run(suite)
    fp.close()

