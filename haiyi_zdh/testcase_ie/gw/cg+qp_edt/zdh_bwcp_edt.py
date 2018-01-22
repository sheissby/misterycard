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
import closewindow
import win32api
import win32con
from PIL import ImageGrab

class zdh_bwcp_edt(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.add_text='bwcp_edt'+now
        self.wjbh_text='wjbh'+now
        self.wjbh2_text='2wjbh'+now
        self.tj_text=u'冯学冠'
        self.qp_text=u'符晓玲'
        self.img_text='img_bwcp_edt_error'
    
    def test_zdh_bwcp_edt(self):
        u"""办文呈批单签批修改"""
        print self.tj_text+u'开始提交办文呈批单流程，名称为：'+self.add_text
        login.login_normal(self)
        driver = self.driver
        allhandlelist=[]
        nowhandle=driver.current_window_handle
        allhandlelist.append(nowhandle)
        #进入公文呈报
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='nav-c0baf144-2241-471a-8947-db8511046075']/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath("html/body/div[2]/div/table[1]/tbody/tr/td[2]/div/ul/li/table/tbody/tr/td[1]/a").click()
        driver.switch_to.default_content()
        time.sleep(1)
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)
        #添加流程信息*******************
        driver.find_element_by_xpath(".//*[@id='080108']").click()
        #日期控件
        #driver.find_element_by_xpath(".//*[@id='fab70432-fe83-4754-a419-76d752f8e0fd']").send_keys(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(1)
        js="$(\"input[id='fab70432-fe83-4754-a419-76d752f8e0fd']\").removeAttr('readonly');$(\"input[id='fab70432-fe83-4754-a419-76d752f8e0fd']\").attr('value','"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"')"
        driver.execute_script(js)
        #driver.find_element_by_xpath(".//*[@id='2da0c1a9-76d0-402d-a4f4-566472a6daf4']").send_keys(time.strftime("%Y-%m-%d", time.localtime()))
        time.sleep(2)
        js="$(\"input[id='2da0c1a9-76d0-402d-a4f4-566472a6daf4']\").removeAttr('readonly');$(\"input[id='2da0c1a9-76d0-402d-a4f4-566472a6daf4']\").attr('value','"+time.strftime("%Y-%m-%d", time.localtime())+"')"
        driver.execute_script(js)
        driver.switch_to.default_content()
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)
        set_textbox_js = 'document.getElementById("2fff7b71-4436-4646-815b-a61f31b61574").value="'+self.add_text+'"'
        driver.execute_script(set_textbox_js)
        time.sleep(1)
        set_textbox_js = 'document.getElementById("2ab2465a-d822-4b56-bd42-a4900a20f4e8").value="10"'
        driver.execute_script(set_textbox_js)
        #点开发放范围选择
        time.sleep(1)
        #定位到要双击的元素
        double =driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[6]/td[1]/img")
        #对定位到的元素执行鼠标双击操作
        ActionChains(driver).double_click(double).perform()
        #driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[6]/td[1]/img").click()
        #切换到发放范围窗口
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        #将获取当前所有窗口与allhandlelist的差集加到allhandlelist后面（连接到allhandlelist）
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        driver.switch_to_frame("mainFrame")
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(1)
        driver.find_element_by_id("ibtSubmit").click()
        #删除没有的窗口句柄
        allhandlelist.pop()
        time.sleep(1)
        driver.switch_to_window(allhandlelist[0])
        driver.switch_to_frame("_DialogFrame_0")
        #点开收件人选择
        time.sleep(1)
        #定位到要双击的元素
        double =driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[8]/td[1]/img")
        #对定位到的元素执行鼠标双击操作
        ActionChains(driver).double_click(double).perform()
        #driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[8]/td[1]/img").click()
        #切换到收件人窗口
        time.sleep(2)
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        #将获取当前所有窗口与allhandlelist的差集加到allhandlelist后面（连接到allhandlelist）
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        driver.switch_to_frame("mainFrame")
        driver.find_element_by_xpath(".//*[@id='tb_Search']").send_keys(self.qp_text)
        driver.find_element_by_xpath(".//*[@id='btn_Search']").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='ibtAddMsg']").click()
        time.sleep(1)
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(2)
        #上传附件
        #删除没有的窗口句柄
        allhandlelist.pop()
        time.sleep(1)
        driver.switch_to_window(allhandlelist[0])
        driver.switch_to_frame("_DialogFrame_0")
        driver.find_element_by_xpath(".//*[@id='tbFilePost_FileUpload']").click()
        frame=driver.find_element_by_css_selector('.fancybox-inner')
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        driver.find_element_by_id("tbFilePost_uploadify").click()
        time.sleep(3)
        os.startfile(os.getcwd().split('testcase_ie')[0]+'\uploadfile\Ie_gw_doc.exe')
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='tbFilePost_OK']").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.switch_to_frame("_DialogFrame_0")
        driver.find_element_by_xpath(".//*[@id='77891a1e-5e2e-4fdd-a8d0-9c99eed17437']").send_keys(self.wjbh_text)
        #获取添加属性值
        qwbm_text=driver.find_element_by_id("SelectOnlyAccount_txbText8").get_attribute('value')
        fffw_text=driver.find_element_by_id("SelectOnlyAccount_txbText14").get_attribute('value')
        ngr_text=driver.find_element_by_id("SelectOnlyAccount_txbText9").get_attribute('value')
        yffs_text=driver.find_element_by_id("2ab2465a-d822-4b56-bd42-a4900a20f4e8").get_attribute('value')
        qwsj_text=driver.find_element_by_id("fab70432-fe83-4754-a419-76d752f8e0fd").get_attribute('value')
        yfrq_text=driver.find_element_by_id("2da0c1a9-76d0-402d-a4f4-566472a6daf4").get_attribute('value')
        driver.find_element_by_id("bt_Submit").click()
        time.sleep(8)
        #完成添加流程信息******************
        print self.tj_text+u'完成提交办文呈批单流程，名称为：'+self.add_text
        driver.quit()
        #会签人(符晓玲)查询是否存在流程，并修改缓急和文件编号----------------------------
        #换账号登录
        print self.qp_text+u'开始查询是否存在流程：'+self.add_text+u',并修改缓急和文件编号'
        time.sleep(1)
        #删除没有的窗口句柄
        allhandlelist.pop()
        closewindow.close_window('Plugin Container for Firefox')
        login.login_normal2(self)
        driver = self.driver
        nowhandle=driver.current_window_handle
        allhandlelist.append(nowhandle)
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
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'1.png')
            print u'错误截图：'+self.img_text+'1.png'
            return
        #判断标题、签批状态、发送人是否正确
        index=0
        try:
            if bt_text==self.add_text and qpzt_text==u'签批' and fsr_text==self.tj_text:
                print u'名称"'+self.add_text+u'",标题、签批状态、发送人正确'
                index=1
            else :
                print u'名称"'+self.add_text+u'",标题、签批状态、发送人存在有误'
                raise NameError('data erro')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.add_text+u'”，标题或签批状态或发送人不正确'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'2.png')
            print u'错误截图：'+self.img_text+'2.png'
        if index==1:
            driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()
            time.sleep(2)
            driver.switch_to.default_content()
            driver.switch_to_frame("_DialogFrame_diagSignMainBox")
            driver.switch_to_frame("dFrame")
            gwbt_text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[2]/td").text
            qwbm_text2=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[3]/td[1]").text
            fffw_text2=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[6]/td[1]").text
            ngr_text2=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[3]/td[2]").text
            yffs_text2=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[5]/td[2]").text
            qwsj_text2=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[4]/td[1]").text
            yfrq_text2=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[5]/td[1]").text
            wjbh_text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[8]/td/span").text
            hj_text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[7]/td[1]/span").text
            if gwbt_text==self.add_text and qwbm_text2==qwbm_text and fffw_text2==fffw_text and ngr_text2==ngr_text and\
            yffs_text2==yffs_text and qwsj_text2==qwsj_text and yfrq_text2==yfrq_text and wjbh_text==self.wjbh_text and hj_text==u'平件':
                print u'名称"'+self.add_text+u'",属性值与提交的属性值一致'
                driver.switch_to.default_content()
                driver.switch_to_frame("_DialogFrame_diagSignMainBox")
                driver.find_element_by_id("btnIBModify").click()
                time.sleep(2)
                driver.switch_to.default_content()
                driver.switch_to_frame("_DialogFrame_diagModifyBox")
                driver.find_element_by_id("77891a1e-5e2e-4fdd-a8d0-9c99eed17437").clear()
                driver.find_element_by_id("77891a1e-5e2e-4fdd-a8d0-9c99eed17437").send_keys(self.wjbh2_text)
                driver.find_element_by_id("080106").click()
                driver.find_element_by_id("bt_Submit").click()
                time.sleep(7)
                driver.switch_to.default_content()
                driver.find_element_by_xpath(".//*[@id='_Draghandle_diagSignMainBox']/td[2]/div[2]").click()
                time.sleep(2)
            else:
                print u'名称"'+self.add_text+u'",属性值与提交的属性值不一致'
                self.verificationErrors.append('Property values are not consistent')
                ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'3.png')
                print u'错误截图：'+self.img_text+'3.png'
                return
        else:
            print u'流程签批查询有存在流程名称：”'+self.add_text+'“，或者信息不正确'
            self.verificationErrors.append('Document Flow Process does not exist or data erro')
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'4.png')
            print u'错误截图：'+self.img_text+'4.png'
            return
        driver.switch_to.default_content()
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath(".//*[@id='ctrTitle']").clear()
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
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'5.png')
            print u'错误截图：'+self.img_text+'5.png'
            return
        #判断标题、签批状态、发送人是否正确
        index=0
        try:
            if bt_text==self.add_text and qpzt_text==u'签批' and fsr_text==self.tj_text:
                print u'名称"'+self.add_text+u'",标题、签批状态、发送人正确'
                index=1
            else :
                print u'名称"'+self.add_text+u'",标题、签批状态、发送人存在有误'
                raise NameError('data erro')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'流程名称“'+self.add_text+u'”，标题或签批状态或发送人不正确'
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'6.png')
            print u'错误截图：'+self.img_text+'6.png'
        if index==1:
            driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()
            time.sleep(2)
            driver.switch_to.default_content()
            driver.switch_to_frame("_DialogFrame_diagSignMainBox")
            driver.switch_to_frame("dFrame")
            wjbh2_text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[8]/td/span").text
            hj2_text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[7]/td[1]/span").text
            if wjbh2_text==self.wjbh2_text and hj2_text==u'急件':
                print self.qp_text+u'修改文件编号和缓急成功修改为：'+wjbh2_text+','+hj2_text
            else:
                print self.qp_text+u'修改文件编号和缓急失败'
                self.verificationErrors.append('Document Flow Process Modify Failed')
                ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'7.png')
                print u'错误截图：'+self.img_text+'7.png'
        else:
            print u'流程签批查询有存在流程名称：”'+self.add_text+'“，或者信息不正确'
            self.verificationErrors.append('Document Flow Process does not exist or data erro')
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'8.png')
            print u'错误截图：'+self.img_text+'8.png'
            return
        print self.qp_text+u'开完成查询是否存在流程：'+self.add_text+u',并修改缓急和文件编号'
        time.sleep(2)
        #完成会签人(符晓玲)查询是否存在流程，并修改缓急和文件编号----------------------------
        
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
