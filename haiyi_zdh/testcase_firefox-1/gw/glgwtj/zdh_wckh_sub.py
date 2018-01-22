# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#引用各种包
import unittest,time,re,os
#引用火狐插件包
from selenium.webdriver.firefox.webdriver import FirefoxProfile
#引用移动鼠标包
from selenium.webdriver.common.action_chains import ActionChains
#操作Windows应用程序 或者操作鼠标键盘用的包
import win32api
import win32con
#调用登录、退出
from haiyi_zdh.public.firefox import login
#调用关闭Plugin Container 冲突窗口
import closewindow

#案例
class zdh_wckh_sub(unittest.TestCase):
    def setUp(self):
        
        #用户登录------------------------------------------------------------------------------------------
        #调用登录函数
        login.login_normal(self)
        #错误信息被打印、接收警告
        self.verificationErrors = []
        self.accept_next_alert = True
        
        #定义字段取值+++++++++++++++++++++++++++++++++++++++++
        #获取当前时间的函数
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        #定义公文标题+当前时间的函数
        self.sub_text='wckh_sub'+now
        #定义公文收件人、呈报人、参会人员（姓名、职称、联系电话）、所属科室、参加会议(班)内容
        self.sub_text2=u'符晓玲'
        self.sub_text3=u'冯学冠'
        self.sub_text4=u'张三'
        self.sub_text14=u'输血科'
        self.sub_text15=u'医院护士'
        self.sub_text16=u'13398991939'
        self.sub_text17=u'参加研讨会'
        self.sub_text18=u'姓名：张三  职称：医院护士  联系电话：13398991939'
        
        #显示用例名称
        print u'---------------《外出开会申请单提交功能自动化测试》----------------------'
        
    def test_zdh_wckh_sub(self):
        
        #打开公文管理-公文呈报-外出开会申请单-------------------------------------------------------------------
        #打开浏览器
        driver = self.driver
        #定位且鼠标移到公文管理模块
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        #点击公文呈报导航链接，设置思考时间
        driver.find_element_by_xpath(".//*[@id='nav-c0baf144-2241-471a-8947-db8511046075']/a").click()
        time.sleep(1)
        #定位到外出开会申请单的所属框架
        driver.switch_to_frame("diaConIf")  
        #点击外出开会申请单链接
        driver.find_element_by_xpath("html/body/div[2]/div/table[1]/tbody/tr/td[2]/div/ul/li/table/tbody/tr/td[4]/a").click()
        time.sleep(1)   

        #配置字段属性，点击提交-------------------------------------------------------------------------------
        #获取呈报页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")
        
        #输入标题、参会人员中的（姓名、职称、联系电话）、会议办内容字段值+++++++++++++++++++++++++
        time.sleep(1)
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").clear()
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").send_keys(self.sub_text)        
        driver.find_element_by_id("ctrUserName_0").send_keys(self.sub_text4)
        driver.find_element_by_id("ctrUserPost_0").send_keys(self.sub_text15)
        driver.find_element_by_id("ctrUserPhone_0").send_keys(self.sub_text16)
        driver.find_element_by_id("274c9e3e-6050-491f-90dc-8e9c9d11e3bb").send_keys(self.sub_text17)
        time.sleep(1)
        
        #所属科室选择++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #点击机构选择按钮       
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[3]/td/img").click()
        #定位到机构选择页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        time.sleep(1)
        #定位到机构选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询机构
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text14)
        #点击查询、添加、提交机构
        driver.find_element_by_id("btn_Search").click()
        driver.find_element_by_id("ibtAddMsg").click()
        driver.find_element_by_id("ibtSubmit").click()
        #获取呈报页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)
       
        #收件人选择+++++++++++++++++++++++++++++++++++++
        #点击收件人选择按钮
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[6]/td/img").click()
        #定位到人员选择页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        time.sleep(1)
        #定位到人员选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询人员
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text2)
        #点击查询、添加、提交人员
        driver.find_element_by_id("btn_Search").click()
        driver.find_element_by_id("ibtAddMsg").click()
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(1)
        #获取呈报页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")

        #附件选择++++++++++++++++++++++++++++++++++++++++
        #定位到附件
        driver.find_element_by_id("tbFilePost_FileUpload").send_keys("")
        #模拟键盘操作
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(1)       
        #获取附件操作的所有和本层窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])       
        time.sleep(1)
        #定位到附件上传框架
        driver.switch_to_frame("_DialogFrame_0")
        #找div class="fancybox-inner"，定位增加文件按钮的frame
        frame=driver.find_element_by_css_selector('.fancybox-inner')
        #遍历下方的iframe
        frames=frame.find_elements_by_tag_name('iframe')
        #取第1个iframe
        driver.switch_to_frame(frames[0])
        #单击增加文件按钮
        driver.find_element_by_id("SWFUpload_0").click()
        time.sleep(1)
        #调用auto工具保存的附件上传word文件
        os.startfile(os.getcwd().split('testcase_firefox')[0]+'\uploadfile\Fox_gw_doc.exe')
        time.sleep(4)
        #点击添加
        driver.find_element_by_id("tbFilePost_OK").click()
        time.sleep(1)  
        #获取呈报页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)

        #获取字段值++++++++++++++++++++++++++++++++++++++++
        #获取申请单号、缓急、密级、正文附件的字段值
        self.sub_text5=driver.find_element_by_id("991fc9b0-73e5-40f1-887f-5ec7566bacd2").get_attribute('value')
        self.sub_text8=driver.find_element_by_id("080105").get_attribute('value')
        self.sub_text9=driver.find_element_by_id("080102").get_attribute('value')
        self.sub_text12=driver.find_element_by_xpath(".//*[@id='tbFilePost_labFilesLink']/ul/li/a[1]").text
          
        #将缓急、密级字段的值左边的1|去掉（取从左边数2位后的内容）
        self.sub_text10=self.sub_text8[2:]
        self.sub_text11=self.sub_text9[2:]
        
        #点击提交按钮
        driver.find_element_by_id("bt_Submit").click()
        time.sleep(4)
        print u'可正常提交公文'
        
        #使用符晓玲（200518）登录-----------------------------------------------------------------
        #获取当前窗口
        nowhandle=driver.current_window_handle
        #回到原窗口
        driver.switch_to_window(nowhandle)
        time.sleep(1)       
        #杀掉火狐对插件不兼容的提示。调用登录函数++++++++++++++++++
        #关闭页面
        driver.quit()
