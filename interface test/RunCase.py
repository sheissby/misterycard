# encoding: utf-8
import unittest
import os
import datetime
import HTMLTestRunner


def run_case():
    case_path = 'TestCase'
    test = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern='case*.py', top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            test.addTest(test_case)
    # runner = unittest.TextTestRunner()
    # runner.run(test)
    fp = file(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'xxx测试报告',
        description=u'xxxx用例执行情况：')
    runner.run(test)
    print runner
    fp.close()


if __name__ == "__main__":
    report_path = os.getcwd()+'\\report\\result.html'
    # fp = file(report_path, 'wb')
    run_case()
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'xxx测试报告',
    #     description=u'xxxx用例执行情况：')
    # runner.run(run_case.test)
    # fp.close()
