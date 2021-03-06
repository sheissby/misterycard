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
import win32api
import win32con
from PIL import ImageGrab

class zdh_dwgk_sch(unittest.TestCase):
    def setUp(self):
        login.login_admin(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.sch_text='sch'
        self.add_sch_text='dwgk_sch'+time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.img_text='img_dwgk_sch_error'
        
    def test_zdh_dwgk_sch(self):
        u"""查询党务公开"""
        driver = self.driver
        above=driver.find_element_by_xpath(".//*[@id='nav-c6abd596-d35c-468c-b3a4-f167d5be1ee1']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='nav-230f2b05-e78a-4ccb-acd7-e71265228739']/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/div/a[2]").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_xpath(".//*[@id='txbTitle']").send_keys(u'党务公开')
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
        #点击浏览范围的“选择”按钮
        driver.find_element_by_xpath(".//*[@id='Page_RightControlId_imgBt']").click()
        time.sleep(1)
        #获取点击选择按钮时的警告信息（请选择浏览范围）
        #alert = driver.switch_to_alert()
        #接收警告信息
        #alert.accept()
        time.sleep(1)
        #获得所有窗口
        allhandles=driver.window_handles
        #选择窗口3（即选择浏览范围的窗口）
        driver.switch_to_window(allhandles[2])
        #进入到frame（mainFrame）
        driver.switch_to_frame("mainFrame")
        #点击“添加”按钮
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(2)
        #点击“确认”按钮
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(1)
##        #选择窗口2（即添加窗口）
##        driver.switch_to_window(allhandles[1])
##        driver.find_element_by_xpath(".//*[@id='Control_aa4faa98_a91a_44ad_a311_90f695a8282f_IbtnAppend']").send_keys('')
##        win32api.keybd_event(13,0,0,0)
##        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
##        time.sleep(5)
##        allhandles=driver.window_handles
##        driver.switch_to_window(allhandles[2])
##        driver.switch_to_frame("PostFrame")
##        driver.find_element_by_xpath(".//*[@id='InputFile']").click()
##        time.sleep(1)
##        os.startfile(os.getcwd().split('testcase_Fox')[0]+'\uploadfile\Fox_fgw_doc.exe')
##        time.sleep(5)
##        driver.find_element_by_xpath(".//*[@id='IbtnPost']").click()
##        time.sleep(5)
##        driver.find_element_by_xpath(".//*[@id='IbtnClose']").click()
##        time.sleep(1)
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
        driver.find_element_by_xpath(".//*[@id='Control_605af416_b00c_4db9_9e0e_37f13214890d']").clear()
        driver.find_element_by_xpath(".//*[@id='Control_605af416_b00c_4db9_9e0e_37f13214890d']").send_keys(self.sch_text)
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
