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

class zdh_bmtxl_sch(unittest.TestCase):
    def setUp(self):
        login.login_admin(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.add_sch_text='sch'+now[2:]
        self.sch_num='95071000'
        self.sort=1
        self.sch_text='sch'
        self.img_text='img_bmtxl_add_error'
    
    def test_zdh_bmtxl_sch(self):
        u"""查询部门通信录"""
        driver = self.driver
        driver.maximize_window()
        above=driver.find_element_by_xpath(".//*[@id='nav-e7c0b5a6-028c-423d-a564-b35e4613947c']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='nav-772c5861-6056-458f-ba5d-aa0675ed88ff']/a").click()
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
        driver.find_element_by_xpath(".//*[@id='txtOrganName']").send_keys(self.add_sch_text)
        driver.find_element_by_xpath(".//*[@id='txbMobilePhoneNum']").send_keys(self.sch_num)
        driver.find_element_by_xpath(".//*[@id='txbNameOrder']").send_keys(str(self.sort))
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(2)
        alert=driver.switch_to_alert()
        text=alert.text
        alert.accept()
        try:
            self.assertEqual(u'添加成功', text)
            print u'添加部门通信录，部门名称“'+self.add_sch_text+'”，添加成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加部门通信录，部门名称“'+self.add_sch_text+'”，添加失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'1.png')
            print u'错误截图：'+self.img_text+'1.png'
        time.sleep(2)
        #完成添加
        driver.switch_to_default_content()
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbName']").send_keys(self.sch_text)
        driver.find_element_by_xpath(".//*[@id='Imagbut']").click()
        time.sleep(1)
        try:
            text=driver.find_element_by_xpath(".//*[@id='gvPhoneList']/tbody/tr[2]/td[1]").text
            if self.sch_text in text:
                print u'模糊查询"'+self.sch_text+'"存在包含"'+self.sch_text+'"的名称'+text
            else:
                raise NameError('Query failed')
                print u'模糊查询"'+self.sch_text+'"没有存在包含"'+self.sch_text+'"的名称:'+text
                ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'2.png')
                print u'错误截图：'+self.img_text+'2.png'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'查询信息失败'
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
