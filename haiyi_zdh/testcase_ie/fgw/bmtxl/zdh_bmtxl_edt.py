# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re,os
from haiyi_zdh.public.ie import login
from PIL import ImageGrab

class zdh_bmtxl_edt(unittest.TestCase):
    def setUp(self):
        login.login_admin(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.add_text='add'+now[2:]
        self.edt_text='edt'+now[2:]
        self.add_num='95071000'
        self.edt_num='089868875951'
        self.sort=1
        self.img_text='img_bmtxl_edt_error'
    
    def test_zdh_bmtxl_edt(self):
        u"""修改部门通信录"""
        driver = self.driver
        driver.maximize_window()
        driver.find_element_by_xpath(".//*[@id='nav-e7c0b5a6-028c-423d-a564-b35e4613947c']/a").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/div/a[3]").click()
        time.sleep(1)
        driver.switch_to_frame("diaConIf")
        time.sleep(1)
        #添加信息
        driver.find_element_by_xpath(".//*[@id='BtAdd']").click()
        time.sleep(1)
        driver.switch_to_default_content()
        frame=driver.find_element_by_css_selector('.jBoxContent')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
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
            print u'添加部门通信录，部门名称“'+self.add_text+'”，添加成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加部门通信录，部门名称“'+self.add_text+'”，添加失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'1.png')
            print u'错误截图：'+self.img_text+'1.png'
        time.sleep(2)
        #完成添加
        driver.switch_to_default_content()
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbName']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='Imagbut']").click()
        try :
            driver.find_element_by_xpath(".//*[@id='gvPhoneList']/tbody/tr[2]/td[4]/a").click()
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'部门通信录列表里没有存在，名称“'+self.add_text+'”退出测试'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'2.png')
            print u'错误截图：'+self.img_text+'2.png'
            return
        time.sleep(1)
        driver.switch_to_default_content()
        frame=driver.find_element_by_css_selector('.jBoxContent')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        time.sleep(1)
        try:
            text=driver.find_element_by_xpath(".//*[@id='txtOrganName']").get_attribute('value')
            self.assertEqual(self.add_text, text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'部门通信录，部门名称“'+text+'”，与实际添加的"'+self.add_text+'不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'4.png')
            print u'错误截图：'+self.img_text+'4.png'
        try:
            text=driver.find_element_by_xpath(".//*[@id='txbMobilePhoneNum']").get_attribute('value')
            self.assertEqual(self.add_num, text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'部门通信录，电话号码“'+text+'”，与实际添加的"'+self.add_num+'不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'5.png')
            print u'错误截图：'+self.img_text+'5.png'
        try:
            text=driver.find_element_by_xpath(".//*[@id='txbNameOrder']").get_attribute('value')
            self.assertEqual(str(self.sort), text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'部门通信录，排序值“'+text+'”，与实际添加的"'+str(self.sort)+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'6.png')
            print u'错误截图：'+self.img_text+'6.png'
        driver.find_element_by_xpath(".//*[@id='txtOrganName']").clear()
        driver.find_element_by_xpath(".//*[@id='txtOrganName']").send_keys(self.edt_text)
        driver.find_element_by_xpath(".//*[@id='txbMobilePhoneNum']").clear()
        driver.find_element_by_xpath(".//*[@id='txbMobilePhoneNum']").send_keys(self.edt_num)
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(2)
        alert=driver.switch_to_alert()
        text=alert.text
        alert.accept()
        try:
            self.assertEqual(u'修改成功', text)
            print u'部门通信录，部门名称“'+self.edt_text+'”，修改成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'部门通信录，部门名称“'+self.edt_text+'”，修改失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'7.png')
            print u'错误截图：'+self.img_text+'7.png'
        time.sleep(2)
        #检查是否在管理的信息列表里
        driver.switch_to_default_content()
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbName']").clear()
        driver.find_element_by_xpath(".//*[@id='txbName']").send_keys(self.edt_text)
        driver.find_element_by_xpath(".//*[@id='Imagbut']").click()
        time.sleep(1)
        try:
            text=driver.find_element_by_xpath(".//*[@id='gvPhoneList']/tbody/tr[2]/td[1]").text
            self.assertEqual(text, self.edt_text)
            print u'部门通信录列表里存在，部门通信录修改后名称“'+self.edt_text+'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'部门通信录列表里没有存在，部门通信录修改后名称“'+self.edt_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'8.png')
            print u'错误截图：'+self.img_text+'8.png'
        try:
            text=driver.find_element_by_xpath(".//*[@id='gvPhoneList']/tbody/tr[2]/td[2]").text
            self.assertEqual(text, self.edt_num)
            print u'部门通信录修改后名称“'+self.edt_text+'”的电话号码修改正确:'+text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'部门通信录修改后名称“'+self.edt_text+'”的电话号码修改失败:'+text
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'9.png')
            print u'错误截图：'+self.img_text+'9.png'
        time.sleep(2)
        driver.quit()
        login.login_normal(self)
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='nav-e7c0b5a6-028c-423d-a564-b35e4613947c']/a").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/div/a[1]").click()
        time.sleep(1)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbName']").clear()
        driver.find_element_by_xpath(".//*[@id='txbName']").send_keys(self.edt_text)
        driver.find_element_by_xpath(".//*[@id='Imagbut']").click()
        time.sleep(1)
        try:
            text=driver.find_element_by_xpath(".//*[@id='gvPhoneList']/tbody/tr[2]/td[1]").text
            self.assertEqual(text, self.edt_text)
            print u'普通用户查看部门通信录列表，存在部门通信录修改后名称“'+self.edt_text+'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'普通用户查看部门通信录列表，没有存在部门通信录修改后名称“'+self.edt_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'10.png')
            print u'错误截图：'+self.img_text+'10.png'
        try:
            text=driver.find_element_by_xpath(".//*[@id='gvPhoneList']/tbody/tr[2]/td[2]").text
            self.assertEqual(text, self.edt_num)
            print u'普通用户查看部门通信录修改后名称“'+self.edt_text+'”的电话号码修改正确:'+text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'普通用户查看部门通信录修改后名称“'+self.edt_text+'”的电话号码修改失败:'+text
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'11.png')
            print u'错误截图：'+self.img_text+'11.png'
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
