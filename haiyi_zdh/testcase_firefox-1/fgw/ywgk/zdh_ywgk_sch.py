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

class zdh_ywgk_sch(unittest.TestCase):
    def setUp(self):
        login.login_admin(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.sch_text='sch'
        self.add_sch_text='ywgk_sch'+time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.img_text='img_ywgk_sch_error'
        
    def test_zdh_ywgk_sch(self):
        u"""查询院务公开"""
        driver = self.driver
        above=driver.find_element_by_xpath(".//*[@id='nav-c6abd596-d35c-468c-b3a4-f167d5be1ee1']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='nav-230f2b05-e78a-4ccb-acd7-e71265228739']/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/div/a[2]").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_xpath(".//*[@id='txbTitle']").send_keys(u'院务公开')
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtSearch']").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='dgBrowse']/tbody/tr[2]/td[5]/a").click()
        #添加信息
        time.sleep(1)
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").send_keys(self.add_sch_text)
        driver.find_element_by_xpath(".//*[@id='CustomrichTextBox']").send_keys(self.add_sch_text)
        #js="$(\"input[id='control_AuditedDateTime_txbDate']\").removeAttr('readonly');$(\"input[id='control_AuditedDateTime_txbDate']\").attr('value','2016-07-31')"
        #driver.execute_script(js)
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='Page_RightControlId_imgBt']").click()
        time.sleep(1)
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(1)
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[2])
        driver.switch_to_frame("mainFrame")
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(2)
        driver.find_element_by_id("ibtSubmit").click()
        driver.switch_to_window(allhandles[1])
        driver.find_element_by_xpath(".//*[@id='ibSaveAndContinue']").click()
        alert = driver.switch_to_alert()
        text=alert.text
        alert.accept()
        try:
            self.assertEqual(u'添加成功', text)
            print u'添加信息，名称“'+self.add_sch_text+'”，添加成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加信息，名称“'+self.add_sch_text+'”，添加失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'1.png')
            print u'【错误截图】：'+self.img_text+'1.png'
            return
        driver.close()
        time.sleep(2)
        #完成添加
        #查询信息
        driver.switch_to_window(allhandles[0])
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_xpath(".//*[@id='dgBrowse']/tbody/tr[2]/td[6]/a").click()
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        driver.find_element_by_xpath(".//*[@id='Control_326f92d9_e1a5_43aa_80d6_1281d32ab368']").clear()
        driver.find_element_by_xpath(".//*[@id='Control_326f92d9_e1a5_43aa_80d6_1281d32ab368']").send_keys(self.sch_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        time.sleep(1)
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[1]/a").text
            if self.sch_text in text:
                print u'模糊查询"'+self.sch_text+'"存在包含"'+self.sch_text+'"的名称'+text
            else:
                raise NameError('Query failed')
                print u'模糊查询"'+self.sch_text+'"没有存在包含"'+self.sch_text+'"的名称:'+text
                ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'2.png')
                print u'【错误截图】：'+self.img_text+'2.png'
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
