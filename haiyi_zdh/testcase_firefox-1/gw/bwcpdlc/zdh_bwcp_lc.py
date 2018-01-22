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
import closewindow
import win32api
import win32con
from PIL import ImageGrab

class zdh_bwcp_lc(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.add_text='bwcp_lc'+now
        self.hq='bwcp_lc_hq'+now
        self.tj_text=u'冯学冠'
        self.qp_text=u'符晓玲'
        self.hq1_text=u'黄植'
        self.hq2_text=u'谭壮华'
        self.hqqp_text=u'吴忠旺'
        self.zz_text=u'丁娥'
        self.js_text=u'马婧'
        self.ffz_text=u'医疗技术_心脑电图室'
        self.ffr_text=u'黄娜'
        self.img_text='img_bwcp_lc_error'
    
    def test_zdh_bwcp_lc(self):
        u"""办文呈批单流程"""
        print self.tj_text+u'开始提交办文呈批单流程，名称为：'+self.add_text
        login.login_normal(self)
        driver = self.driver
        #进入公文呈报
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='nav-c0baf144-2241-471a-8947-db8511046075']/a").click()
        time.sleep(2)
        nowhandle=driver.current_window_handle
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath("html/body/div[2]/div/table[1]/tbody/tr/td[2]/div/ul/li/table/tbody/tr/td[1]/a").click()
        driver.switch_to.default_content()
        time.sleep(1)
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)
        #添加流程信息--------------------
        driver.find_element_by_xpath(".//*[@id='080108']").click()
        driver.find_element_by_xpath(".//*[@id='fab70432-fe83-4754-a419-76d752f8e0fd']").click()
        time.sleep(2)
        frame=driver.find_element_by_xpath('/html/body/div[2]')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        driver.find_element_by_xpath(".//*[@id='dpTodayInput']").click()
        driver.switch_to.default_content()
        driver.switch_to_frame("_DialogFrame_0")
        driver.find_element_by_xpath(".//*[@id='2da0c1a9-76d0-402d-a4f4-566472a6daf4']").click()
        time.sleep(2)
        frame=driver.find_element_by_xpath('/html/body/div[2]')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        driver.find_element_by_xpath(".//*[@id='dpTodayInput']").click()
        time.sleep(1)
        driver.switch_to.default_content()
        driver.switch_to_frame("_DialogFrame_0")
        driver.find_element_by_xpath(".//*[@id='2fff7b71-4436-4646-815b-a61f31b61574']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='2ab2465a-d822-4b56-bd42-a4900a20f4e8']").send_keys('10')
        #点开发放范围选择
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[6]/td[1]/img").click()
        time.sleep(1)
        allhandles=driver.window_handles
        time.sleep(1)
        #切换到发放范围窗口
        driver.switch_to_window(allhandles[1])
        driver.switch_to_frame("mainFrame")
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(1)
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(1)
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("_DialogFrame_0")
        #点开收件人选择
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[8]/td[1]/img").click()
        time.sleep(1)
        allhandles=driver.window_handles
        time.sleep(1)
        #切换到收件人窗口
        driver.switch_to_window(allhandles[1])
        driver.switch_to_frame("mainFrame")
        driver.find_element_by_xpath(".//*[@id='tb_Search']").send_keys(self.qp_text)
        driver.find_element_by_xpath(".//*[@id='btn_Search']").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(1)
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(2)
        #上传附件
        driver.switch_to_window(allhandles[0])
        driver.switch_to_frame("_DialogFrame_0")
        driver.find_element_by_xpath(".//*[@id='tbFilePost_FileUpload']").click()
        frame=driver.find_element_by_css_selector('.fancybox-inner')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        driver.find_element_by_id("tbFilePost_uploadify").click()
        time.sleep(3)
        os.startfile(os.getcwd().split('testcase_firefox')[0]+'\uploadfile\Fox_gw_doc.exe')
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='tbFilePost_OK']").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.switch_to_frame("_DialogFrame_0")
        driver.find_element_by_xpath(".//*[@id='77891a1e-5e2e-4fdd-a8d0-9c99eed17437']").send_keys(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        driver.find_element_by_xpath(".//*[@id='bt_Submit']").click()
        time.sleep(7)
        print self.tj_text+u'完成提交办文呈批单流程，名称为：'+self.add_text
        driver.quit()
        #完成添加流程信息-------------------
        #进行会签(符晓玲)----------------------------
        #换账号登录
        print self.qp_text+u'开始会签，会签名称为：'+self.hq+u'分别会签给'+self.hq1_text+u'和'+self.hq2_text
        time.sleep(1)
        login.login_normal2(self)
        closewindow.close_window('Plugin Container for Firefox')
        driver = self.driver
        #进入公文呈报
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-70f461d6-02d9-4a0e-9c75-1b38aa29da02']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='ctrTitle']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='IB_search']").click()
        time.sleep(1)
        #获取标题、签批状态、发送人。如果获取异常侧作为不在存数据处理
        try:
            bt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").text
            qpzt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            fsr_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'没有存在流程名称“'+self.add_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'1.png')
            print u'【错误截图】：'+self.img_text+'1.png'
            return
        #判断标题、签批状态、发送人是否正确
        try:
            if bt_text!=self.add_text or qpzt_text!=u'签批' or fsr_text!=self.tj_text:
                print u'名称"'+self.add_text+u'",标题、签批状态、发送人存在有误'
                raise NameError('data erro')
            else :print u'名称"'+self.add_text+u'",标题、签批状态、发送人正确'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.add_text+u'”，标题或签批状态或发送人不正确'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'2.png')
            print u'【错误截图】：'+self.img_text+'2.png'
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='IB_sendsplit']").click()
        time.sleep(1)
        driver.switch_to.default_content()
        driver.switch_to_frame("_DialogFrame_diagSendSplitBox")
        #点开收件人(发送会签)选择
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='SelectUser_imgBt']").click()
        time.sleep(1)
        allhandles=driver.window_handles
        time.sleep(1)
        #切换到收件人窗口
        driver.switch_to_window(allhandles[1])
        driver.switch_to_frame("mainFrame")
        driver.find_element_by_xpath(".//*[@id='tb_Search']").send_keys(self.hq1_text)
        driver.find_element_by_xpath(".//*[@id='btn_Search']").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='tb_Search']").clear()
        driver.find_element_by_xpath(".//*[@id='tb_Search']").send_keys(self.hq2_text)
        driver.find_element_by_xpath(".//*[@id='btn_Search']").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(1)
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(1)
        #输入会签标题
        driver.switch_to_window(allhandles[0])
        driver.switch_to_frame("_DialogFrame_diagSendSplitBox")
        driver.find_element_by_xpath(".//*[@id='tbTitle']").send_keys(self.hq)
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='IB_add']").click()
        time.sleep(2)
        driver.find_element_by_xpath('html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='IB_add']").click()
        time.sleep(2)
        driver.find_element_by_css_selector('.aui_state_highlight').click()
        time.sleep(2)
        driver.quit()
        print self.qp_text+u'完成会签，会签名称为：'+self.hq+u'分别会签给'+self.hq1_text+u'和'+self.hq2_text
        #完成会签(符晓玲)---------------------
        #开始第一个（黄植）会签签批---------------------
        print self.hq1_text+u',开始会签签批，并转交给'+self.hqqp_text+u'签批'
        time.sleep(1)
        login.login_normal3(self)
        driver = self.driver
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-70f461d6-02d9-4a0e-9c75-1b38aa29da02']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='ctrTitle']").send_keys(self.hq)
        driver.find_element_by_xpath(".//*[@id='IB_search']").click()
        time.sleep(1)
        try:
            bt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").text
            qpzt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            fsr_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'没有存在流程名称“'+self.add_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'3.png')
            print u'【错误截图】：'+self.img_text+'3.png'
            return
        #判断标题、签批状态、发送人是否正确
        try:
            if bt_text!=self.hq or qpzt_text!=u'会签签批' or fsr_text!=self.qp_text:
                print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",有误'
                raise NameError('data erro')
            else :print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",正确'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.hq+u'”，标题或签批状态或发送人不正确'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'4.png')
            print u'【错误截图】：'+self.img_text+'4.png'
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()
        time.sleep(2)
        #点开收件人选择
        driver.switch_to.default_content()
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='SelectUser_imgBt']").click()
        time.sleep(1)
        allhandles=driver.window_handles
        time.sleep(1)
        #切换到收件人窗口
        driver.switch_to_window(allhandles[1])
        driver.switch_to_frame("mainFrame")
        driver.find_element_by_xpath(".//*[@id='tb_Search']").send_keys(self.hqqp_text)
        driver.find_element_by_xpath(".//*[@id='btn_Search']").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(1)
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(2)
        #上传附件
        driver.switch_to_window(allhandles[0])
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='tbFilePost_FileUpload']").click()
        time.sleep(1)
        frame=driver.find_element_by_css_selector('.fancybox-inner')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        driver.find_element_by_id("tbFilePost_uploadify").click()
        time.sleep(3)
        os.startfile(os.getcwd().split('testcase_firefox')[0]+'\uploadfile\Fox_gw_doc.exe')
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='tbFilePost_OK']").click()
        time.sleep(1)
        driver.switch_to_window(allhandles[0])
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='tbConten']").send_keys(self.hq1_text+u'同意')
        driver.find_element_by_xpath(".//*[@id='IBSure']").click()
        time.sleep(5)
        driver.quit()
        print self.hq1_text+u',完成会签签批，并转交给'+self.hqqp_text+u'签批'
        #完成第一个（黄植）会签签批,并转交给吴忠旺------------------
        #开始会签签批（吴忠旺）------------------
        print self.hqqp_text+u'开始结束会签'
        time.sleep(1)
        login.login_normal4(self)
        closewindow.close_window('Plugin Container for Firefox')
        driver = self.driver
        nowhandle=driver.current_window_handle
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-70f461d6-02d9-4a0e-9c75-1b38aa29da02']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='ctrTitle']").send_keys(self.hq)
        driver.find_element_by_xpath(".//*[@id='IB_search']").click()
        time.sleep(1)
        try:
            bt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").text
            qpzt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            fsr_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'没有存在流程名称“'+self.hq+'”'
            return
        #判断标题、签批状态、发送人是否正确
        try:
            if bt_text!=self.hq or qpzt_text!=u'签批' or fsr_text!=self.hq1_text:
                print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",有误'
                raise NameError('data erro')
            else :print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",正确'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.hq+u'”，标题或签批状态或发送人不正确'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'5.png')
            print u'【错误截图】：'+self.img_text+'5.png'
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()
        #上传附件
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='tbFilePost_FileUpload']").click()
        frame=driver.find_element_by_css_selector('.fancybox-inner')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        driver.find_element_by_id("tbFilePost_uploadify").click()
        time.sleep(3)
        os.startfile(os.getcwd().split('testcase_firefox')[0]+'\uploadfile\Fox_gw_doc.exe')
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='tbFilePost_OK']").click()
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='tbConten']").send_keys(self.hqqp_text+u'同意')
        driver.find_element_by_xpath(".//*[@id='IB_SendAndOver']").click()
        time.sleep(5)
        driver.quit()
        print self.hqqp_text+u'完成结束会签'
        #完成会签签批（吴忠旺）------------------
        #开始第二个（谭壮华）会签签批---------------------
        print self.hq2_text+u'开始结束会签'
        time.sleep(1)
        closewindow.close_window('Plugin Container for Firefox')
        login.login_normal5(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-70f461d6-02d9-4a0e-9c75-1b38aa29da02']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='ctrTitle']").send_keys(self.hq)
        driver.find_element_by_xpath(".//*[@id='IB_search']").click()
        time.sleep(1)
        try:
            bt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").text
            qpzt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            fsr_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'没有存在流程名称“'+self.hq+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'6.png')
            print u'【错误截图】：'+self.img_text+'6.png'
            return
        #判断标题、签批状态、发送人是否正确
        try:
            if bt_text!=self.hq or qpzt_text!=u'会签签批' or fsr_text!=self.qp_text:
                print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",有误'
                raise NameError('data erro')
            else :print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",正确'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.hq+u'”，标题或签批状态或发送人不正确'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'7.png')
            print u'【错误截图】：'+self.img_text+'7.png'
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()
##        #上传附件
##        driver.switch_to_window(nowhandle)
##        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
##        driver.find_element_by_xpath(".//*[@id='tbFilePost_FileUpload']").click()
##        time.sleep(1)
##        frame=driver.find_element_by_css_selector('.fancybox-inner')
##        frames=frame.find_elements_by_tag_name('iframe')
##        driver.switch_to_frame(frames[0])
##        driver.find_element_by_id("tbFilePost_uploadify").click()
##        time.sleep(3)
##        os.startfile(os.getcwd().split('testcase_firefox')[0]+'\uploadfile\Fox_gw_doc.exe')
##        time.sleep(5)
##        driver.find_element_by_xpath(".//*[@id='tbFilePost_OK']").click()
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='tbConten']").send_keys(self.hq2_text+u'同意')
        driver.find_element_by_xpath(".//*[@id='IB_SendAndOver']").click()
        time.sleep(6)
        driver.quit()
        print self.hq2_text+u'完成结束会签'
        #提交意见（符晓玲）接收人：丁娥---------------------
        #开始提交意见（符晓玲）接收人：丁娥---------------------
        print self.qp_text+u'开始提交意见,接收人为：'+self.zz_text
        time.sleep(1)
        login.login_normal2(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-70f461d6-02d9-4a0e-9c75-1b38aa29da02']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='ctrTitle']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='IB_search']").click()
        time.sleep(1)
        try:
            bt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").text
            qpzt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            fsr_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'没有存在流程名称“'+self.add_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'8.png')
            print u'【错误截图】：'+self.img_text+'8.png'
            return
        #判断标题、签批状态、发送人是否正确
        try:
            if bt_text!=self.add_text or qpzt_text!=u'签批' or fsr_text!=self.tj_text:
                print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",有误'
                raise NameError('data erro')
            else :print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",正确'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.add_text+u'”，标题或签批状态或发送人不正确'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'9.png')
            print u'【错误截图】：'+self.img_text+'9.png'
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()
        #点开收件人选择
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='SelectUser_imgBt']").click()
        time.sleep(1)
        allhandles=driver.window_handles
        time.sleep(1)
        #切换到收件人窗口
        driver.switch_to_window(allhandles[1])
        driver.switch_to_frame("mainFrame")
        driver.find_element_by_xpath(".//*[@id='tb_Search']").send_keys(self.zz_text)
        driver.find_element_by_xpath(".//*[@id='btn_Search']").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(1)
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(2)
##        #上传附件
##        driver.switch_to_window(nowhandle)
##        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
##        driver.find_element_by_xpath(".//*[@id='tbFilePost_FileUpload']").click()
##        time.sleep(1)
##        frame=driver.find_element_by_css_selector('.fancybox-inner')
##        frames=frame.find_elements_by_tag_name('iframe')
##        driver.switch_to_frame(frames[0])
##        driver.find_element_by_id("tbFilePost_uploadify").click()
##        time.sleep(3)
##        os.startfile(os.getcwd().split('testcase_firefox')[0]+'\uploadfile\Fox_gw_doc.exe')
##        time.sleep(5)
##        driver.find_element_by_xpath(".//*[@id='tbFilePost_OK']").click()
        time.sleep(1)
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='tbConten']").send_keys(self.qp_text+u'同意')
        driver.find_element_by_xpath(".//*[@id='btnIBSure']").click()
        time.sleep(5)
        driver.quit()
        print self.qp_text+u'完成提交意见,接收人为：'+self.zz_text
        #完成提交意见（符晓玲）接收人：丁娥---------------------
        #中转（丁娥）接收人：马婧---------------------
        print self.zz_text+u'开始中转给'+self.js_text
        time.sleep(1)
        login.login_normal6(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-70f461d6-02d9-4a0e-9c75-1b38aa29da02']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='ctrTitle']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='IB_search']").click()
        time.sleep(1)
        try:
            bt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").text
            qpzt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            fsr_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'没有存在流程名称“'+self.add_text+'”'
            return
        #判断标题、签批状态、发送人是否正确
        try:
            if bt_text!=self.add_text or qpzt_text!=u'签批' or fsr_text!=self.qp_text:
                print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",有误'
                raise NameError('data erro')
            else :print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",正确'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.add_text+u'”，标题或签批状态或发送人不正确'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'10.png')
            print u'【错误截图】：'+self.img_text+'10.png'
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()
        time.sleep(2)
        #点开收件人选择
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='SelectUser_imgBt']").click()
        time.sleep(1)
        allhandles=driver.window_handles
        time.sleep(1)
        #切换到收件人窗口
        driver.switch_to_window(allhandles[1])
        driver.switch_to_frame("mainFrame")
        driver.find_element_by_xpath(".//*[@id='tb_Search']").send_keys(self.js_text)
        driver.find_element_by_xpath(".//*[@id='btn_Search']").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(1)
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(2)
##        #上传附件
##        driver.switch_to_window(nowhandle)
##        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
##        driver.find_element_by_xpath(".//*[@id='tbFilePost_FileUpload']").click()
##        time.sleep(1)
##        frame=driver.find_element_by_css_selector('.fancybox-inner')
##        frames=frame.find_elements_by_tag_name('iframe')
##        driver.switch_to_frame(frames[0])
##        driver.find_element_by_id("tbFilePost_uploadify").click()
##        time.sleep(3)
##        os.startfile(os.getcwd().split('testcase_firefox')[0]+'\uploadfile\Fox_gw_doc.exe')
##        time.sleep(5)
##        driver.find_element_by_xpath(".//*[@id='tbFilePost_OK']").click()
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='IBHasOption']").click()
        driver.find_element_by_xpath(".//*[@id='tbConten']").send_keys(self.zz_text+u'同意')
        driver.find_element_by_xpath(".//*[@id='IB_Jump']").click()
        time.sleep(5)
        driver.quit()
        print self.zz_text+u'完成中转给'+self.js_text
        #完成中转（丁娥）接收人：马婧---------------------
        #提交人（冯学冠）在公文跟踪里，查看流程状态是否正确---------------------
        print self.tj_text+u'开始在公文跟踪查询流程'
        time.sleep(1)
        login.login_normal(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-5446eccb-1dc6-4819-aadc-fb4a5e74c26b']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbTitle']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='IB_search']").click()
        time.sleep(1)
        try:
            bt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").text
            gwlx_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[6]").text
            dqjd_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[7]").text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'没有存在流程名称“'+self.add_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'11.png')
            print u'【错误截图】：'+self.img_text+'11.png'
            return
        #判断标题、签批状态、发送人是否正确
        try:
            if bt_text!=self.add_text or gwlx_text!=u'办文呈批单' or dqjd_text!=self.js_text:
                print u'标题、公文类型、当前节点"'+bt_text+u'、'+gwlx_text+u'、'+dqjd_text+u'",有误'
                raise NameError('data erro')
            else :print u'标题、公文类型、当前节点"'+bt_text+u'、'+gwlx_text+u'、'+dqjd_text+u'",正确'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.add_text+u'”，标题、公文类型、当前节点有误'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'12.png')
            print u'【错误截图】：'+self.img_text+'12.png'
        driver.quit()
        print self.tj_text+u'完成在公文跟踪查询流程'
        #完成提交人（冯学冠）在公文跟踪里，查看流程状态是否正确---------------------
        #马婧结束流程---------------------
        print self.js_text+u'开始结束流程'
        time.sleep(1)
        login.login_normal7(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-70f461d6-02d9-4a0e-9c75-1b38aa29da02']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='ctrTitle']").send_keys(self.add_text)
        driver.find_element_by_xpath(".//*[@id='IB_search']").click()
        time.sleep(1)
        try:
            bt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").text
            qpzt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            fsr_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'没有存在流程名称“'+self.add_text+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'13.png')
            print u'【错误截图】：'+self.img_text+'13.png'
            return
        #判断标题、签批状态、发送人是否正确
        try:
            if bt_text!=self.add_text or qpzt_text!=u'中转' or fsr_text!=self.zz_text:
                print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",有误'
                raise NameError('data erro')
            else :print u'名称、标题、签批状态"'+bt_text+u'、'+qpzt_text+u'、'+fsr_text+u'",正确'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.add_text+u'”，标题或签批状态或发送人不正确'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'14.png')
            print u'【错误截图】：'+self.img_text+'14.png'
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()
        time.sleep(2)
        #上传附件
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='tbFilePost_FileUpload']").click()
        frame=driver.find_element_by_css_selector('.fancybox-inner')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        driver.find_element_by_id("tbFilePost_uploadify").click()
        time.sleep(3)
        os.startfile(os.getcwd().split('testcase_firefox')[0]+'\uploadfile\Fox_gw_doc.exe')
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='tbFilePost_OK']").click()
        time.sleep(1)
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.find_element_by_xpath(".//*[@id='IBHasOption']").click()
        driver.find_element_by_xpath(".//*[@id='tbConten']").send_keys(self.js_text+u'同意')
        driver.find_element_by_xpath(".//*[@id='IB_over']").click()
        time.sleep(5)
        driver.quit()
        print self.js_text+u'完成结束流程'
        #完成马婧结束流程---------------------
        #提交人（冯学冠）在公文查询里，查看流程是否正确---------------------
        print self.tj_text+u'开始在公文查询查询流程'
        time.sleep(1)
        closewindow.close_window('Plugin Container for Firefox')
        login.login_normal(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-675c548c-97c9-4f10-9eab-ba0ed7db2594']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbKeyName']").send_keys(self.add_text)
        #先定位到下拉框
        m=driver.find_element_by_id("ddlType")
        #再点击下拉框下的选项
        m.find_element_by_xpath("//option[@value='100402']").click()
        m=driver.find_element_by_id("ddlDetailType")
        m.find_element_by_xpath("//option[@value='tb164']").click()
        time.sleep(0.5)
        js="$(\"input[id='ctrStartDate']\").attr('value','2016-01-01')"
        driver.execute_script(js)
        time.sleep(0.5)
        js="$(\"input[id='ctrEndDate']\").attr('value','12-12')"
        driver.execute_script(js)
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='IB_search']").click()
        time.sleep(1)
        try:
            bt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").text
            gwlx_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            cjr_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'没有存在流程名称“'+self.add_text+'”'
            return
        #判断标题、公文类型、创建人是否正确
        try:
            if bt_text!=self.add_text or gwlx_text!=u'办文呈批单' or cjr_text!=self.tj_text:
                print u'标题、公文类型、创建人"'+bt_text+u'、'+gwlx_text+u'、'+cjr_text+u'",有误'
                raise NameError('data erro')
            else :print u'标题、公文类型、创建人"'+bt_text+u'、'+gwlx_text+u'、'+cjr_text+u'",正确'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.add_text+u'”，标题、公文类型、创建人有误'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'15.png')
            print u'【错误截图】：'+self.img_text+'15.png'
        driver.quit()
        print self.tj_text+u'完成在公文查询查询流程'
        #完成提交人（冯学冠）在公文查询里，查看流程是否正确---------------------
        #签批人（符晓玲）在公文查询里，查看流程（签批）是否正确---------------------
        print self.qp_text+u'开始在公文查询查询流程（签批）'
        time.sleep(1)
        login.login_normal2(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-675c548c-97c9-4f10-9eab-ba0ed7db2594']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='txbKeyName']").send_keys(self.hq)
        #先定位到下拉框
        m=driver.find_element_by_id("ddlType")
        #再点击下拉框下的选项
        m.find_element_by_xpath("//option[@value='100402']").click()
        m=driver.find_element_by_id("ddlDetailType")
        m.find_element_by_xpath("//option[@value='tb164']").click()
        js="$(\"input[id='ctrStartDate']\").attr('value','2016-01-01')"
        driver.execute_script(js)
        js="$(\"input[id='ctrEndDate']\").attr('value','12-12')"
        driver.execute_script(js)
        driver.find_element_by_xpath(".//*[@id='rbYes']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='IB_search']").click()
        time.sleep(1)
        try:
            bt_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").text
            gwlx_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            cjr_text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'没有存在流程名称“'+self.hq+'”'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'16.png')
            print u'【错误截图】：'+self.img_text+'16.png'
            return
        #判断标题、公文类型、创建人是否正确
        try:
            if bt_text!=self.hq or gwlx_text!=u'办文呈批单会签件' or cjr_text!=self.qp_text:
                print u'标题、公文类型、创建人"'+bt_text+u'、'+gwlx_text+u'、'+cjr_text+u'",有误'
                raise NameError('data erro')
            else :print u'标题、公文类型、创建人"'+bt_text+u'、'+gwlx_text+u'、'+cjr_text+u'",正确'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.hq+u'”，标题、公文类型、创建人有误'
            ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'17.png')
            print u'【错误截图】：'+self.img_text+'17.png'
        driver.quit()
        print self.qp_text+u'完成在公文查询查询流程（签批）'
        #完成签批人（符晓玲）在公文查询里，查看流程（签批）是否正确---------------------
        #提交人（冯学冠）在待阅事务里，查看流程是否正确，并分发（丁娥）-----------
        print self.tj_text+u'开始在待阅事务里，查看流程是否正确，并分发给：'+self.ffr_text
        time.sleep(1)
        login.login_normal(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-6c73c99c-ce6c-49ab-a5b7-b7a827994667']/a").click()
        time.sleep(2)
        #遍历待阅事务里的流程*************************
        driver.switch_to_frame("diaConIf")
        index = 0
        while 1:
            text=driver.find_element_by_xpath(".//*[@id='vpFinish']/table/tbody/tr/td[2]/span[1]").text
            if len(text)!=8:
                print u'在待阅事务获取页数出错'
                self.verificationErrors.append('data of Transaction to be read erro')
                ImageGrab.grab().save(os.getcwd().split('testcase_firefox')[0]+'\\img\\'+self.img_text+'.png')
                print u'【错误截图】：'+self.img_text+'.png'
                break
            num1=text[2]
            num2=text[4]
            table=driver.find_element_by_id("dgQuery")
            drs=table.find_elements_by_tag_name('tr')
            time.sleep(3)
            if len(drs)>0:
                for i in range(len(drs)-1):#由于一般表都有表头，而表头只是一些标题而已不是需要的数据所以len(drs)-1
                    xpath1=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[2]/label"
                    xpath2=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[3]"
                    xpath3=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[4]"
                    xpath4=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[6]"
                    xpath5=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[7]"
                    bt_text=driver.find_element_by_xpath(xpath1).text
                    gwlx_text=driver.find_element_by_xpath(xpath2).text
                    ffr_text=driver.find_element_by_xpath(xpath3).text
                    cbr_text=driver.find_element_by_xpath(xpath4).text
                    ydzt_text=driver.find_element_by_xpath(xpath5).text
                    if bt_text==self.add_text and gwlx_text==u'办文呈批单' and ffr_text==self.js_text and cbr_text==self.tj_text and ydzt_text==u'未阅':
                        index=1
                        bt_xpath=xpath1
                        break
            if index==1 or num1==num2:break
            else:
                #点击下一页
                driver.find_element_by_xpath(".//*[@id='vpFinish']/table/tbody/tr/td[2]/a[3]").click()
        #完成遍历待阅事务里的流程*************************
        #将流程暂存待阅，并分发给组*********
        if index==1:
            print u'在待阅事务里存在流程名称：”'+self.add_text+'“，并且信息正确'
            driver.find_element_by_xpath(bt_xpath).click()
            time.sleep(2)
            #点开收件人选择
            driver.switch_to_window(nowhandle)
            driver.switch_to_frame("_DialogFrame_0")
            driver.find_element_by_xpath(".//*[@id='SelectUser_imgBt']").click()
            time.sleep(1)
            allhandles=driver.window_handles
            time.sleep(1)
            #切换到收件人窗口
            driver.switch_to_window(allhandles[1])
            driver.switch_to_frame("mainFrame")
            driver.find_element_by_xpath(".//*[@id='tb_Search']").send_keys(self.ffz_text)
            driver.find_element_by_xpath(".//*[@id='btn_Search']").click()
            time.sleep(1)
            driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
            time.sleep(1)
            driver.find_element_by_id("ibtSubmit").click()
            time.sleep(1)
            driver.switch_to_window(nowhandle)
            driver.switch_to_frame("_DialogFrame_0")
            driver.find_element_by_xpath(".//*[@id='txbOpion']").send_keys(self.tj_text+u'进行分发')
            driver.find_element_by_xpath(".//*[@id='btnSend']").click()
            time.sleep(10)
            driver.find_element_by_xpath(".//*[@id='btnSave']").click()
            time.sleep(10)
        else:
            print u'在待阅事务里没有存在流程名称：”'+self.add_text+'“，或者信息不正确'
            self.verificationErrors.append('data of Transaction to be read erro')
            return
        #完成流程暂存待阅，并分发给组*********
        #查询暂存是否成功，且是否处于已阅******
        driver.switch_to_window(nowhandle)
        driver.switch_to_frame("diaConIf")
        index = 0
        while 1:
            text=driver.find_element_by_xpath(".//*[@id='vpFinish']/table/tbody/tr/td[2]/span[1]").text
            if len(text)!=8:
                print u'在待阅事务获取页数出错'
                self.verificationErrors.append('get the pages of Transaction to be read fail')
                return
            num1=text[2]
            num2=text[4]
            table=driver.find_element_by_id("dgQuery")
            drs=table.find_elements_by_tag_name('tr')
            time.sleep(3)
            if len(drs)>0:
                for i in range(len(drs)-1):#由于一般表都有表头，而表头只是一些标题而已不是需要的数据所以len(drs)-1
                    xpath1=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[2]/label"
                    xpath2=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[3]"
                    xpath3=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[4]"
                    xpath4=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[6]"
                    xpath5=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[7]"
                    bt_text=driver.find_element_by_xpath(xpath1).text
                    gwlx_text=driver.find_element_by_xpath(xpath2).text
                    ffr_text=driver.find_element_by_xpath(xpath3).text
                    cbr_text=driver.find_element_by_xpath(xpath4).text
                    ydzt_text=driver.find_element_by_xpath(xpath5).text
                    if bt_text==self.add_text and gwlx_text==u'办文呈批单' and ffr_text==self.js_text and cbr_text==self.tj_text and ydzt_text==u'已阅':
                        index=1
                        break
            if index==1 or num1==num2:break
            else:
                driver.find_element_by_xpath(".//*[@id='vpFinish']/table/tbody/tr/td[2]/a[3]").click()
        if index==1:
            print u'在待阅事务里存在流程名称：”'+self.add_text+'“，信息正确，阅读状态为“已阅”'
        else:
            print u'在待阅事务里没有存在流程名称：”'+self.add_text+'“，或者信息不正确'
            self.verificationErrors.append('data of Transaction to be read erro')
            return
        #完成查询暂存是否成功，且是否处于已阅******
        driver.quit()
        print self.tj_text+u'完成在待阅事务里，查看流程是否正确，并分发给：'+self.ffr_text
        #完成提交人（冯学冠）在待阅事务里，查看流程（签批）是否正确，并分发（黄娜）-----------
        #分发组里的某个人（黄娜）在待阅事务里，查看流程状态是否正确-----------
        print self.ffr_text+u'开始在待阅事务里，查看流程否是正确'
        time.sleep(1)
        login.login_normal8(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='nav-6c73c99c-ce6c-49ab-a5b7-b7a827994667']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        index = 0
        while 1:
            text=driver.find_element_by_xpath(".//*[@id='vpFinish']/table/tbody/tr/td[2]/span[1]").text
            if len(text)!=8:
                print u'在待阅事务获取页数出错'
                self.verificationErrors.append('data of Transaction to be read erro')
                return
            num1=text[2]
            num2=text[4]
            table=driver.find_element_by_id("dgQuery")
            drs=table.find_elements_by_tag_name('tr')
            time.sleep(3)
            if len(drs)>0:
                for i in range(len(drs)-1):#由于一般表都有表头，而表头只是一些标题而已不是需要的数据所以len(drs)-1
                    xpath1=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[2]/label"
                    xpath2=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[3]"
                    xpath3=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[4]"
                    xpath4=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[6]"
                    xpath5=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[7]"
                    bt_text=driver.find_element_by_xpath(xpath1).text
                    gwlx_text=driver.find_element_by_xpath(xpath2).text
                    ffr_text=driver.find_element_by_xpath(xpath3).text
                    cbr_text=driver.find_element_by_xpath(xpath4).text
                    ydzt_text=driver.find_element_by_xpath(xpath5).text
                    if bt_text==self.add_text and gwlx_text==u'办文呈批单' and ffr_text==self.tj_text and cbr_text==self.tj_text and ydzt_text==u'未阅':
                        index=1
                        bt_xpath=xpath1
                        gwlx_xpath=xpath2
                        ffr_xpath=xpath3
                        cbr_xpath=xpath4
                        ydzt_xpath=xpath5
                        break
            if index==1 or num1==num2:break
            else:
                driver.find_element_by_xpath(".//*[@id='vpFinish']/table/tbody/tr/td[2]/a[3]").click()
        if index==1:
            print u'在待阅事务里存在流程名称：”'+self.add_text+'“，并且信息正确'
        else:
            print u'在待阅事务里没有存在流程名称：”'+self.add_text+'“，或者信息不正确'
            self.verificationErrors.append('status or data of Transaction to be read erro')
            return
        print self.ffr_text+u'完成在待阅事务里，查看流程否是正确'
        #完成分发组里的某个人（黄娜）在待阅事务里，查看流程状态是否正确-----------
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
        closewindow.close_window('Plugin Container for Firefox')

if __name__ == "__main__":
    unittest.main()
