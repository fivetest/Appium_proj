#!/usr/bin/env python
from testcases.Woody_cases import WoodyApps
import unittest


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(WoodyApps))
    return suite


if __name__ == "__main__":
    suite = get_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)

