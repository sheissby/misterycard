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

class zdh_bwcp_cg_del (unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.add_text='bwcp_cg_edt'+now
        self.wjbh_text='wjbh'+now
        self.tj_text=u'冯学冠'
        self.qp_text=u'符晓玲'
        self.img_text='img_bwcp_cg_edt_error'
    
    def test_zdh_bwcp_cg_del (self):
        u"""办文呈批单草稿删除"""
        print self.tj_text+u'开始提交办文呈批单流程，名称为：'+self.add_text
        login.login_normal(self)
        driver = self.driver
        allhandlelist=[]
        nowhandle=driver.current_window_handle
        allhandlelist.append(nowhandle)
        #进入公文呈报
        driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[1]/a").click()
        time.sleep(2)
        driver.switch_to_frame("diaConIf")
        driver.find_element_by_xpath("html/body/div[2]/div/table[1]/tbody/tr/td[2]/div/ul/li/table/tbody/tr/td[1]/a").click()
        driver.switch_to.default_content()
        time.sleep(1)
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)
        #添加流程信息*******************
        driver.find_element_by_xpath(".//*[@id='080108']").click()
        #获取当前时间输入到日期控件
        driver.find_element_by_xpath(".//*[@id='fab70432-fe83-4754-a419-76d752f8e0fd']").send_keys(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='2da0c1a9-76d0-402d-a4f4-566472a6daf4']").send_keys(time.strftime("%Y-%m-%d", time.localtime()))
        time.sleep(2)
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
        time.sleep(1)
        #删除没有的窗口句柄
        allhandlelist.pop()
        time.sleep(1)
        #选择窗口1（原窗口）
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
        #选择窗口1（即源窗口）
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
        driver.find_element_by_id("bt_Save").click()
        time.sleep(8)
        #完成添加流程信息******************
        print self.tj_text+u'完成提交办文呈批单流程，名称为：'+self.add_text
        print self.tj_text+u'开始在公文草稿箱里查询办文呈批单流程名称：'+self.add_text+',并做删除操作'
        driver.switch_to.default_content()
        #点击草稿箱
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/a").click()
        time.sleep(1)
        #遍历公文草稿箱里刚才保存的流程*************************
        driver.switch_to_frame("diaConIf")
        index = 0
        while 1:
            time.sleep(3)
            text=driver.find_element_by_xpath(".//*[@id='vpFinish']/table/tbody/tr/td[2]/span[1]").text
            if len(text)!=8:
                print u'在公文草稿箱获取页数出错'
                self.verificationErrors.append('data of Transaction to be read erro')
                break
            #提取出里面的数字
            nums=re.findall(r"\d+\.?\d*",text)
            #获取当前页数
            num1=nums[0]
            #获取总页数
            num2=nums[1]
            table=driver.find_element_by_id("dgQuery")
            drs=table.find_elements_by_tag_name('tr')
            if len(drs)>0:
                for i in range(len(drs)-1):#由于一般表都有表头，而表头只是一些标题而已不是需要的数据所以len(drs)-1
                    xpath1=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[2]/label"
                    xpath2=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[3]"
                    #删除按钮路径
                    xpath3=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[5]"
                    bt_text=driver.find_element_by_xpath(xpath1).text
                    gwlx_text=driver.find_element_by_xpath(xpath2).text
                    if bt_text==self.add_text and gwlx_text==u'办文呈批单':
                        index=1
                        del_xpath=xpath3
                        break
            if index==1 or num1==num2:break
            else:
                #点击下一页
                driver.find_element_by_xpath(".//*[@id='vpFinish']/table/tbody/tr/td[2]/a[3]").send_keys('')
                win32api.keybd_event(13,0,0,0)
                win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        #完成遍历公文草稿箱里刚才保存的流程*************************
        #如果存在保存的流程就进行删除取消和删除操作
        if index==1:
            print u'在公文草稿箱里存在流程名称：”'+self.add_text+'“，并且信息正确'
            driver.find_element_by_xpath(del_xpath).click()
            time.sleep(2)
            alert=driver.switch_to_alert()
            alert.dismiss()
            time.sleep(1)
            driver.find_element_by_xpath(del_xpath).click()
            time.sleep(2)
            alert=driver.switch_to_alert()
            alert.accept()
        else:
            print u'在公文草稿箱里没有存在流程名称：”'+self.add_text+'“，或者信息不正确'
            self.verificationErrors.append('Document Flow Process does not exist')
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'1.png')
            print u'错误截图：'+self.img_text+'1.png'
            return
        time.sleep(2) 
        driver.switch_to.default_content()
        #点击草稿箱
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[6]/a").click()
        #遍历公文草稿箱里刚才保存的流程*************************
        driver.switch_to_frame("diaConIf")
        index = 0
        while 1:
            time.sleep(3)
            text=driver.find_element_by_xpath(".//*[@id='vpFinish']/table/tbody/tr/td[2]/span[1]").text
            if len(text)==0:
                print u'在公文草稿箱获取页数出错'
                self.verificationErrors.append('data of Transaction to be read erro')
                ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'2.png')
                print u'错误截图：'+self.img_text+'2.png'
                break
            #提取出里面的数字
            nums=re.findall(r"\d+\.?\d*",text)
            #获取当前页数
            num1=nums[0]
            #获取总页数
            num2=nums[1]
            table=driver.find_element_by_id("dgQuery")
            drs=table.find_elements_by_tag_name('tr')
            if len(drs)>0:
                for i in range(len(drs)-1):#由于一般表都有表头，而表头只是一些标题而已不是需要的数据所以len(drs)-1
                    #获取标题路径
                    xpath1=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[2]/label"
                    #获取公文类型路径
                    xpath2=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[3]"
                    #获取删除按钮路径
                    xpath3=".//*[@id='dgQuery']/tbody/tr["+str(i+2)+"]/td[5]"
                    bt_text=driver.find_element_by_xpath(xpath1).text
                    gwlx_text=driver.find_element_by_xpath(xpath2).text
                    if bt_text==self.add_text and gwlx_text==u'办文呈批单':
                        index=1
                        del_xpath=xpath3
                        break
            if index==1 or num1==num2:break
            else:
                #点击下一页
                driver.find_element_by_xpath(".//*[@id='vpFinish']/table/tbody/tr/td[2]/a[3]").send_keys('')
                win32api.keybd_event(13,0,0,0)
                win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        #完成遍历公文草稿箱里刚才保存的流程*************************
        #如果存在保存的流程就做删除取消和删除操作************
        if index==0:
            print u'删除成功，在在公文草稿箱里删除流程名称：”'+self.add_text
            time.sleep(2)
        else:
            print u'删除失败，在在公文草稿箱里未能删除流程名称：'+self.add_text
            self.verificationErrors.append('Document Flow Process exist')
            ImageGrab.grab().save(os.getcwd().split('testcase_ie')[0]+'\\img\\'+self.img_text+'3.png')
            print u'错误截图：'+self.img_text+'3.png'
            return
        print self.tj_text+u'完成在公文草稿箱里查询办文呈批单流程名称：'+self.add_text+',并做删除操作'
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
        time.sleep(2)
        closewindow.close_window('Plugin Container for Firefox')

if __name__ == "__main__":
    unittest.main()
