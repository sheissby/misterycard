# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re,os
from HnaCargo.public.firefox import login
from PIL import ImageGrab
import win32api
import win32con
import traceback
import datetime

class zdh_gswddl_add(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.today = datetime.date.today()
        self.tom_day=self.today+datetime.timedelta(days=1)
        self.wjbt='zdh_hygghs_add'+now
        self.ydqx=u'全公司'
        self.name=u'wxl员工'
        self.agent=u'wxl代理'
        self.hs='wxl_test2'
        self.img_text='img_pjff_add_error'
        print u'---------------《添加公司文档-代理功能自动化测试》----------------------'
    
    def test_gswddl_add(self):
        u"""添加公司文档-代理"""
        login.login_hs(self)
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='form1']/div[3]/div[1]/ul[1]/li[1]/ul/li[5]/a").click()
        time.sleep(1)
        above=driver.find_element_by_xpath(".//*[@id='form1']/div[3]/div[2]/ul/li[3]/a/span/s[1]")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='form1']/div[3]/div[2]/ul/li[3]/ul/li[3]/a/span/s[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='topic']/div[1]/ul/li[2]").click()
        #添加公司文档-代理信息
        print u'开始添加公司文档-代理：'+self.wjbt
        driver.find_element_by_id("btnShowEdit").click()
        time.sleep(1)
        frame=driver.find_element_by_css_selector('.pop')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        driver.find_element_by_id("txbTitle").send_keys(self.wjbt)
        driver.find_element_by_id("txbDocNumber").send_keys(self.wjbt)
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='UpLoader1manual-fine-uploader']/div/div[2]/input").click()
        os.startfile(os.getcwd().split('testcase_firefox')[0]+'\uploadfile\Fox_fgw_doc.exe')
        time.sleep(4)
        driver.find_element_by_id("btnSave").click()
        #等待返回的添加信息
        driver.switch_to.default_content()
        for i in range(30):
            try:
                ul=driver.find_element_by_id("noty_center_layout_container")
                button=ul.find_elements_by_tag_name('button')
                if u'确定' == button[0].text:
                    span=ul.find_elements_by_tag_name('span')
                    #点击确定按钮
                    button[0].click()
                    print span[0].text
                    break
            except: pass
            time.sleep(1)
        else:
            print u'添加公司文档-代理没有返回确定信息'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'1.png')
            time.sleep(1)
            print u'【错误截图】：'+self.img_text+'1.png'
            self.verificationErrors.append("time out")
        print u'完成添加公司文档-代理：'+self.wjbt
        #检查添加添加例会纪要信息是否正确
        print u'开始检查添加公司文档-代理信息是否正确'
        time.sleep(1)
        driver.find_element_by_id("MainContent_txbTitle").send_keys(self.wjbt)
        driver.find_element_by_id("MainContent_txbCreator").send_keys(self.name)
        time.sleep(1)
        driver.find_element_by_id("lkbtnSearch").click()
        time.sleep(2)
        #检查文号
        try:
            text=driver.find_element_by_xpath(".//*[@id='topic']/div[2]/div[2]/table/tbody/tr/td[2]/span").text
            self.assertEqual(self.wjbt, text)
            print u'添加公司文档-代理信息，文号信息正确：'+text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加公司文档-代理信息，文号信息有误：'+text
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'2.png')
            print u'错误截图：'+self.img_text+'2.png'
        #检查标题
        try:
            text=driver.find_element_by_xpath(".//*[@id='topic']/div[2]/div[2]/table/tbody/tr/td[3]/div[1]/a/span").text
            self.assertEqual(self.wjbt, text)
            print u'添加公司文档-代理信息，标题信息正确：'+text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加公司文档-代理信息，标题信息有误：'+text
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'3.png')
            print u'错误截图：'+self.img_text+'3.png'
        #检查上传人
        try:
            text=driver.find_element_by_xpath(".//*[@id='topic']/div[2]/div[2]/table/tbody/tr/td[6]").text
            self.assertEqual(self.name, text)
            print u'添加公司文档-代理信息，上传人信息正确：'+text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加公司文档-代理信息，上传人信息有误：'+text
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'4.png')
            print u'错误截图：'+self.img_text+'4.png'
        print u'完成检查添加公司文档-代理信息是否正确'
        driver.quit()
        print u'开始用代理人"'+self.agent+'"检查是否存在添加公司文档-代理，且信息是否正确'
        #用代理人账号查询刚添加的公司文档-代理信息
        login.login_agent(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='form1']/div[3]/div[3]/div/div[3]/ul/li[3]/a/s/span").click()
        time.sleep(1)
        allhandles=driver.window_handles
        time.sleep(1)
        driver.switch_to_window(allhandles[1])
        driver.find_element_by_id("MainContent_txbTitle").send_keys(self.wjbt)
        driver.find_element_by_id("MainContent_txbCreator").send_keys(self.name)
        time.sleep(1)
        driver.find_element_by_id("lkbtnSearch").click()
        time.sleep(2)
        #检查文号
        try:
            text=driver.find_element_by_xpath(".//*[@id='form1']/div[3]/div[3]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]").text
            self.assertEqual(self.wjbt, text)
            print u'添加公司文档-代理信息，文号信息正确：'+text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加公司文档-代理信息，文号信息有误：'+text
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'5.png')
            print u'错误截图：'+self.img_text+'5.png'
        #检查标题
        try:
            text=driver.find_element_by_xpath(".//*[@id='form1']/div[3]/div[3]/div/div[2]/div/div[2]/table/tbody/tr/td[3]/a/span").text
            self.assertEqual(self.wjbt, text)
            print u'添加公司文档-代理信息，标题信息正确：'+text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加公司文档-代理信息，标题信息有误：'+text
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'6.png')
            print u'错误截图：'+self.img_text+'6.png'
        #检查上传人
        try:
            text=driver.find_element_by_xpath(".//*[@id='form1']/div[3]/div[3]/div/div[2]/div/div[2]/table/tbody/tr/td[6]").text
            self.assertEqual(self.name, text)
            print u'添加公司文档-代理信息，上传人信息正确：'+text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加公司文档-代理信息，上传人信息有误：'+text
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'7.png')
            print u'错误截图：'+self.img_text+'7.png'
        print u'完成用代理人"'+self.agent+'"检查是否存在添加的公司文档-代理信息，且信息是否正确'
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
        error=traceback.format_exc()
        if 'errorhandler.py' in error:
            ImageGrab.grab().save(os.getcwd().split('testcase')[0]+'\\img\\'+self.img_text+'end_exceptional.png')
            time.sleep(1)
            print u'【异常错误截图】：'+self.img_text+'_exceptional.png'
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
