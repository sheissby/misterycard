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
from haiyi_zdh.public.ie import login
#调用关闭Plugin Container 冲突窗口
import closewindow

#案例
class zdh_sjcg_sub(unittest.TestCase):
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
        self.sub_text='sjcg_sub'+now
        #定义公文收件人、申请人、试剂名称、每人份(例)、月检查量(估)、收费标准、年收入
        self.sub_text2=u'符晓玲'
        self.sub_text3=u'冯学冠'
        self.sub_text4=u'针管'
        self.sub_text5=u'1'
        self.sub_text6=u'100'
        self.sub_text7=u'60'
        self.sub_text8=u'200'
     
        #显示用例名称
        print u'---------------《试剂采购申请单 提交功能自动化测试》----------------------'
        
    def test_zdh_sjcg_sub(self):
        
        #打开公文管理-公文呈报-试剂采购申请单 -------------------------------------------------------------------
        #打开浏览器
        driver = self.driver
        #赋窗口空值，获取当前窗口
        allhandlelist=[]
        nowhandle=driver.current_window_handle
        allhandlelist.append(nowhandle)
        #打开公文管理模块
        driver.find_element_by_id("nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd").click()
        time.sleep(1)
        #点击公文呈报导航链接，设置思考时间
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[1]/a").click()
        time.sleep(1)
        
        #定位呈批单的iframe框架+++++++++++++++++++++++++++
        #找div class="mainRight"
        frame=driver.find_element_by_css_selector('.mainRight')
        #遍历下方的iframe
        frames=frame.find_elements_by_tag_name('iframe')
        #取第1个iframe
        driver.switch_to_frame(frames[0]) 
        #点击试剂采购申请单 链接
        driver.find_element_by_xpath("html/body/div[2]/div/table[3]/tbody/tr/td[2]/div/ul/li/table/tbody/tr/td[3]/a").click()
        time.sleep(1)   

        #配置字段属性，点击提交-------------------------------------------------------------------------------
        #获取呈报页面窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")
        
        #输入标题、试剂名称、每人份(例)、月检查量(估)、收费标准、年收入+++++++++++++++++++++++++
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").clear()
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").send_keys(self.sub_text)        
        driver.find_element_by_id("f7bf3c4c-0939-4a0b-affd-8ace3f81b0e1").send_keys(self.sub_text4)
        driver.find_element_by_id("bba87653-800b-44bd-9d30-06bdae1730a7").send_keys(self.sub_text5)
        driver.find_element_by_id("db8747e6-2b30-4bcc-b696-95aa990d54b1").send_keys(self.sub_text6)
        driver.find_element_by_id("141ade7f-74ef-4cb1-9416-3c992d09cbcf").send_keys(self.sub_text7)
        driver.find_element_by_id("fa42b758-1aca-41c4-acc9-69460599f452").send_keys(self.sub_text8)
        time.sleep(1)
    
        #收件人选择+++++++++++++++++++++++++++++++++++++
        #双击收件人选择按钮
        double=driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[17]/td/img")
        ActionChains(driver).double_click(double).perform()   
        time.sleep(1) 
        #获取页面的上层和本层窗口
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))#与上层窗口作比较
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        #定位到人员选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询人员
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text2)
        #点击查询、双击添加、单击提交人员
        driver.find_element_by_id("btn_Search").click()
        time.sleep(1)
        double=driver.find_element_by_id("ibtAddMsg")
        ActionChains(driver).double_click(double).perform() 
        time.sleep(1) 
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(1)
        #删除之前已关闭消失的窗口句柄
        allhandlelist.pop()
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")

        #附件选择++++++++++++++++++++++++++++++++++++++++
        #定位到要双击的附件元素，并执行双击
        double2=driver.find_element_by_id("tbFilePost_FileUpload")
        ActionChains(driver).double_click(double2).perform()
        time.sleep(1)       
        #获取附件操作的本层窗口
        driver.switch_to_window(allhandlelist[0])       
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
        driver.find_element_by_id("tbFilePost_uploadify").click()
        time.sleep(1)
        #调用auto工具保存的附件上传word文件
        os.startfile(os.getcwd().split('testcase_ie')[0]+'\uploadfile\Ie_gw_doc.exe')
        time.sleep(4)
        #点击添加
        driver.find_element_by_id("tbFilePost_OK").click()
        time.sleep(1)  
        #获取呈报页面窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")
        
        #获取字段值++++++++++++++++++++++++++++++++++++++++
        #获取单据编号、申请科室、申请时间、缓急、密级、正文附件的字段值
        self.sub_text9=driver.find_element_by_id("33c1a495-9648-4ead-a516-3120628be29f").get_attribute('value')
        self.sub_text10=driver.find_element_by_id("SelectOnlyAccount_txbText8").get_attribute('value')
        self.sub_text11=driver.find_element_by_id("63276f89-408e-41db-b0e9-3780336533d3").get_attribute('value')
        self.sub_text12=driver.find_element_by_id("080105").get_attribute('value')
        self.sub_text13=driver.find_element_by_id("080102").get_attribute('value')
        self.sub_text14=driver.find_element_by_xpath(".//*[@id='tbFilePost_labFilesLink']/ul/li/a[1]").text
        #将缓急、密级字段的值左边的1|去掉（取从左边数2位后的内容）
        self.sub_text15=self.sub_text12[2:]
        self.sub_text16=self.sub_text13[2:]
        
        #点击提交按钮
        driver.find_element_by_id("bt_Submit").click()
        time.sleep(4)
        print u'可正常提交公文'
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
                                
