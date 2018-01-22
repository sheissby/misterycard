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
from haiyi_zdh.public.firefox import login

#案例
class zdh_rjxz_del(unittest.TestCase):
    def setUp(self):
        #调用登录函数
        login.login_admin(self)
        
        #脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True

        #获取当前时间的函数
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        #软件下载标题加当前时间的函数
        self.del_text='rjxz_del'+now
        
    def test_zdh_rjxz_del(self):
        u"""删除"""
        
        #打开浏览器
        driver = self.driver
    
        #定位信息发布与共享模块
        above=driver.find_element_by_xpath(".//*[@id='nav-c75240a6-fb3c-4efb-8af1-536993800d4a']/a")
        #鼠标移至信息发布与共享模块
        ActionChains(driver).move_to_element(above).perform()
        #点击软件下载导航链接
        driver.find_element_by_xpath(".//*[@id='nav-60bd5c9d-beff-496d-ac6f-9cc6c10aca6c']/a").click()
        #将滚动条拉到最下方
        js="var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        
        #点击软件下载添加导航链接
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[7]/div/a[2]").click()
        #思考时间
        time.sleep(2)

        #在信息发布与共享模块下的软件下载添加中
        #定位到框架
        driver.switch_to_frame("diaConIf")
        
        #点击添加按钮，打开软件下载添加页面
        driver.find_element_by_id("btnAddTask").click()
        time.sleep(1)
        
        #获取添加页面的上层窗口和本层窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
              
        #输入标题和内容字段 
        driver.find_element_by_id("txtTitle").send_keys(self.del_text)        
        
        #定位到附件
        driver.find_element_by_id("uploadFile").send_keys("")

        #模拟键盘操作
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(2)
         
        #调用auto工具保存的附件上传EXE文件
        os.startfile(os.getcwd().split('testcase_firefox')[0]+'\uploadfile\Fox_fgw_doc.exe')
        time.sleep(4)
        
        #获取添加页面的窗口
        driver.switch_to_window(allhandles[1])
        time.sleep(2)
        
        #点击添加
        driver.find_element_by_xpath(".//*[@id='btnAddTask']").click()

        #接受告警信息，确定、取消页面
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(1)

        #接受告警信息，添加
        alert = driver.switch_to_alert()
        text=alert.text
        alert.accept()
        time.sleep(1)
        
        try:
            self.assertEqual(u'上传成功', text)
            print u'添加信息，名称“'+self.del_text+'”，添加成功' 
        except AssertionError as e:
            print u'添加信息，名称“'+self.del_text+'”，添加失败'

        time.sleep(2)        
        #完成添加功能
        #检查是否在软件下载添加的信息列表
        #获取软件下载添加列表的窗口
        driver.switch_to_window(allhandles[0])
        time.sleep(2)
        #定位到软件下载模块的查询框架
        driver.switch_to_frame("diaConIf")
                
        #输入标题查询字段
        driver.find_element_by_id("txtTitle").send_keys(self.del_text)
        
        #点击查询
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)

        #结果是否显示正确
        try:
            text=driver.find_element_by_xpath(".//*[@id='tbdata']/tr[1]/td[1]").text
            self.assertEqual(text, self.del_text)
            print u'软件下载添加的信息列表里存在，名称“'+self.del_text+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'软件下载添加的信息列表里没有存在，名称“'+self.del_text+u'”'
        time.sleep(2)
     
        #完成添加列表的结果查看功能

        #进行删除
        #点击删除按钮
        driver.find_element_by_xpath(".//*[@id='tbdata']/tr[1]/td[3]/a").click()

        #接受告警信息,判断是否有取消按钮
        alert = driver.switch_to_alert()
        alert.dismiss()
        time.sleep(1)
        print u'存在确定、取消对话框，取消功能正常'

        #获取结果列表页面的本层窗口
        driver.switch_to_window(allhandles[0])

        #定位到框架
        driver.switch_to_frame("diaConIf")
        
        #取消删除后重新查询该数据
        #输入标题查询字段
        driver.find_element_by_id("txtTitle").clear()
        driver.find_element_by_id("txtTitle").send_keys(self.del_text)
        
        #点击查询
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)

        #结果是否显示正确
        try:
            text=driver.find_element_by_xpath(".//*[@id='tbdata']/tr[1]/td[1]").text
            self.assertEqual(text, self.del_text)
            print u'取消删除后添加的信息列表里存在，名称“'+self.del_text+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'取消删除后添加的信息列表里不存在，名称“'+self.del_text+u'”'
        time.sleep(2)
     
        #完成取消删除后的结果查看功能

        #进行删除对话框确定按钮的判断
        #点击删除按钮
        driver.find_element_by_xpath(".//*[@id='tbdata']/tr[1]/td[3]/a").click()
        #接受告警信息,判断是否有确定按钮
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(1)
        print u'存在确定、取消对话框，确定功能正常' 
        
        text=alert.text        
        #删除成功判断
        try:
            self.assertEqual(u'删除成功', text)
            print u'删除信息，名称“'+self.del_text+u'”，删除成功提示语' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'删除信息，名称“'+self.del_text+u'”，删除失败提示语'  

        #关闭删除成功页面
        alert.accept()
        time.sleep(1)

        #获取软件下载列表页面的本层窗口
        driver.switch_to_window(allhandles[0])
        
        #进行删除后的查询
        #定位到框架
        driver.switch_to_frame("diaConIf")
        #输入标题查询字段
        driver.find_element_by_id("txtTitle").clear()
        driver.find_element_by_id("txtTitle").send_keys(self.del_text)
        
        #点击查询
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)
        
        #结果是否显示正确
        #获取整体结果列表的ID
        table=driver.find_element_by_id("tbdata")
        #列表标签多个行定义，包含标题行
        tr=table.find_elements_by_tag_name("tr")
        
        #进行删除后查询结果判断，是否大于1行，
        if len(tr)>1:
            self.verificationErrors.append('del fail')
            print self.del_text+u'软件下载添加页面删除数据失败'
        else :
            print self.del_text+u'软件下载添加页面删除数据成功'
        time.sleep(2)
        #完成软件下载添加页面删除后的结果验证功能


        #检查是否在软件下载的信息列表已删除数据
        #获取当前窗口
        nowhandle=driver.current_window_handle
        #回到原窗口
        driver.switch_to_window(nowhandle)
        
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[7]/div/a[1]").click()
        #思考时间
        time.sleep(2)
        
        #获取软件下载添加列表的窗口
        driver.switch_to_window(allhandles[0])
        time.sleep(2)
        #定位到软件下载模块的查询框架
        driver.switch_to_frame("diaConIf")
                
        #输入标题查询字段
        driver.find_element_by_id("txtTitle").send_keys(self.del_text)
        
        #点击查询
        driver.find_element_by_id("btnSearch").click()
        time.sleep(1)

        #结果是否显示正确
        #获取整体结果列表的ID
        table=driver.find_element_by_id("tbdata")
        #列表标签多个行定义，包含标题行
        tr=table.find_elements_by_tag_name("tr")
        
        #进行删除后查询结果判断，是否大于1行，
        if len(tr)>1:
            self.verificationErrors.append('del fail')
            print self.del_text+u'软件下载页面删除数据失败'
        else :
            print self.del_text+u'软件下载页面删除数据成功'
        time.sleep(2)
        #完成软件下载页面删除后的结果验证功能
     
    
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
