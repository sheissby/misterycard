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

class zdh_bmtxl_del(unittest.TestCase):
    def setUp(self):
        login.login_admin(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.del_text='del'+now[2:]
        self.del_num='95071000'
        self.sort=1
        self.img_text='img_zdh_bmtxl_error'
    
    def test_zdh_bmtxl_del(self):
        u"""删除部门通信录"""
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
        driver.find_element_by_xpath(".//*[@id='txtOrganName']").send_keys(self.del_text)
        driver.find_element_by_xpath(".//*[@id='txbMobilePhoneNum']").send_keys(self.del_num)
        driver.find_element_by_xpath(".//*[@id='txbNameOrder']").send_keys(str(self.sort))
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(2)
        alert=driver.switch_to_alert()
        text=alert.text
        alert.accept()
        try:
            self.assertEqual(u'添加成功', text)
            print u'添加部门通信录，部门名称“'+self.del_text+'”，添加成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加部门通信录，部门名称“'+self.del_text+'”，添加失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'1.png')
            print u'错误截图：'+self.img_text+'1.png'
        time.sleep(2)
        #完成添加
        driver.switch_to_default_content()
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbName']").send_keys(self.del_text)
        driver.find_element_by_xpath(".//*[@id='Imagbut']").click()
        try :
            driver.find_element_by_xpath(".//*[@id='gvPhoneList_ctl02_linkBtnDelete']").click()
        except:
            self.verificationErrors.append('add date fail')
            print u'部门通信录列表里没有存在，名称“'+self.del_text+'”退出测试'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'3.png')
            print u'错误截图：'+self.img_text+'3.png'
            return
        time.sleep(1)
        alert=driver.switch_to_alert()
        alert.accept()
        time.sleep(1)
        alert=driver.switch_to_alert()
        text=alert.text
        alert.accept()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='txbName']").clear()
        driver.find_element_by_xpath(".//*[@id='txbName']").send_keys(self.del_text)
        driver.find_element_by_xpath(".//*[@id='Imagbut']").click()
        table=driver.find_element_by_id("gvPhoneList")
        tr=table.find_elements_by_tag_name("tr")
        if text!=u'删除成功' or len(tr)>1:
            self.verificationErrors.append('del fail')
            print u'查看部门通信录，存在部门名称“'+self.del_text+u'”，删除失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'4.png')
            print u'错误截图：'+self.img_text+'4.png'
        else : print u'查看部门通信录，不存在部门名称“'+self.del_text+u'”，删除成功'
        time.sleep(2)
        driver.quit()
        login.login_normal(self)
        driver = self.driver
        above=driver.find_element_by_xpath(".//*[@id='nav-e7c0b5a6-028c-423d-a564-b35e4613947c']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='nav-772c5861-6056-458f-ba5d-aa0675ed88ff']/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/div/a[1]").click()
        time.sleep(1)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbName']").clear()
        driver.find_element_by_xpath(".//*[@id='txbName']").send_keys(self.del_text)
        driver.find_element_by_xpath(".//*[@id='Imagbut']").click()
        table=driver.find_element_by_id("gvPhoneList")
        tr=table.find_elements_by_tag_name("tr")
        if text!=u'删除成功' or len(tr)>1:
            self.verificationErrors.append('del fail')
            print u'普通用户查看部门通信录，存在部门名称“'+self.del_text+u'”，删除失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'5.png')
            print u'错误截图：'+self.img_text+'5.png'
        else : print u'普通用户查看部门通信录，不存在部门名称“'+self.del_text+u'”，删除成功'
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
