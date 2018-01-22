# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#引用各种包
import unittest,time,re,os
#引用火狐插件包
from selenium.webdriver.firefox.webdriver import FirefoxProfile
#引用移动鼠标包
from selenium.webdriver.common.action_chains import ActionChains
#操作Windows应用程序 或者操作鼠标键盘用的包
import win32api
import win32con
#调用登录
from haiyi_zdh.public.ie import login

#案例
class zdh_rjxz_sch(unittest.TestCase):
    def setUp(self):
        #用户登录------------------------------------------------------------------------------------------
        #调用登录函数
        login.login_admin(self)
        #脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True

        #定义字段取值+++++++++++++++++++++++++++++++++++++++++
        #获取当前时间的函数
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        #软件下载标题加当前时间的函数
        self.sch_text='rjxz_sch'+now
        
        #显示用例名称
        print u'-------《软件下载查询功能测试》------------'
        
    def test_zdh_rjxz_sch(self):
        #打开信息发布与共享-软件下载-软件下载添加-------------------------------------------------------------------
        #打开浏览器
        driver = self.driver
        #赋窗口空值，获取当前窗口
        allhandlelist=[]
        nowhandle=driver.current_window_handle
        allhandlelist.append(nowhandle)
    
        #点击信息发布与共享模块
        driver.find_element_by_xpath(".//*[@id='nav-c75240a6-fb3c-4efb-8af1-536993800d4a']/a").click()
        time.sleep(1)
        #点击软件下载导航链接
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[7]/a").click()
        time.sleep(1)
        #滚动条拉到最下方
        js="var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        time.sleep(1)
        #点击软件下载添加导航链接
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[7]/div/a[2]").click()
        #思考时间
        time.sleep(1)

        #在信息发布与共享模块下的iframe框架+++++++++++++++++++++++++++
        #定位到框架
        driver.switch_to_frame("diaConIf")
        #点击添加按钮，打开软件下载添加页面
        driver.find_element_by_id("btnAddTask").click()
        time.sleep(1)   
        #获取添加页面的上层窗口和本层窗口
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))#与上层窗口作比较
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        
        #配置字段属性，点击提交-------------------------------------------------------------------------------        
        #输入标题和内容字段 
        driver.find_element_by_id("txtTitle").send_keys(self.sch_text)        
        time.sleep(1)
        
        #附件选择++++++++++++++++++++++++++++++++++++++++
        #定位到附件
        #定位到要双击的元素
        double =driver.find_element_by_id("uploadFile")
        #对定位到的元素执行鼠标双击操作
        ActionChains(driver).double_click(double).perform()
        #调用auto工具保存的附件上传EXE文件
        os.startfile(os.getcwd().split('testcase_ie')[0]+'\uploadfile\Ie_fgw_doc.exe')
        time.sleep(4)
        #获取添加页面的窗口
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        #点击添加
        driver.find_element_by_id("btnAddTask").click()

        #接受告警信息，确定、取消页面，确定+++++++++++++++++
        time.sleep(1)
        alert = driver.switch_to_alert()
        time.sleep(1)
        alert.accept()
        time.sleep(1)

        #接受告警信息，添加++++++++++++++++++++++++
        alert = driver.switch_to_alert()
        text=alert.text
        time.sleep(1)
        alert.accept()
        time.sleep(1)

        #进行提示语判断+++++++++++++++++
        try:
            self.assertEqual(u'上传成功', text)
            print u'添加信息，名称“'+self.sch_text+'”，添加成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加信息，名称“'+self.sch_text+'”，添加失败'
        time.sleep(1)
        
        #检查是否在软件下载添加的信息列表----------------------------------------------
        #删除之前已关闭消失的（没有的）窗口句柄
        allhandlelist.pop()
        #获取软件下载添加列表的窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #定位到软件下载模块的查询框架
        driver.switch_to_frame("diaConIf")
                
        #输入标题查询字段++++++++++++++++++++++++
        driver.find_element_by_id("txtTitle").send_keys(self.sch_text)
        #点击查询
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)

        #结果是否显示正确+++++++++++++++++++++++++
        try:
            text=driver.find_element_by_xpath(".//*[@id='tbdata']/tr[1]/td[1]").text
            self.assertEqual(text, self.sch_text)
            print u'软件下载添加的信息列表里存在，名称“'+self.sch_text+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'软件下载添加的信息列表里没有存在，名称“'+self.sch_text+u'”'
        time.sleep(1)
    
        #检查是否在软件下载的信息列表---------------------------------------------------
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)

        #点击软件下载导航链接
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[7]/div/a[1]").click()
        time.sleep(1)
        #获取软件下载列表的窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #定位到软件下载模块的查询框架
        driver.switch_to_frame("diaConIf")
                
        #输入标题查询字段+++++++++++++++++++++++++++
        driver.find_element_by_id("txtTitle").send_keys(self.sch_text)  
        #点击查询
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)

        #结果是否显示正确++++++++++++++++++++++++++++++
        try:
            text=driver.find_element_by_xpath(".//*[@id='tbdata']/tr[1]/td[1]").text
            self.assertEqual(text, self.sch_text)
            print u'软件下载的信息列表里存在，名称“'+self.sch_text+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'软件下载的信息列表里没有存在，名称“'+self.sch_text+u'”'
        time.sleep(1)

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
