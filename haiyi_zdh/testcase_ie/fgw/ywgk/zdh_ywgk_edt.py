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

class zdh_ywgk_edt(unittest.TestCase):
    def setUp(self):
        login.login_admin(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.img_text='img_ywgk_edt_error'
        
    def test_zdh_ywgk_edt(self):
        u"""修改院务公开"""
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
        driver.find_element_by_xpath(".//*[@id='txbTitle']").send_keys(u'院务公开')
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtSearch']").click()
        time.sleep(1)
        #添加信息***************************
        edt_text='ywgk_edt'+time.strftime("%Y%m%d%H%M%S", time.localtime())
        driver.find_element_by_xpath(".//*[@id='dgBrowse']/tbody/tr[2]/td[5]/a").click()
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        #将获取当前所有窗口与allhandlelist的差集加到allhandlelist后面（连接到allhandlelist）
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").send_keys(edt_text)
        set_wyswyg_js = 'document.getElementById("CustomrichTextBox_editor").contentWindow.document.body.innerHTML="'+edt_text+'"'
        driver.execute_script(set_wyswyg_js)
        #js="$(\"input[id='control_AuditedDateTime_txbDate']\").removeAttr('readonly');$(\"input[id='control_AuditedDateTime_txbDate']\").attr('value','2016-07-31')"
        #driver.execute_script(js)
        time.sleep(1)
        #点击浏览范围的“选择”按钮
        driver.find_element_by_xpath(".//*[@id='Page_RightControlId_imgBt']").click()
        #time.sleep(1)
        #获取点击选择按钮时的警告信息（请选择浏览范围）
        #alert = driver.switch_to_alert()
        #接收警告信息
        #alert.accept()
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
        #获取属性值（除标题和内容）-------------------------------
        fbdw_text=u'重庆金算盘软件有限公司'
        fbrq_text=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_txbDate']").get_attribute('value')
        #获取时分秒
        fbsjh_add_text=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_hour']").get_attribute('value')
        fbsjm_add_text=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_minute']").get_attribute('value')
        fbsjs_add_text=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_second']").get_attribute('value')
        #浏览范围
        llfw_text=u'重庆金算盘软件有限公司'
        #完成获取属性值（除标题和内容）-----------------------------
        driver.find_element_by_xpath(".//*[@id='ibSaveAndContinue']").click()
        alert = driver.switch_to_alert()
        text=alert.text
        alert.accept()
        try:
            self.assertEqual(u'添加成功', text)
            print u'添加用于修改信息，名称“'+edt_text+'”，添加成功' 
        except :
            print u'添加用于修改信息，名称“'+edt_text+'”，添加失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'1.png')
            print u'错误截图：'+self.img_text+'1.png'
            return
        #关闭添加信息窗口
        driver.close()
        time.sleep(2)
        #完成添加**************************
        #修改信息-----------------------
        #edt2_text为要修改后的名称
        edt2_text='ywgk_2edt'+time.strftime("%Y%m%d%H%M%S", time.localtime())
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
        driver.find_element_by_xpath(".//*[@id='Control_326f92d9_e1a5_43aa_80d6_1281d32ab368']").clear()
        driver.find_element_by_xpath(".//*[@id='Control_326f92d9_e1a5_43aa_80d6_1281d32ab368']").send_keys(edt_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        time.sleep(1)
        try:
            #点击修改
            driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[5]/a").click()
        except:
            print u'添加的信息列表里没有存在，名称“'+edt_text+'”'
            self.verificationErrors.append('no data')
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'2.png')
            print u'错误截图：'+self.img_text+'2.png'
            return
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        driver.switch_to_window(allhandlelist[2])
        time.sleep(1)
        #对比属性一致性--------------------------
        try:
            text=driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").text
            self.assertEqual(edt_text,text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'标题名称为“'+text+'"与添加时的内容"'+edt_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'3.png')
            print u'错误截图：'+self.img_text+'3.png'
        try:
            text=driver.find_element_by_xpath(".//*[@id='CustomrichTextBox']").get_attribute('value')
            self.assertEqual(edt_text,text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'内容为“'+text+'"与添加时的内容"'+edt_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'4.png')
            print u'错误截图：'+self.img_text+'4.png'
        try:
            text=driver.find_element_by_xpath(".//*[@id='Page_OrganNameControlId_txbText']").get_attribute('value')
            self.assertEqual(fbdw_text,text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'发布单位为“'+text+'"与添加时的内容"'+edt2_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'5.png')
            print u'错误截图：'+self.img_text+'5.png'
        try:
            fbsjh_edt_text=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_hour']").get_attribute('value')
            self.assertEqual(fbsjh_add_text,fbsjh_edt_text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'发布时点为“'+fbsjh_edt_text+'"与添加时的内容"'+fbsjh_add_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'6.png')
            print u'错误截图：'+self.img_text+'6.png'
        try:
            fbsjm_edt_text=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_minute']").get_attribute('value')
            self.assertEqual(fbsjm_add_text,fbsjm_edt_text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'发布时分为“'+fbsjm_edt_text+'"与添加时的内容"'+fbsjm_add_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'7.png')
            print u'错误截图：'+self.img_text+'7.png'
        try:
            fbsjs_edt_text=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_second']").get_attribute('value')
            self.assertEqual(fbsjs_add_text,fbsjs_edt_text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'发布时秒为“'+fbsjs_edt_text+'"与添加时的内容"'+fbsjs_add_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'8.png')
            print u'错误截图：'+self.img_text+'8.png'
        try:
            text=driver.find_element_by_xpath(".//*[@id='Page_RightControlId_txbText']").get_attribute('value')
            self.assertEqual(llfw_text,text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'浏览范围名称为“'+text+'"与添加时的内容"'+llfw_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'9.png')
            print u'错误截图：'+self.img_text+'9.png'
        #完成对比属性一致性--------------------------
        #清空标题名称
        driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").clear()
        #将标题修成edt2_text
        driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").send_keys(edt2_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        #获取修改后的告警信息
        alert = driver.switch_to_alert()
        #获取告警信息的提示语
        text=alert.text
        #接受告警
        alert.accept()
        #判断提示语是否为操作成功
        try:
            self.assertEqual(u'操作成功', text)
            print u'名称“'+edt_text+'”，修改成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'名称“'+edt_text+'”，修改失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'10.png')
            print u'错误截图：'+self.img_text+'10.png'
        #删除没有的窗口句柄
        allhandlelist.pop()
        time.sleep(1)
        #选择管理信息窗口
        driver.switch_to_window(allhandlelist[1])
        #以下三行为在管理信息窗口查询edt2_text
        driver.find_element_by_xpath(".//*[@id='Control_326f92d9_e1a5_43aa_80d6_1281d32ab368']").clear()
        driver.find_element_by_xpath(".//*[@id='Control_326f92d9_e1a5_43aa_80d6_1281d32ab368']").send_keys(edt2_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        time.sleep(1)
        #获取查询后的第一条记录的标题名称，判断是否修改成功
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[1]/a").text
            self.assertEqual(text, edt2_text)
            print u'信息列表里存在，修改后名称“'+edt2_text+'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'信息列表里没有存在，修改后名称“'+edt2_text+'”'
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
