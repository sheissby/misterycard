#coding=utf-8
import unittest
import os ,time
import HTMLTestRunner
from public import sendreport_firefox
#获取脚本文件夹

def creatsuite_firefox():
    #定义脚本的相对路径
    list_firefox=os.getcwd()+'\\testcase_firefox'
    testunit=unittest.TestSuite()
    #discover 方法定义，获zdh_前缀的py脚本
    discover=unittest.defaultTestLoader.discover(list_firefox,
                                                 pattern ='zdh_*.py',
                                                 top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    i=0
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
##            print testunit
            i=i+1
    print u'用例数为：'+str(i)
    #保存测试报告
    now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
    #定义报告的相对路径
    filename = os.getcwd()+'\\report\\firefox\\firefox_'+now+'result.html'
    fp = file(filename, 'wb')
    runner_firefox =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'firefox_海医OA自动化测试报告',
        description=u'firefox_海医OA自动化用例执行情况：')
    runner_firefox.run(testunit)
    #一定要有fp.close()，否则当前生成的报告内容为空
    fp.close()
    #调用sendreport发送邮件
    #sendreport_firefox.sendreport()

    #执行测试用例
if __name__ == "__main__":
    creatsuite_firefox()
