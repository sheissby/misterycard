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
import win32api
import win32con
from PIL import ImageGrab

class zdh_yywh_add(unittest.TestCase):
    def setUp(self):
        login.login_admin(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.add_text='yyhw_add'+now
        self.img_text='img_yywh_add_error'
    
    def test_zdh_yywh_add(self):
        u"""添加医院文化"""
        driver = self.driver
        allhandlelist=[]
        nowhandle=driver.current_window_handle
        allhandlelist.append(nowhandle)
        above=driver.find_element_by_xpath(".//*[@id='nav-c6abd596-d35c-468c-b3a4-f167d5be1ee1']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='nav-230f2b05-e78a-4ccb-acd7-e71265228739']/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/div/a[2]").click()
        time.sleep(2)
        nowhandle=driver.current_window_handle
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_xpath(".//*[@id='txbTitle']").send_keys(u'医院文化')
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtSearch']").click()
        time.sleep(1)
        #添加信息
        driver.find_element_by_xpath(".//*[@id='dgBrowse']/tbody/tr[2]/td[5]/a").click()
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        #将获取当前所有窗口与allhandlelist的差集加到allhandlelist后面（连接到allhandlelist）
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").send_keys(self.add_text)
        # getElementById("iframe的ID")
        set_wyswyg_js = 'document.getElementById("CustomrichTextBox_editor").contentWindow.document.body.innerHTML="'+self.add_text+'"'
        driver.execute_script(set_wyswyg_js)
        #js="$(\"input[id='control_AuditedDateTime_txbDate']\").removeAttr('readonly');$(\"input[id='control_AuditedDateTime_txbDate']\").attr('value','2016-07-31')"
        #driver.execute_script(js)
        #点击浏览范围的“选择”按钮
        driver.find_element_by_xpath(".//*[@id='Page_RightControlId_imgBt']").click()
        #time.sleep(1)
        #获取点击选择按钮时的警告信息（请选择浏览范围）
        alert = driver.switch_to_alert()
        #接收警告信息
        alert.accept()
        time.sleep(1)
        #获得所有窗口
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        #选择窗口3（即选择浏览范围的窗口）
        driver.switch_to_window(allhandlelist[2])
        time.sleep(1)
        #进入到frame（mainFrame）
        driver.switch_to_frame("mainFrame")
        #点击“添加”按钮
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(2)
        #点击“确认”按钮
        driver.find_element_by_id("ibtSubmit").click()
        #删除没有的窗口句柄
        allhandlelist.pop()
        time.sleep(1)
        #选择窗口2（即添加窗口）
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='Control_e1210244_f06c_4386_9cd4_b59744a33179_IbtnAppend']").send_keys('')
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        driver.switch_to_window(allhandlelist[2])
        time.sleep(1)
        driver.switch_to_frame("PostFrame")
        #定位到要双击的元素
        double =driver.find_element_by_xpath(".//*[@id='InputFile']")
        #对定位到的元素执行鼠标双击操作
        ActionChains(driver).double_click(double).perform()
        time.sleep(1)
        os.startfile(os.getcwd().split('testcase_ie')[0]+'\uploadfile\Ie_fgw_doc.exe')
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='IbtnPost']").click()
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='IbtnClose']").click()
        time.sleep(1)
        #删除没有的窗口句柄
        allhandlelist.pop()
        #选择窗口2（即添加窗口）
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibSaveAndContinue']").click()
        alert = driver.switch_to_alert()
        text=alert.text
        alert.accept()
        try:
            self.assertEqual(u'添加成功', text)
            print u'添加信息，名称“'+self.add_text+'”，添加成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加信息，名称“'+self.add_text+'”，添加失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'1.png')
            print u'错误截图：'+self.img_text+'1.png'
        time.sleep(2)
        #完成添加
        #检查是否在管理的信息列表里
        driver.close()
        time.sleep(1)
        #删除没有的窗口句柄
        allhandlelist.pop()
        time.sleep(1)
        driver.switch_to_window(allhandlelist[0])
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_xpath(".//*[@id='dgBrowse']/tbody/tr[2]/td[6]/a").click()
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='Control_54d74d16_6f98_4943_9cc2_ad09bad8fe9c']").clear()
        driver.find_element_by_xpath(".//*[@id='Control_54d74d16_6f98_4943_9cc2_ad09bad8fe9c']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        time.sleep(1)
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[1]/a").text
            self.assertEqual(text, self.add_text)
            print u'添加的信息列表里存在，名称“'+self.add_text+'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加的信息列表里没有存在，名称“'+self.add_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'2.png')
            print u'错误截图：'+self.img_text+'2.png'
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
