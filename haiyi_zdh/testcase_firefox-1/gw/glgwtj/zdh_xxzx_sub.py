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
#调用登录
from haiyi_zdh.public.firefox import login
#调用关闭Plugin Container 冲突窗口
import closewindow

#案例
class zdh_xxzx_sub(unittest.TestCase):
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
        self.sub_text='xxzx_sub'+now
        #定义公文收件人、填报人、填报人电话、楼层房号
        self.sub_text2=u'符晓玲'
        self.sub_text3=u'冯学冠'
        self.sub_text4=u'13398991939'
        self.sub_text13=u'2001'
        self.sub_text14=u'无法打开显示器'
        self.sub_text15=u'黄植'
        #显示用例名称
        print u'---------------《信息中心维修单 提交功能自动化测试》----------------------'
        
    def test_zdh_xxzx_sub(self):
        
        #打开公文管理-公文呈报-信息中心维修单 -------------------------------------------------------------------
        #打开浏览器
        driver = self.driver
        #定位且鼠标移到公文管理模块
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        #点击公文呈报导航链接，设置思考时间
        driver.find_element_by_xpath(".//*[@id='nav-c0baf144-2241-471a-8947-db8511046075']/a").click()
        time.sleep(1)
        #定位到信息中心维修单 的所属框架
        driver.switch_to_frame("diaConIf")  
        #点击信息中心维修单 链接
        driver.find_element_by_xpath("html/body/div[2]/div/table[2]/tbody/tr/td[2]/div/ul/li/table/tbody/tr/td[3]/a").click()
        time.sleep(1)   

        #配置字段属性，点击提交-------------------------------------------------------------------------------
        #获取呈报页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)
        
        #输入标题、填报人电话、楼层房号、报修类别(电脑、打印机)、问题描述+++++++++++++++++++++++++
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").clear()
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").send_keys(self.sub_text)        
        driver.find_element_by_id("a940e23e-0671-49a6-9a2b-3b4e2321e066").clear()
        driver.find_element_by_id("a940e23e-0671-49a6-9a2b-3b4e2321e066").send_keys(self.sub_text4)
        driver.find_element_by_id("6fe07469-ea19-4cc8-b2da-5fbf4666ff0c").send_keys(self.sub_text13)
        driver.find_element_by_xpath("html/body/form/div/div[2]/table/tbody/tr[5]/td/input[1]").click()
        driver.find_element_by_xpath("html/body/form/div/div[2]/table/tbody/tr[5]/td/input[2]").click()
        driver.find_element_by_id("274c9e3e-6050-491f-90dc-8e9c9d11e3bb").send_keys(self.sub_text14)

        #科室负责人选择+++++++++++++++++++++++++++++++++++++
        #点击科室负责人选择按钮
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[2]/td[2]/img").click()
        #定位到人员选择页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        time.sleep(1)
        #定位到人员选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询人员
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text15)
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
        
        #收件人选择+++++++++++++++++++++++++++++++++++++
        #点击收件人选择按钮
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[7]/td/img").click()
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
        
        #获取字段值++++++++++++++++++++++++++++++++++++++++
        #获取部门/科室、申请时间、维修单号、缓急、密级、正文附件、报修类别（字段1、字段2）的字段值
        self.sub_text5=driver.find_element_by_id("SelectOnlyAccount_txbText8").get_attribute('value')
        self.sub_text6=driver.find_element_by_id("9b3a75b7-af4c-4814-aed6-019414aeb3bf").get_attribute('value')
        self.sub_text7=driver.find_element_by_id("19842358-8a51-4c2f-a676-8351d21c24e2").get_attribute('value')
        self.sub_text8=driver.find_element_by_id("080105").get_attribute('value')
        self.sub_text9=driver.find_element_by_id("080102").get_attribute('value')
        self.sub_text12=driver.find_element_by_xpath(".//*[@id='tbFilePost_labFilesLink']/ul/li/a[1]").text
        self.sub_text16=driver.find_element_by_xpath("html/body/form/div/div[2]/table/tbody/tr[5]/td/label[1]").text
        self.sub_text17=driver.find_element_by_xpath("html/body/form/div/div[2]/table/tbody/tr[5]/td/label[2]").text
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
        ddlType.find_element_by_xpath("//option[@value='100403']").click()
        ddlDetailType=driver.find_element_by_id('ddlDetailType')
        ddlDetailType.find_element_by_xpath("//option[@value='tb170']").click()
        
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
            self.assertEqual(text,u'信息中心维修单')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型是“信息中心维修单”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型不是“信息中心维修单”'
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
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[1]/td[1]/span").text
            self.assertEqual(text, self.sub_text)
            print u'标题字段值“'+text+'"与呈报时的值"'+self.sub_text+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'标题字段值“'+text+'"与呈报时的值"'+self.sub_text+'"不一致"'+u'”' 
        #判断维修单号字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[1]/td[2]").text
            self.assertEqual(text, self.sub_text7)
            print u'事项编号字段值“'+text+'"与呈报时的值"'+self.sub_text7+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'事项编号字段值“'+text+'"与呈报时的值"'+self.sub_text7+'"不一致"'+u'”' 
        #判断部门/科室字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='SelectOnlyAccount_txbText']").text
            self.assertEqual(text, self.sub_text5)
            print u'部门/科室字段值“'+text+'"与呈报时的值"'+self.sub_text5+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'部门/科室字段值“'+text+'"与呈报时的值"'+self.sub_text5+'"不一致"'+u'”' 
        #判断科室负责人字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[2]/td[2]").text
            self.assertEqual(text, self.sub_text15)
            print u'科室负责人字段值“'+text+'"与呈报时的值"'+self.sub_text15+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'科室负责人字段值“'+text+'"与呈报时的值"'+self.sub_text15+'"不一致"'+u'”'
        #判断填报人字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[3]/td[1]").text
            self.assertEqual(text, self.sub_text3)
            print u'填报人字段值“'+text+'"与呈报时的值"'+self.sub_text3+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'填报人字段值“'+text+'"与呈报时的值"'+self.sub_text3+'"不一致"'+u'”'
        #判断填报人电话字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[3]/td[2]").text
            self.assertEqual(text, self.sub_text4)
            print u'填报人电话字段值“'+text+'"与呈报时的值"'+self.sub_text4+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'填报人电话字段值“'+text+'"与呈报时的值"'+self.sub_text4+'"不一致"'+u'”'
        #判断楼层房号字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[4]/td[1]").text
            self.assertEqual(text, self.sub_text13)
            print u'楼层房号字段值“'+text+'"与呈报时的值"'+self.sub_text13+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'楼层房号字段值“'+text+'"与呈报时的值"'+self.sub_text13+'"不一致"'+u'”'
        #判断申请时间字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='9b3a75b7-af4c-4814-aed6-019414aeb3bf']").text
            self.assertEqual(text, self.sub_text6)
            print u'申请时间字段值“'+text+'"与呈报时的值"'+self.sub_text6+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请时间字段值“'+text+'"与呈报时的值"'+self.sub_text6+'"不一致"'+u'”'  
        #判断报修类别的字段1是否被选中
        try:
            driver.find_element_by_xpath("html/body/div[2]/div/table/tbody/tr[5]/td/input[1]").is_selected()
            print u'报修类别字段1“'+self.sub_text16+'"已勾选'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'报修类别字段1“'+self.sub_text16+'"未勾选'
        #判断报修类别的字段2是否被选中
        try:
            text=driver.find_element_by_xpath("html/body/div[2]/div/table/tbody/tr[5]/td/input[2]").is_selected()
            print u'报修类别字段2“'+self.sub_text17+'"已勾选'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'报修类别字段2“'+self.sub_text17+'"未勾选' 
        #判断缓急字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[6]/td[1]/span").text
            self.assertEqual(text, self.sub_text10)
            print u'缓急字段值“'+text+'"与呈报时的值"'+self.sub_text10+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'缓急字段值“'+text+'"与呈报时的值"'+self.sub_text10+'"不一致"'+u'”'
        #判断密级字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[6]/td[2]/span").text
            self.assertEqual(text, self.sub_text11)
            print u'密级字段值“'+text+'"与呈报时的值"'+self.sub_text11+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'密级字段值“'+text+'"与呈报时的值"'+self.sub_text11+'"不一致"'+u'”'
        #判断问题描述字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[7]/td/div").text
            self.assertEqual(text, self.sub_text14)
            print u'问题描述字段值“'+text+'"与呈报时的值"'+self.sub_text14+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'问题描述字段值“'+text+'"与呈报时的值"'+self.sub_text14+'"不一致"'+u'”'
        #判断正文附件字段
        try:
            text=driver.find_element_by_xpath("html/body/div[2]/div/table/tbody/tr[8]/td/div/a[2]").text
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