##        #杀掉火狐对插件不兼容的提示+++++++++++++++++++++++++++++++++++++++++++++++
##        closewindow.close_window('Plugin Container for Firefox')
##        time.sleep(1)
        
        #关闭页面，使用符晓玲（200518）登录-----------------------------------------------------------------
        #关闭页面
        driver.quit()
        #删除之前已关闭消失的窗口句柄
        allhandlelist.pop()
        #调用登录函数
        login.login_normal2(self)
        
        #打开公文管理-公文签批------------------------------------------------------------------------------------------
        #重新打开浏览器
        driver = self.driver
        nowhandle=driver.current_window_handle
        allhandlelist.append(nowhandle)
        #打开公文管理模块
        driver.find_element_by_id("nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd").click()
        time.sleep(1)
        #点击公文签批导航链接
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[2]/a").click()
        time.sleep(1)

        #输入字段，进行查询---------------------------------------------------------------------------------------------
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #定位到公文签批查询字段的所属框架
        driver.switch_to_frame("diaConIf")
        
        #输入标题、接文时间
        driver.find_element_by_id("ctrTitle").send_keys(self.sub_text)
        driver.find_element_by_id("ctrStartDate").send_keys(u'2016-01-01')
        driver.find_element_by_id("ctrEndDate").send_keys(u'12-31')
        
        #定位和选择公文类型的下拉框
        ddlType=driver.find_element_by_id('ddlType')
        ddlType.find_element_by_xpath("//option[@value='100404']").click()
        time.sleep(1)
        ddlDetailType=driver.find_element_by_id('ddlDetailType')
        ddlDetailType.find_element_by_xpath("//option[@value='tb173']").click()
        time.sleep(1)
        
        #发送人选择+++++++++++++++++++++++++++++++++++++++
        #单击选择按钮
        driver.find_element_by_xpath(".//*[@id='ctrUser_imgBt']").click()
        time.sleep(1)    
        #获取页面的上层和本层窗口
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))#与上层窗口作比较
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        #定位到人员选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询人员
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text3)
        #点击查询、双击添加、单击提交人员
        driver.find_element_by_id("btn_Search").click()
        time.sleep(1)
        double=driver.find_element_by_id("ibtAddMsg")
        ActionChains(driver).double_click(double).perform() 
        time.sleep(1)
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(1)
        #删除之前已关闭消失的窗口句柄
        allhandlelist.pop()
        #获取列表的窗口
        driver.switch_to_window(allhandlelist[0])
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
            self.assertEqual(text,u'试剂采购申请单')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型是“试剂采购申请单”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型不是“试剂采购申请单”'
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
        time.sleep(1)

        #公文详情中，检查字段信息----------------------------------------------------------------------------------------
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)      
        #定位到所属框架
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        driver.switch_to_frame("dFrame")

        #公文详情中的字段值判断-------------------------------------------------------------------------------------------
        #判断标题字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[1]/td[1]/span").text
            self.assertEqual(text, self.sub_text)
            print u'标题字段值“'+text+'"与呈报时的值"'+self.sub_text+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'标题字段值“'+text+'"与呈报时的值"'+self.sub_text+'"不一致"'+u'”' 
        #判断单据编号字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[1]/td[2]").text
            self.assertEqual(text, self.sub_text9)
            print u'单据编号字段值“'+text+'"与呈报时的值"'+self.sub_text9+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'单据编号字段值“'+text+'"与呈报时的值"'+self.sub_text9+'"不一致"'+u'”' 
        #判断申请人字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[2]/td[1]").text
            self.assertEqual(text, self.sub_text3)
            print u'申请人字段值“'+text+'"与呈报时的值"'+self.sub_text3+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请人字段值“'+text+'"与呈报时的值"'+self.sub_text3+'"不一致"'+u'”'
        #判断申请科室字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[2]/td[2]").text
            self.assertEqual(text, self.sub_text10)
            print u'申请科室字段值“'+text+'"与呈报时的值"'+self.sub_text10+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请科室字段值“'+text+'"与呈报时的值"'+self.sub_text10+'"不一致"'+u'”' 
        #判断申请时间字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[2]/td[3]").text
            self.assertEqual(text, self.sub_text11)
            print u'申请时间字段值“'+text+'"与呈报时的值"'+self.sub_text11+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请时间字段值“'+text+'"与呈报时的值"'+self.sub_text11+'"不一致"'+u'”'   
        #判断试剂名称字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[3]/td").text
            self.assertEqual(text, self.sub_text4)
            print u'试剂名称字段值“'+text+'"与呈报时的值"'+self.sub_text4+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'试剂名称字段值“'+text+'"与呈报时的值"'+self.sub_text4+'"不一致"'+u'”' 
        #判断每人份(例)字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[15]/td[1]").text
            text1=text[0:1]
            self.assertEqual(text1,self.sub_text5)
            print u'每人份(例)字段值“'+text1+'"与呈报时的值"'+self.sub_text5+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'每人份(例)字段值“'+text1+'"与呈报时的值"'+self.sub_text5+'"不一致"'+u'”' 
        #判断月检查量(估)字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[15]/td[2]").text
            text1=text[0:3]
            self.assertEqual(text1, self.sub_text6)
            print u'月检查量(估)字段值“'+text1+'"与呈报时的值"'+self.sub_text6+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'月检查量(估)字段值“'+text1+'"与呈报时的值"'+self.sub_text6+'"不一致"'+u'”' 
        #判断收费标准字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[16]/td[1]").text
            text1=text[7:9]
            self.assertEqual(text1,self.sub_text7)
            print u'收费标准字段值“'+text1+'"与呈报时的值"'+self.sub_text7+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'收费标准字段值“'+text1+'"与呈报时的值"'+self.sub_text7+'"不一致"'+u'”' 
        #判断年收入字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[16]/td[2]").text
            text1=text[0:3]
            self.assertEqual(text1, self.sub_text8)
            print u'年收入字段值“'+text1+'"与呈报时的值"'+self.sub_text8+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'年收入字段值“'+text1+'"与呈报时的值"'+self.sub_text8+'"不一致"'+u'”' 
        #判断缓急字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[17]/td[1]/span").text
            self.assertEqual(text, self.sub_text15)
            print u'缓急字段值“'+text+'"与呈报时的值"'+self.sub_text15+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'缓急字段值“'+text+'"与呈报时的值"'+self.sub_text15+'"不一致"'+u'”'
        time.sleep(1)
        #判断密级字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[17]/td[2]/span").text
            self.assertEqual(text, self.sub_text16)
            print u'密级字段值“'+text+'"与呈报时的值"'+self.sub_text16+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'密级字段值“'+text+'"与呈报时的值"'+self.sub_text16+'"不一致"'+u'”'
        #判断正文附件字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='AttachmentDIV5']/a[2]").text
            self.assertEqual(text, self.sub_text14)
            print u'正文附件“'+text+'"与添加时的"'+self.sub_text14+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'正文附件“'+text+'"与添加时的"'+self.sub_text14+'"不一致"'+u'”' 
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
