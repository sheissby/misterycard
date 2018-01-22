# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re,os
from haiyi_zdh.public.firefox import login
from PIL import ImageGrab

class zdh_bmtxl_add(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.add_text='add'+now[2:]
        self.add_num='091335858421'
        self.sort=1
        self.img_text='img_bmtxl_add_error'
        print u'---------------《添加部门通信录功能自动化测试》----------------------'
    
    def test_zdh_bmtxl_add(self):
        u"""添加部门通信录"""
        login.login_admin(self)
        driver = self.driver
        print u'1.登录用户名判断:'
        try:
            self.assertEqual(u"系统管理", driver.find_element_by_link_text(u"系统管理").text)
            print u'(1)【通过】：系统管理登录，用户名显示系统管理正常' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'(1)【错误】：系统管理登录，用户名显示系统管理有误'
            #获取全屏截图，保存截图到指定路径
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'1.png')      
            time.sleep(1)
            print u'【错误截图】：'+self.img_text+'1.png'
        above=driver.find_element_by_xpath(".//*[@id='nav-e7c0b5a6-028c-423d-a564-b35e4613947c']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='nav-772c5861-6056-458f-ba5d-aa0675ed88ff']/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/div/a[3]").click()
        time.sleep(1)
        driver.switch_to_frame("diaConIf")
        time.sleep(1)
        #添加信息
        print u'2.添加部门通信录信息:'
        driver.find_element_by_xpath(".//*[@id='BtAdd']").click()
        time.sleep(1)
        driver.switch_to_default_content()
        frame=driver.find_element_by_css_selector('.jBoxContent')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        print frames
        return
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='txtOrganName']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='txbMobilePhoneNum']").send_keys(self.add_num)
        driver.find_element_by_xpath(".//*[@id='txbNameOrder']").send_keys(str(self.sort))
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(2)
        alert=driver.switch_to_alert()
        text=alert.text
        alert.accept()
        try:
            self.assertEqual(u'添加成功', text)
            print u'(1)【通过】：添加部门通信录，部门名称“'+self.add_text+'”，添加成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'(1)【错误】：添加部门通信录，部门名称“'+self.add_text+'”，添加失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'2.png')
            print u'错误截图：'+self.img_text+'2.png'
        time.sleep(2)
        #完成添加
        #检查是否在管理的信息列表里
        print u'3.检查部门通信录列表里是否存在新添加的信息:'
        driver.switch_to_default_content()
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbName']").clear()
        driver.find_element_by_xpath(".//*[@id='txbName']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='Imagbut']").click()
        time.sleep(1)
        try:
            text=driver.find_element_by_xpath(".//*[@id='gvPhoneList']/tbody/tr[2]/td[1]").text
            self.assertEqual(text, self.add_text)
            print u'(1)【通过】：添加的部门通信录列表里存在，部门通信录名称“'+self.add_text+'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'(1)【错误】：添加的部门通信录列表里没有存在，部门通信录名称“'+self.add_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'3.png')
            print u'错误截图：'+self.img_text+'3.png'
        time.sleep(2)
        driver.quit()
        login.login_normal(self)
        driver = self.driver
        print u'4.切换用户名判断:'
        try:
            self.assertEqual(u"冯学冠", driver.find_element_by_link_text(u"冯学冠").text)
            print u'(1)【通过】：切换用户为冯学冠登录，用户名显示符晓玲正常' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'(1)【错误】：切换用户为冯学冠登录，用户名显示符晓玲有误'
            #获取全屏截图，保存截图到指定路径
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'4.png')      
            time.sleep(1)
            print u'错误截图：'+self.img_text+'4.png'
        print u'5.普通用户查看部门通信录列表是否存在新添加的信息:'
        above=driver.find_element_by_xpath(".//*[@id='nav-e7c0b5a6-028c-423d-a564-b35e4613947c']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='nav-772c5861-6056-458f-ba5d-aa0675ed88ff']/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/div/a[1]").click()
        time.sleep(1)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbName']").clear()
        driver.find_element_by_xpath(".//*[@id='txbName']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='Imagbut']").click()
        time.sleep(1)
        try:
            text=driver.find_element_by_xpath(".//*[@id='gvPhoneList']/tbody/tr[2]/td[1]").text
            self.assertEqual(text, self.add_text)
            print u'(1)【通过】：普通用户查看部门通信录列表，存在部门通信录名称“'+self.add_text+'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'(1)【错误】：普通用户查看部门通信录列表，没有存在部门通信录名称“'+self.add_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'5.png')
            print u'错误截图：'+self.img_text+'5.png'
        time.sleep(2)
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
