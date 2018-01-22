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

class zdh_ywgk_add(unittest.TestCase):
    def setUp(self):
        login.login_admin(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.add_text='ywgk_add'+now
        self.img_text='img_ywgk_add_error'
    
    def test_zdh_ywgk_add(self):
        u"""添加院务公开"""
        driver = self.driver
        allhandlelist=[]
        nowhandle=driver.current_window_handle
        allhandlelist.append(nowhandle)
        #定位到鼠标移动到上面的元素
        above=driver.find_element_by_xpath(".//*[@id='nav-c6abd596-d35c-468c-b3a4-f167d5be1ee1']/a")
        #对定位到的元素执行鼠标移动到上面的操作
        ActionChains(driver).move_to_element(above).perform()
        #点击内容管理（全）
        driver.find_element_by_xpath(".//*[@id='nav-230f2b05-e78a-4ccb-acd7-e71265228739']/a").click()
        time.sleep(2)
        #点击左边内容管理（全）下面的“信息管理”
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/div/a[2]").click()
        time.sleep(2)
        #进入到frame（diaConIf）
        driver.switch_to_frame("diaConIf")
        #进入到frame（rightFrame）
        driver.switch_to_frame("rightFrame")
        #列表名称输入'院务公开'
        driver.find_element_by_xpath(".//*[@id='txbTitle']").send_keys(u'院务公开')
        time.sleep(1)
        #点击“查询”按钮
        driver.find_element_by_xpath(".//*[@id='ibtSearch']").click()
        time.sleep(1)
        #开始添加信息-----------------------------------
        driver.find_element_by_xpath(".//*[@id='dgBrowse']/tbody/tr[2]/td[5]/a").click()
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        #将获取当前所有窗口与allhandlelist的差集加到allhandlelist后面（连接到allhandlelist）
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        #选择窗口2（即添加窗口）
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        #输入标题信息
        driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").send_keys(self.add_text)
        #输入内容
        set_wyswyg_js = 'document.getElementById("CustomrichTextBox_editor").contentWindow.document.body.innerHTML="'+self.add_text+'"'
        driver.execute_script(set_wyswyg_js)
        #js="$(\"input[id='control_AuditedDateTime_txbDate']\").removeAttr('readonly');$(\"input[id='control_AuditedDateTime_txbDate']\").attr('value','2016-07-31')"
        #driver.execute_script(js)
        time.sleep(1)
        #点击浏览范围的“选择”按钮
        driver.find_element_by_xpath(".//*[@id='Page_RightControlId_imgBt']").click()
        time.sleep(1)
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
        #给附件赋个空值
        driver.find_element_by_xpath(".//*[@id='Control_b1539a1b_2161_4997_8238_1fe0723e2e17_IbtnAppend']").send_keys('')
        #下面两句为模拟键盘的回车 按下和松开
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        driver.switch_to_window(allhandlelist[2])
        time.sleep(1)
        #进入PostFrame框架
        driver.switch_to_frame("PostFrame")
        #点击浏览按钮
        #定位到要双击的元素
        double =driver.find_element_by_xpath(".//*[@id='InputFile']")
        #对定位到的元素执行鼠标双击操作
        ActionChains(driver).double_click(double).perform()
        time.sleep(1)
        #执行Windows文件D:\selenium+python\windowsexe\docx.exe
        os.startfile(os.getcwd().split('testcase_ie')[0]+'\uploadfile\Ie_fgw_doc.exe')
        #等待5s，因为选择附件需要一些时间
        time.sleep(2)
        #点击附加按钮
        driver.find_element_by_xpath(".//*[@id='IbtnPost']").click()
        time.sleep(5)
        #点击提交按钮
        driver.find_element_by_xpath(".//*[@id='IbtnClose']").click()
        time.sleep(1)
        #删除没有的窗口句柄
        allhandlelist.pop()
        #选择管理信息窗口
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        #点击“保存并继续添加”按钮
        driver.find_element_by_xpath(".//*[@id='ibSaveAndContinue']").click()
        #获取点击“保存并继续添加”按钮后的告警信息（添加成功/添加失败）
        alert = driver.switch_to_alert()
        text=alert.text
        #接受告警信息
        alert.accept()
        #检查告警信息是否为“添加成功”，如果不是会抛出异常，异常信息会加到self.verificationErrors数组里
        try:
            self.assertEqual(u'添加成功', text)
            print u'添加信息，名称“'+self.add_text+'”，添加成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加信息，名称“'+self.add_text+'”，添加失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'1.png')
            print u'错误截图：'+self.img_text+'1.png'
        time.sleep(2)
        #完成添加信息---------------------------------------
        #检查添加的信息是否在管理的信息列表里--------------
        #关闭添加窗口
        driver.close()
        time.sleep(1)
        #删除没有的窗口句柄
        allhandlelist.pop()
        time.sleep(1)
        #选择窗口1（即打开浏览器时原始窗口）
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
        driver.find_element_by_xpath(".//*[@id='Control_326f92d9_e1a5_43aa_80d6_1281d32ab368']").clear()
        driver.find_element_by_xpath(".//*[@id='Control_326f92d9_e1a5_43aa_80d6_1281d32ab368']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        time.sleep(1)
        #检查信息列表是否有标题为self.add_text的信息，如果不是会抛出异常，异常信息会加到self.verificationErrors数组里
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