##        os.system("taskkill /F /IM plugin-container.exe")
        time.sleep(1)
        closewindow.close_window('Plugin Container for Firefox')
        time.sleep(1)
        login.login_normal2(self)
        
        #打开公文管理-公文签批------------------------------------------------------------------------------------------
        #重新打开浏览器
        driver = self.driver
        #定位且鼠标移到公文管理模块
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        #点击公文签批导航链接
        driver.find_element_by_xpath(".//*[@id='nav-70f461d6-02d9-4a0e-9c75-1b38aa29da02']/a").click()
        #思考时间
        time.sleep(1)

        #输入字段，进行查询---------------------------------------------------------------------------------------------
        #获取当前窗口
        nowhandle=driver.current_window_handle
        #定位到公文签批查询字段的所属框架
        driver.switch_to_frame("diaConIf")
        
        #输入标题、接文时间
        driver.find_element_by_id("ctrTitle").send_keys(self.sub_text)
        driver.find_element_by_id("ctrStartDate").send_keys(u'2016-01-01')
        driver.find_element_by_id("ctrEndDate").send_keys(u'12-31')
        
        #定位和选择公文类型的下拉框
        ddlType=driver.find_element_by_id('ddlType')
        ddlType.find_element_by_xpath("//option[@value='100402']").click()
        ddlDetailType=driver.find_element_by_id('ddlDetailType')
        ddlDetailType.find_element_by_xpath("//option[@value='tb167']").click()
        
        #发送人选择+++++++++++++++++++++++++++++++++++++++
        #点击发送人选择按钮
        driver.find_element_by_xpath(".//*[@id='ctrUser_imgBt']").click()
        #定位到人员选择页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        time.sleep(1)
        #定位到人员选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询人员
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text3)
        #点击查询、添加、提交人员
        driver.find_element_by_id("btn_Search").click()
        driver.find_element_by_id("ibtAddMsg").click()
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(1)
        #回到原窗口
        driver.switch_to_window(nowhandle)
        time.sleep(1)
        #定位到公文签批查询字段的所属框架
        driver.switch_to_frame("diaConIf")

        #点击查询按钮
        driver.find_element_by_id("IB_search").click()
        time.sleep(1)
        
        #查询结果判断---------------------------------------------------------------------------------------------
        #公文类型字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[2]").text
            self.assertEqual(text,u'外出开会申请单')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型是外出开会申请单' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型不是外出开会申请单'
        #标题字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]").text
            self.assertEqual(text, self.sub_text)
            print u'公文签批的结果列表里存在，标题“'+self.sub_text+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里不存在，标题“'+self.sub_text+u'”'
        #签批状态字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            self.assertEqual(text, u'签批')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的签批状态是签批' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的签批状态不是签批'
        #发送人字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
            self.assertEqual(text, self.sub_text3)
            print u'公文签批的结果列表里的发送人“'+text+'"与呈报时的人员"'+self.sub_text3+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里的发送人“'+text+'"与呈报时的人员"'+self.sub_text3+'"不一致"'+u'”'
        time.sleep(1)

        #查询结果中，点击标题链接，打开公文详情--------------------------------------------------------------------------
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()

        #公文详情中，检查字段信息----------------------------------------------------------------------------------------
        #获取所有窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])     
        #定位到所属框架
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.switch_to_frame("dFrame")

        #公文详情中的字段值判断-------------------------------------------------------------------------------------------
        #判断标题字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[1]/td/span").text
            self.assertEqual(text, self.sub_text)
            print u'标题字段值“'+text+'"与呈报时的值"'+self.sub_text+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'标题字段值“'+text+'"与呈报时的值"'+self.sub_text+'"不一致"'+u'”' 
        #判断申请单号字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[1]/td[2]").text
            self.assertEqual(text, self.sub_text5)
            print u'申请单号字段值“'+text+'"与呈报时的值"'+self.sub_text5+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请单号字段值“'+text+'"与呈报时的值"'+self.sub_text5+'"不一致"'+u'”'
        #判断参会人员字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='ctrMember']/p").text
            self.assertEqual(text, self.sub_text18)
            print u'申请单号字段值“'+text+'"与呈报时的值"'+self.sub_text18+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请单号字段值“'+text+'"与呈报时的值"'+self.sub_text18+'"不一致"'+u'”'
        #判断所属科室字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='SelectOnlyAccount_txbText']").text
            self.assertEqual(text, self.sub_text14)
            print u'所属科室字段值“'+text+'"与呈报时的值"'+self.sub_text14+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'所属科室字段值“'+text+'"与呈报时的值"'+self.sub_text14+'"不一致"'+u'”' 
        #判断是否使用专项经费字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[4]/td[1]").text
            self.assertEqual(text, u'否')
            print u'是否使用专项经费字段值“'+text+u'”与呈报时的"否"一致' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'是否使用专项经费字段值“'+text+u'”与呈报时的"否"不一致'   
        #判断缓急字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[5]/td[1]/span").text
            self.assertEqual(text, self.sub_text10)
            print u'缓急字段值“'+text+'"与呈报时的值"'+self.sub_text10+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'缓急字段值“'+text+'"与呈报时的值"'+self.sub_text10+'"不一致"'+u'”'
        #判断密级字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[5]/td[2]/span").text
            self.assertEqual(text, self.sub_text11)
            print u'密级字段值“'+text+'"与呈报时的值"'+self.sub_text11+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'密级字段值“'+text+'"与呈报时的值"'+self.sub_text11+'"不一致"'+u'”'
        #判断参加会议(班)内容字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[7]/td/div").text
            self.assertEqual(text, self.sub_text17)
            print u'参加会议(班)内容字段值“'+text+'"与呈报时的值"'+self.sub_text17+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'参加会议(班)内容字段值“'+text+'"与呈报时的值"'+self.sub_text17+'"不一致"'+u'”'
        #判断正文附件字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='AttachmentDIV5']/a[2]").text
            self.assertEqual(text, self.sub_text12)
            print u'正文附件“'+text+'"与添加时的"'+self.sub_text12+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'正文附件“'+text+'"与添加时的"'+self.sub_text12+'"不一致"'+u'”' 
        time.sleep(1)
  
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
