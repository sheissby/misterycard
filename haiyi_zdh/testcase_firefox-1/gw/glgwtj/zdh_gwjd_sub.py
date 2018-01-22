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
class zdh_gwjd_sub(unittest.TestCase):
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
        self.sub_text='gwjd_sub'+now
        #定义公文收件人、申请人、经办人、经办人电话、接待事由
        self.sub_text2=u'符晓玲'
        self.sub_text3=u'冯学冠'
        self.sub_text4=u'黄植'
        self.sub_text5=u'13398991935'
        self.sub_text6=u'游览假日海滩'
        #定义接待对象情况（单位、接待人数、联系人、联系电话、主要人员、预计到达时间、预计离开时间）、接待预算
        self.sub_text7=u'中国地震局'
        self.sub_text8=u'10'
        self.sub_text9=u'李四'
        self.sub_text10=u'13398991934'
        self.sub_text11=u'王五、马六'
        self.sub_text12=u'2000'
        
        #显示用例名称
        print u'---------------《公务接待(标准)审批表 提交功能自动化测试》----------------------'
        
    def test_zdh_gwjd_sub(self):
        
        #打开公文管理-公文呈报-公务接待(标准)审批表 -------------------------------------------------------------------
        #打开浏览器
        driver = self.driver
        #定位且鼠标移到公文管理模块
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        #点击公文呈报导航链接，设置思考时间
        driver.find_element_by_xpath(".//*[@id='nav-c0baf144-2241-471a-8947-db8511046075']/a").click()
        time.sleep(1)
        #定位到公务接待(标准)审批表 的所属框架
        driver.switch_to_frame("diaConIf")  
        #点击公务接待(标准)审批表 链接
        driver.find_element_by_xpath("html/body/div[2]/div/table[4]/tbody/tr/td[2]/div/ul/li/table/tbody/tr/td[1]/a").click()
        time.sleep(1)   

        #配置字段属性，点击提交-------------------------------------------------------------------------------
        #获取呈报页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)
        
        #输入标题、经办人电话、接待事由+++++++++++++++++++++++++
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").clear()
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").send_keys(self.sub_text)        
        driver.find_element_by_id("266e2146-36c2-4f45-b10c-f5799633e83d").send_keys(self.sub_text5)
        driver.find_element_by_id("274c9e3e-6050-491f-90dc-8e9c9d11e3bb").send_keys(self.sub_text6)
        #输入接待对象情况（单位、接待人数、联系人、联系电话、主要人员）、接待预算+++++++++
        driver.find_element_by_id("b188e962-08c6-4634-baa4-bf0f30ac6d58").send_keys(self.sub_text7)        
        driver.find_element_by_id("d6ae0bea-bf4b-4a04-b943-ae4981e51516").send_keys(self.sub_text8)
        driver.find_element_by_id("0d092758-582e-41b9-a0ad-42667b6124a5").send_keys(self.sub_text9)
        driver.find_element_by_id("e6f77541-82fa-4028-9790-5085da9a5201").send_keys(self.sub_text10)        
        driver.find_element_by_id("340c5bcf-922e-458a-bd3a-5ed30cb73c1f").send_keys(self.sub_text11)
        driver.find_element_by_id("ea943206-faa4-4533-932b-7be832df54f4").send_keys(self.sub_text12)
        #输入接待对象情况（预计到达时间、预计离开时间）
        js="$(\"input[id='c8698db9-676e-4795-a562-ad92d4a50e5d']\").removeAttr('readonly');$(\"input[id='c8698db9-676e-4795-a562-ad92d4a50e5d']\").attr('value','2016-08-25 16:38:34')"
        driver.execute_script(js)
        js="$(\"input[id='33193633-a61f-4daf-bb1e-6c8b5ff11fd1']\").removeAttr('readonly');$(\"input[id='33193633-a61f-4daf-bb1e-6c8b5ff11fd1']\").attr('value','2016-08-30 16:38:34')"
        driver.execute_script(js)

        #经办人选择+++++++++++++++++++++++++++++++++++++
        #点击经办人选择按钮
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[3]/td[1]/img").click()
        #定位到人员选择页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        time.sleep(1)
        #定位到人员选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询人员
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text4)
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
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[13]/td/img").click()
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
        #获取单据编号、申请科室、申请时间、预计到达时间、预计离开时间、缓急、密级、正文附件的字段值
        self.sub_text13=driver.find_element_by_id("8f66d953-e068-49a9-833e-943f102828c2").get_attribute('value')
        self.sub_text14=driver.find_element_by_id("SelectOnlyAccount_txbText8").get_attribute('value')
        self.sub_text15=driver.find_element_by_id("d7e20886-6fde-4080-9a17-4506b2bc267c").get_attribute('value')
        self.sub_text16=driver.find_element_by_id("c8698db9-676e-4795-a562-ad92d4a50e5d").get_attribute('value')
        self.sub_text17=driver.find_element_by_id("33193633-a61f-4daf-bb1e-6c8b5ff11fd1").get_attribute('value')
        self.sub_text18=driver.find_element_by_id("080105").get_attribute('value')
        self.sub_text19=driver.find_element_by_id("080102").get_attribute('value')
        self.sub_text20=driver.find_element_by_xpath(".//*[@id='tbFilePost_labFilesLink']/ul/li/a[1]").text
        #将缓急、密级字段的值左边的1|去掉（取从左边数2位后的内容）
        self.sub_text21=self.sub_text18[2:]
        self.sub_text22=self.sub_text19[2:]
        
        #点击提交按钮
        driver.find_element_by_id("bt_Submit").click()
        time.sleep(4)
        print u'可正常提交公文'
        
        #关闭页面，使用符晓玲（200518）登录-----------------------------------------------------------------
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
        ddlType.find_element_by_xpath("//option[@value='100405']").click()
        ddlDetailType=driver.find_element_by_id('ddlDetailType')
        ddlDetailType.find_element_by_xpath("//option[@value='tb175']").click()
        
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
            self.assertEqual(text,u'公务接待(标准)审批表')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型是“公务接待(标准)审批表”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型不是“公务接待(标准)审批表”'
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
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[2]/td[1]/span").text
            self.assertEqual(text, self.sub_text)
            print u'标题字段值“'+text+'"与呈报时的值"'+self.sub_text+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'标题字段值“'+text+'"与呈报时的值"'+self.sub_text+'"不一致"'+u'”' 
        #判断单据编号字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[2]/td[2]").text
            self.assertEqual(text, self.sub_text13)
            print u'单据编号字段值“'+text+'"与呈报时的值"'+self.sub_text13+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'单据编号字段值“'+text+'"与呈报时的值"'+self.sub_text13+'"不一致"'+u'”' 
        #判断接待事由字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[3]/td").text
            self.assertEqual(text, self.sub_text6)
            print u'接待事由字段值“'+text+'"与呈报时的值"'+self.sub_text6+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'接待事由字段值“'+text+'"与呈报时的值"'+self.sub_text6+'"不一致"'+u'”' 
        #判断申请人字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[4]/td[1]").text
            self.assertEqual(text, self.sub_text3)
            print u'申请人字段值“'+text+'"与呈报时的值"'+self.sub_text3+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请人字段值“'+text+'"与呈报时的值"'+self.sub_text3+'"不一致"'+u'”'
        #判断申请科室字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[4]/td[2]").text
            self.assertEqual(text, self.sub_text14)
            print u'申请科室字段值“'+text+'"与呈报时的值"'+self.sub_text14+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请科室字段值“'+text+'"与呈报时的值"'+self.sub_text14+'"不一致"'+u'”' 
        #判断申请时间字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[4]/td[3]").text
            self.assertEqual(text, self.sub_text15)
            print u'申请时间字段值“'+text+'"与呈报时的值"'+self.sub_text15+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请时间字段值“'+text+'"与呈报时的值"'+self.sub_text15+'"不一致"'+u'”' 
        #判断经办人字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[5]/td[1]").text
            self.assertEqual(text, self.sub_text4)
            print u'经办人字段值“'+text+'"与呈报时的值"'+self.sub_text4+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'经办人字段值“'+text+'"与呈报时的值"'+self.sub_text4+'"不一致"'+u'”' 
        #判断经办人电话字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[5]/td[2]").text
            self.assertEqual(text, self.sub_text5)
            print u'经办人电话字段值“'+text+'"与呈报时的值"'+self.sub_text5+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'经办人电话字段值“'+text+'"与呈报时的值"'+self.sub_text5+'"不一致"'+u'”' 
        #判断单位字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[6]/td[1]").text
            text1=text[3:]
            self.assertEqual(text1, self.sub_text7)
            print u'经办人电话字段值“'+text1+'"与呈报时的值"'+self.sub_text7+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'经办人电话字段值“'+text1+'"与呈报时的值"'+self.sub_text7+'"不一致"'+u'”' 
        #判断接待人数字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[6]/td[2]").text
            text1=text[0:2]
            self.assertEqual(text1, self.sub_text8)
            print u'接待人数字段值“'+text1+'"与呈报时的值"'+self.sub_text8+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'接待人数字段值“'+text1+'"与呈报时的值"'+self.sub_text8+'"不一致"'+u'”'
        #判断联系人字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[7]/td[1]").text
            self.assertEqual(text, self.sub_text9)
            print u'联系人字段值“'+text+'"与呈报时的值"'+self.sub_text9+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'联系人字段值“'+text+'"与呈报时的值"'+self.sub_text9+'"不一致"'+u'”'
        #判断联系人电话字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[7]/td[2]").text
            self.assertEqual(text, self.sub_text10)
            print u'联系人电话字段值“'+text+'"与呈报时的值"'+self.sub_text10+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'联系人电话字段值“'+text+'"与呈报时的值"'+self.sub_text10+'"不一致"'+u'”'
        #判断主要人员字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[8]/td[1]").text
            text1=text[5:]
            self.assertEqual(text1, self.sub_text11)
            print u'主要人员字段值“'+text1+'"与呈报时的值"'+self.sub_text11+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'主要人员字段值“'+text1+'"与呈报时的值"'+self.sub_text11+'"不一致"'+u'”'
        #判断预计到达时间字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[8]/td[2]").text
            self.assertEqual(text, self.sub_text16)
            print u'预计到达时间字段值“'+text+'"与呈报时的值"'+self.sub_text16+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'预计到达时间字段值“'+text+'"与呈报时的值"'+self.sub_text16+'"不一致"'+u'”'
        #判断预计离开时间字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[8]/td[3]").text
            self.assertEqual(text, self.sub_text17)
            print u'预计离开时间字段值“'+text+'"与呈报时的值"'+self.sub_text17+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'预计离开时间字段值“'+text+'"与呈报时的值"'+self.sub_text17+'"不一致"'+u'”'
        #判断接待预算字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[12]/td").text
            text1=text[0:4]
            self.assertEqual(text1, self.sub_text12)
            print u'器械名称字段值“'+text1+'"与呈报时的值"'+self.sub_text12+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'器械名称字段值“'+text1+'"与呈报时的值"'+self.sub_text12+'"不一致"'+u'”' 
        #判断缓急字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[14]/td[1]/span").text
            self.assertEqual(text, self.sub_text21)
            print u'缓急字段值“'+text+'"与呈报时的值"'+self.sub_text21+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'缓急字段值“'+text+'"与呈报时的值"'+self.sub_text21+'"不一致"'+u'”'
        #判断密级字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[14]/td[2]/span").text
            self.assertEqual(text, self.sub_text22)
            print u'密级字段值“'+text+'"与呈报时的值"'+self.sub_text22+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'密级字段值“'+text+'"与呈报时的值"'+self.sub_text22+'"不一致"'+u'”'
        #判断正文附件字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='AttachmentDIV5']/a[2]").text
            self.assertEqual(text, self.sub_text20)
            print u'正文附件“'+text+'"与添加时的"'+self.sub_text20+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'正文附件“'+text+'"与添加时的"'+self.sub_text20+'"不一致"'+u'”' 
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
