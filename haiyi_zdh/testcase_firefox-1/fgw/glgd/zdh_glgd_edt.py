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

class zdh_glgd_edt(unittest.TestCase):
    def setUp(self):
        login.login_admin(self)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.img_text='img_glgd_edt_error'
    
    def test_zdh_glgd_edt(self):
        u"""修改管理规定"""
        driver = self.driver
        above=driver.find_element_by_xpath(".//*[@id='nav-c6abd596-d35c-468c-b3a4-f167d5be1ee1']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='nav-230f2b05-e78a-4ccb-acd7-e71265228739']/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/div/a[2]").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_xpath(".//*[@id='txbTitle']").send_keys(u'管理规定')
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtSearch']").click()
        time.sleep(1)
        #添加信息
        edt_text='ywgk_edt'+time.strftime("%Y%m%d%H%M%S", time.localtime())
        driver.find_element_by_xpath(".//*[@id='dgBrowse']/tbody/tr[2]/td[5]/a").click()
        time.sleep(1)
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").send_keys(edt_text)
        driver.find_element_by_xpath(".//*[@id='CustomrichTextBox']").send_keys(edt_text)
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
        #选择窗口2（即添加窗口）
        driver.switch_to_window(allhandles[1])
        #获取属性值（除标题和内容）
        llfw_add_text=driver.find_element_by_xpath(".//*[@id='Page_RightControlId_txbText']").get_attribute('value')
        fbdw_text=u'重庆金算盘软件有限公司'
        fbrq_text=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_txbDate']").get_attribute('value')
        hour=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_hour']")
        hour_selcteds=hour.find_elements_by_tag_name("option")
        for hour_selcted in hour_selcteds:
            if hour_selcted.get_attribute('selected'):
                fbsjh_add_text=hour_selcted.get_attribute('value')
        minute=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_minute']")
        minute_selcteds=minute.find_elements_by_tag_name("option")
        for minute_selcted in minute_selcteds:
            if minute_selcted.get_attribute('selected'):
                fbsjm_add_text=minute_selcted.get_attribute('value')
        second=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_second']")
        second_selcteds=second.find_elements_by_tag_name("option")
        for second_selcted in second_selcteds:
            if second_selcted.get_attribute('selected'):
                fbsjs_add_text=second_selcted.get_attribute('value')
        driver.find_element_by_xpath(".//*[@id='ibSaveAndContinue']").click()
        alert = driver.switch_to_alert()
        text=alert.text
        alert.accept()
        try:
            self.assertEqual(u'添加成功', text)
            print u'添加信息，名称“'+edt_text+'”，添加成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加信息，名称“'+edt_text+'”，添加失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'1.png')
            print u'【错误截图】：'+self.img_text+'1.png'
        driver.close()
        time.sleep(2)
        #完成添加
        #修改信息
        edt2_text='ywgk_2edt'+time.strftime("%Y%m%d%H%M%S", time.localtime())
        driver.switch_to_window(allhandles[0])
        driver.switch_to_frame("diaConIf")
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_xpath(".//*[@id='dgBrowse']/tbody/tr[2]/td[6]/a").click()
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        driver.find_element_by_xpath(".//*[@id='Control_f080c6e8_7f60_4232_a1c9_24f6feeb8c5e']").clear()
        driver.find_element_by_xpath(".//*[@id='Control_f080c6e8_7f60_4232_a1c9_24f6feeb8c5e']").send_keys(edt_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        time.sleep(1)
        try:
            driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[5]/a").click()
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'添加的信息列表里没有存在，名称“'+edt_text+'”退出测试'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'2.png')
            print u'【错误截图】：'+self.img_text+'2.png'
            return
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[2])
        try:
            text=driver.find_element_by_xpath(".//*[@id='Page_RightControlId_txbText']").get_attribute('value')
            self.assertEqual(llfw_add_text,text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'浏览范围名称为“'+text+'"与添加时的内容"'+edt_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'3.png')
            print u'【错误截图】：'+self.img_text+'3.png'
        try:
            text=driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").text
            self.assertEqual(edt_text,text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'标题名称为“'+text+'"与添加时的内容"'+edt_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'4.png')
            print u'【错误截图】：'+self.img_text+'4.png'
        try:
            text=driver.find_element_by_xpath(".//*[@id='CustomrichTextBox']").text
            self.assertEqual(edt_text,text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'内容为“'+text+'"与添加时的内容"'+edt_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'5.png')
            print u'【错误截图】：'+self.img_text+'5.png'
        try:
            text=driver.find_element_by_xpath(".//*[@id='Page_OrganNameControlId_txbText']").get_attribute('value')
            self.assertEqual(fbdw_text,text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'发布单位为“'+text+'"与添加时的内容"'+edt2_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'6.png')
            print u'【错误截图】：'+self.img_text+'6.png'
        try:
            hour=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_hour']")
            hour_selcteds=hour.find_elements_by_tag_name("option")
            for hour_selcted in hour_selcteds:
                if hour_selcted.get_attribute('selected'):
                    fbsjh_edt_text=hour_selcted.get_attribute('value')
            self.assertEqual(fbsjh_add_text,fbsjh_edt_text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'发布时点为“'+fbsjh_edt_text+'"与添加时的内容"'+fbsjh_add_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'7.png')
            print u'【错误截图】：'+self.img_text+'7.png'
        try:
            minute=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_minute']")
            minute_selcteds=minute.find_elements_by_tag_name("option")
            for minute_selcted in minute_selcteds:
                if minute_selcted.get_attribute('selected'):
                    fbsjm_edt_text=minute_selcted.get_attribute('value')
            self.assertEqual(fbsjm_add_text,fbsjm_edt_text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'发布时分为“'+fbsjm_edt_text+'"与添加时的内容"'+fbsjm_add_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'8.png')
            print u'【错误截图】：'+self.img_text+'8.png'
        try:
            second=driver.find_element_by_xpath(".//*[@id='control_AuditedDateTime_second']")
            second_selcteds=second.find_elements_by_tag_name("option")
            for second_selcted in second_selcteds:
                if second_selcted.get_attribute('selected'):
                    fbsjs_edt_text=second_selcted.get_attribute('value')
            self.assertEqual(fbsjs_add_text,fbsjs_edt_text )
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'发布时秒为“'+fbsjs_edt_text+'"与添加时的内容"'+fbsjs_add_text+'"不一致'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'9.png')
            print u'【错误截图】：'+self.img_text+'9.png'
        driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").clear()
        driver.find_element_by_xpath(".//*[@id='Page_TitleControlId']").send_keys(edt2_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        alert = driver.switch_to_alert()
        text=alert.text
        alert.accept()
        try:
            self.assertEqual(u'操作成功', text)
            print u'名称“'+edt_text+'”，修改成功' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'名称“'+edt_text+'”，修改失败'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'10.png')
            print u'【错误截图】：'+self.img_text+'10.png'
        driver.switch_to_window(allhandles[1])
        driver.find_element_by_xpath(".//*[@id='Control_f080c6e8_7f60_4232_a1c9_24f6feeb8c5e']").clear()
        driver.find_element_by_xpath(".//*[@id='Control_f080c6e8_7f60_4232_a1c9_24f6feeb8c5e']").send_keys(edt2_text)
        driver.find_element_by_xpath(".//*[@id='ibtSubmit']").click()
        time.sleep(1)
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgListRecord']/tbody/tr[2]/td[1]/a").text
            self.assertEqual(text, edt2_text)
            print u'信息列表里存在，修改后名称“'+edt2_text+'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'信息列表里没有存在，修改后名称“'+edt2_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'11.png')
            print u'【错误截图】：'+self.img_text+'11.png'
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
