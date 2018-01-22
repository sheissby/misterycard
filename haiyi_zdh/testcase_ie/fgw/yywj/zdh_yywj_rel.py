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

class zdh_yywj_rel(unittest.TestCase):
    def setUp(self):
        login.login_admin(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.rel_text='yywj_rel'+now
        self.img_text='img_yywj_rel_error'
    
    def test_zdh_yywj_rel(self):
        u"""发布医院文件"""
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
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_xpath(".//*[@id='txbTitle']").send_keys(u'医院文件')
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtSearch']").click()
        time.sleep(1)
        #添加修改信息
        driver.find_element_by_xpath(".//*[@id='dgBrowse']/tbody/tr[2]/td[5]/a").click()
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        #将获取当前所有窗口与allhandlelist的差集加到allhandlelist后面（连接到allhandlelist）
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").send_keys(self.rel_text)
        # getElementById("iframe的ID")
        set_wyswyg_js = 'document.getElementById("CustomrichTextBox_editor").contentWindow.document.body.innerHTML="'+self.rel_text+'"'
        driver.execute_script(set_wyswyg_js)
        #js="$(\"input[id='control_AuditedDateTime_txbDate']\").removeAttr('readonly');$(\"input[id='control_AuditedDateTime_txbDate']\").attr('value','2016-07-31')"
        #driver.execute_script(js)
        time.sleep(1)
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
        driver.find_element_by_xpath(".//*[@id='ibSaveAndContinue']").click()
        alert = driver.switch_to_alert()
        text=alert.text
        alert.accept()
        try:
            self.assertEqual(u'添加成功', text)
            print u'添加信息，名称“'+self.rel_text+'”，添加成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加信息，名称“'+self.rel_text+'”，添加失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'1.png')
            print u'错误截图：'+self.img_text+'1.png'
        driver.close()
        time.sleep(2)
        #完成添加
        #删除没有的窗口句柄
        allhandlelist.pop()
        time.sleep(1)
        driver.switch_to_window(allhandlelist[0])
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_xpath(".//*[@id='dgBrowse']/tbody/tr[2]/td[6]/a").click()
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        driver.find_element_by_xpath(".//*[@id='Control_60a7e30c_ef53_4999_a8fa_6b056075d481']").clear()
        driver.find_element_by_xpath(".//*[@id='Control_60a7e30c_ef53_4999_a8fa_6b056075d481']").send_keys(self.rel_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        time.sleep(1)
        try:
            text1=driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[1]/a").text
            text2=driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[8]/a").text
            if text1!=self.rel_text or text2!=u'发布':
                raise NameError('date error !')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加的信息列表里没有存在，名称“'+self.rel_text+'”,或者数据不再可发布状态，退出测试'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'2.png')
            print u'错误截图：'+self.img_text+'2.png'
            return
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[8]/a").send_keys('')
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        driver.switch_to_window(allhandlelist[2])
        time.sleep(2)
        driver.close()
        time.sleep(2)
        #删除没有的窗口句柄
        allhandlelist.pop()
        time.sleep(1)
        driver.switch_to_window(allhandlelist[1])
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[5]").text
            self.assertEqual(u'已审批', text)
            print u'发布成功，名称'+self.rel_text+ '已审批'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'发布失败，名称'+self.rel_text
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'3.png')
            print u'错误截图：'+self.img_text+'3.png'
        time.sleep(2)
        driver.quit()
        #普通用户登录查看检查
        login.login_normal(self)
        driver=self.driver
        driver.find_element_by_xpath(".//*[@id='nav-e7c0b5a6-028c-423d-a564-b35e4613947c']/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[5]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[5]/div/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='Control_f1377e3a_dfe3_4a0d_a7b9_fe587de4c8d0']").clear()
        driver.find_element_by_xpath(".//*[@id='Control_f1377e3a_dfe3_4a0d_a7b9_fe587de4c8d0']").send_keys(self.rel_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        time.sleep(2)
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[2]/a").text
            self.assertEqual(self.rel_text, text)
            print u'发布成功，用普通用户登录查看，存在名称'+self.rel_text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'发布失败，用普通用户登录查看，没有存在名称'+self.rel_text
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'4.png')
            print u'错误截图：'+self.img_text+'4.png'
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
