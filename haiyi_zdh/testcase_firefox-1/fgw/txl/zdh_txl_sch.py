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
class zdh_txl_sch(unittest.TestCase):
    def setUp(self):
        #调用登录函数
        login.login_admin(self)
        
        #脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True

        #通讯录标题
        self.sch_text=u'系统管理'
        #通讯录移动电话
        self.sch_text2=u'13398992001'    
        
    def test_zdh_txl_sch(self):       

        #打开浏览器
        driver = self.driver
    
        #定位系统管理模块
        above=driver.find_element_by_xpath(".//*[@id='nav-c6abd596-d35c-468c-b3a4-f167d5be1ee1']/a")
        #鼠标移至系统管理模块
        ActionChains(driver).move_to_element(above).perform()
        #点击公共信息管理导航链接
        driver.find_element_by_xpath(".//*[@id='nav-a6ce5b2e-7e0d-4340-a2e3-a749b9bca5cd']/a").click()
        #点击通讯录管理导航链接
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[3]/div/a[2]").click()
        #思考时间
        time.sleep(2)

        #在通讯录管理的添加中
        #定位到框架
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("phoneList")
        
        #点击添加按钮，打开通讯录添加页面
        driver.find_element_by_id("BtAdd").click()
        time.sleep(1)
        
        #定位到框架
        #定位到当前窗口
        driver.switch_to_default_content()
        #找div class="jBoxContent"
        frame=driver.find_element_by_css_selector('.jBoxContent')

        #遍历下方的iframe
        frames=frame.find_elements_by_tag_name('iframe')
        #取第1个iframe
        driver.switch_to_frame(frames[0])

        driver.find_element_by_id("txbOfficePhoneNum").send_keys(u"089812345678")
        driver.find_element_by_id("txbMobilePhoneNum").send_keys(self.sch_text2)
        driver.find_element_by_id("txbExtensionNum").send_keys(u"123@126.com")
        driver.find_element_by_id("txbNameOrder").send_keys(u"1")
        driver.find_element_by_id("ucName_imgBt").click()

        #定位到人员选择页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        time.sleep(2)

        #定位到框架
        driver.switch_to_frame("mainFrame")
        
        #输入查询人员
        driver.find_element_by_id("tb_Search").send_keys(self.sch_text)
        #点击查询、添加、提交人员
        driver.find_element_by_id("btn_Search").click()
        driver.find_element_by_id("ibtAddMsg").click()
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(2)
        
        #定位到添加窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])
        #定位到框架
        #找div class="jBoxContent"
        frame=driver.find_element_by_css_selector('.jBoxContent')
        #遍历下方的iframe
        frames=frame.find_elements_by_tag_name('iframe')
        #取第1个iframe
        driver.switch_to_frame(frames[0])

        #提交通讯录
        driver.find_element_by_id("ibtSubmit").click()

        #接受告警信息
        alert = driver.switch_to_alert()
        text=alert.text
        alert.accept()
        time.sleep(1)

        try:
            self.assertEqual(u'添加成功', text)
            print u'添加用户的通讯录成功' 
        except AssertionError as e:
            print u'添加用户的通讯录失败'

        #检查是否在信息列表
        #获取列表的窗口
        driver.switch_to_window(allhandles[0])
        time.sleep(2)
        #定位到通讯录模块的查询框架
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("phoneList")
       
        #输入标题查询字段
        driver.find_element_by_id("txbName").clear()
        driver.find_element_by_id("txbName").send_keys(self.sch_text2)
        
        #点击查询
        driver.find_element_by_id("Imagbut").click()
        time.sleep(1)

        #结果是否显示正确
        try:
            text=driver.find_element_by_xpath(".//*[@id='gvPhoneList']/tbody/tr[2]/td[3]").text
            self.assertEqual(text, self.sch_text2)
            print u'添加的信息列表里存在，移动电话为'+self.sch_text2+'用户' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加的信息列表里不存在，移动电话为'+self.sch_text2+'用户'
        time.sleep(2)

        #进行删除
        #点击删除按钮
        driver.find_element_by_xpath(".//*[@id='gvPhoneList_ctl02_linkBtnDelete']").click()
        time.sleep(1)

        #接受告警信息,判断是否有取消按钮
        alert = driver.switch_to_alert()
        alert.dismiss()
        time.sleep(1)
        print u'存在确定、取消对话框，取消功能正常'

        #取消删除后重新查询该数据
        #获取列表的窗口
        driver.switch_to_window(allhandles[0])
        time.sleep(2)
        #定位到通讯录模块的查询框架
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("phoneList")
       
        #输入标题查询字段
        driver.find_element_by_id("txbName").clear()
        driver.find_element_by_id("txbName").send_keys(self.sch_text2)
        
        #点击查询
        driver.find_element_by_id("Imagbut").click()
        time.sleep(1)

        #结果是否显示正确
        try:
            text=driver.find_element_by_xpath(".//*[@id='gvPhoneList']/tbody/tr[2]/td[3]").text
            self.assertEqual(text, self.sch_text2)
            print u'取消删除后添加的信息列表里存在，移动电话"'+self.sch_text2+'"用户"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'取消删除后添加的信息列表里不存在，移动电话"'+self.sch_text2+'"用户"'+u'”' 
        time.sleep(2)
        

        #完成取消删除后的结果查看功能

        #进行删除对话框确定按钮的判断
        #点击删除按钮
        driver.find_element_by_xpath(".//*[@id='gvPhoneList_ctl02_linkBtnDelete']").click()
        #接受告警信息,判断是否有确定按钮
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(1)
        print u'存在确定、取消对话框，确定功能正常' 

        text=alert.text        
        #删除成功判断
        try:
            self.assertEqual(u'删除成功', text)
            print u'删除信息，名称“'+self.sch_text2+u'”，删除成功提示语' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'删除信息，名称“'+self.sch_text2+u'”，删除失败提示语'  

        #关闭删除成功页面
        alert.accept()
        time.sleep(1)
        
        #进行删除后的查询
        #获取列表的窗口
        driver.switch_to_window(allhandles[0])
        time.sleep(2)
        #定位到通讯录模块的查询框架
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("phoneList")
       
        #输入标题查询字段
        driver.find_element_by_id("txbName").clear()
        driver.find_element_by_id("txbName").send_keys(self.sch_text2)
        
        #点击查询
        driver.find_element_by_id("Imagbut").click()
        time.sleep(1)

        #结果是否显示正确
        #获取整体结果列表的ID
        table=driver.find_element_by_id("gvPhoneList")
        #列表标签多个行定义，包含标题行
        tr=table.find_elements_by_tag_name("tr")
        
        #进行删除后查询结果判断，是否大于1行，
        if len(tr)>1:
            self.verificationErrors.append('del fail')
            print self.sch_text2+u'通讯录删除数据失败'
        else :
            print self.sch_text2+u'通讯录删除数据成功'
        time.sleep(2)
        #完成通讯录删除后的结果验证功能
                
  
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
