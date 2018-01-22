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
class zdh_gwyc_sub(unittest.TestCase):
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
        self.sub_text='gwyc_sub'+now
        #定义公文收件人、申请人、申请人电话、用车人数、用车原因、办事地点、用车科室负责人
        self.sub_text2=u'符晓玲'
        self.sub_text3=u'冯学冠'
        self.sub_text4=u'13398991939'
        self.sub_text5=u'10'
        self.sub_text6=u'游览观光办事'
        self.sub_text7=u'大礼堂'
        self.sub_text8=u'黄植'  
        #显示用例名称
        print u'---------------《公务用车申请单 提交功能自动化测试》----------------------'
        
    def test_zdh_gwyc_sub(self):
        
        #打开公文管理-公文呈报-公务用车申请单 -------------------------------------------------------------------
        #打开浏览器
        driver = self.driver
        #定位且鼠标移到公文管理模块
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        #点击公文呈报导航链接，设置思考时间
        driver.find_element_by_xpath(".//*[@id='nav-c0baf144-2241-471a-8947-db8511046075']/a").click()
        time.sleep(1)
        #定位到公务用车申请单 的所属框架
        driver.switch_to_frame("diaConIf")  
        #点击公务用车申请单 链接
        driver.find_element_by_xpath("html/body/div[2]/div/table[4]/tbody/tr/td[2]/div/ul/li/table/tbody/tr/td[2]/a").click()
        time.sleep(1)   

        #配置字段属性，点击提交-------------------------------------------------------------------------------
        #获取呈报页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)
        
        #输入标题、申请人电话、用车人数、用车原因、办事地点、用车科室负责人+++++++++++++++++++++++++
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").clear()
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").send_keys(self.sub_text)
        driver.find_element_by_id("f7a223e1-2752-4ae3-85aa-e42d096d6bb4").clear()
        driver.find_element_by_id("f7a223e1-2752-4ae3-85aa-e42d096d6bb4").send_keys(self.sub_text4)
        driver.find_element_by_id("3b0fe25f-a592-4e31-959b-3e03cb5249e0").send_keys(self.sub_text5)
        driver.find_element_by_id("9b749865-643d-42ce-b3dc-54670f490a26").send_keys(self.sub_text6)        
        driver.find_element_by_id("c97fde5b-836f-4a50-b121-e878cbbbd5b4").send_keys(self.sub_text7)
        #勾选用车类型
        driver.find_element_by_name("101309b8-855a-46ae-ab3e-89914ffd60bc").click()

        #输入用车时长（开始时间、结束时间），且触发时长计算++++++++++++++++++++++++++++++++
        #开始时间选择
        #点击开始时间
        driver.find_element_by_id("c273307c-6481-45e3-9969-cbd4b66cebe3").click()
        #定位到iframe frameborder="0" 的div style的xpath路径
        frame=driver.find_element_by_xpath('/html/body/div[3]')
        #遍历下方的iframe取第1个
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        #单击今天按钮
        driver.find_element_by_id("dpTodayInput").click()
        time.sleep(1)
        #需重新获取框架
        driver.switch_to_window(allhandles[0])
        driver.switch_to_frame("_DialogFrame_0")

        #结束时间选择
        #点击结束时间
        driver.find_element_by_id("879bf094-2ffe-420b-9758-ce910c4bf3b5").click()
        #定位到iframe frameborder="0" 的div style的xpath路径
        frame=driver.find_element_by_xpath('/html/body/div[3]')
        #遍历下方的iframe取第1个
        frames=frame.find_elements_by_tag_name('iframe')
        driver.switch_to_frame(frames[0])
        #单击后退按钮
        driver.find_element_by_xpath(".//*[@id='dpTitle']/div[6]/a").click()
        time.sleep(1)
        #单击确定按钮
        driver.find_element_by_id("dpOkInput").click()
        time.sleep(1)
        #需重新获取框架
        driver.switch_to_window(allhandles[0])
        driver.switch_to_frame("_DialogFrame_0")
        
        #用车科室负责人选择+++++++++++++++++++++++++++++++++++++
        #点击用车科室负责人选择按钮
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[6]/td[2]/img").click()
        #定位到人员选择页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        time.sleep(1)
        #定位到人员选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询人员
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text8)
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
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[9]/td/img").click()
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
        time.sleep(1)

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
        #获取单据编号、申请部门、申请人电话、用车时长（开始时间、结束时间、总计）、缓急、密级、正文附件、用车类型（字段1）的字段值
        self.sub_text9=driver.find_element_by_id("5fed8dba-8fc3-4d23-8e91-839c2811f076").get_attribute('value')
        self.sub_text10=driver.find_element_by_id("SelectOnlyAccount_txbText9").get_attribute('value')
        self.sub_text11=driver.find_element_by_id("f7a223e1-2752-4ae3-85aa-e42d096d6bb4").get_attribute('value')
        self.sub_text12=driver.find_element_by_id("c273307c-6481-45e3-9969-cbd4b66cebe3").get_attribute('value')
        self.sub_text13=driver.find_element_by_id("879bf094-2ffe-420b-9758-ce910c4bf3b5").get_attribute('value')
        self.sub_text14=driver.find_element_by_id("b1bad614-9877-4a2e-ad97-e6ad142c687c").get_attribute('value')
        self.sub_text15=driver.find_element_by_id("080105").get_attribute('value')
        self.sub_text16=driver.find_element_by_id("080102").get_attribute('value')
        self.sub_text17=driver.find_element_by_xpath(".//*[@id='tbFilePost_labFilesLink']/ul/li/a[1]").text
        self.sub_text18=driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[3]/td[1]/label[1]").text
        #将缓急、密级字段的值左边的1|去掉（取从左边数2位后的内容）
        self.sub_text19=self.sub_text15[2:]
        self.sub_text20=self.sub_text16[2:]
        
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
        ddlDetailType.find_element_by_xpath("//option[@value='tb176']").click()
        
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
            self.assertEqual(text,u'公务用车申请单')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型是“公务用车申请单”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型不是“公务用车申请单”'
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
        #判断申请部门字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[2]/td[2]").text
            self.assertEqual(text, self.sub_text10)
            print u'申请部门字段值“'+text+'"与呈报时的值"'+self.sub_text10+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请部门字段值“'+text+'"与呈报时的值"'+self.sub_text10+'"不一致"'+u'”' 
        #判断申请人电话字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[2]/td[3]").text
            self.assertEqual(text, self.sub_text11)
            print u'申请人电话字段值“'+text+'"与呈报时的值"'+self.sub_text11+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'申请人电话字段值“'+text+'"与呈报时的值"'+self.sub_text11+'"不一致"'+u'”' 
        #判断用车类型的字段1是否被选中
        try:
            driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[3]/td[1]/input[1]").is_selected()
            print u'用车类型字段1"'+self.sub_text18+'"已勾选'
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'用车类型字段1"'+self.sub_text18+'"未勾选'       
        #判断用车人数字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[3]/td[2]").text
            text1=text[0:2]
            self.assertEqual(text1, self.sub_text5)
            print u'用车人数字段值“'+text1+'"与呈报时的值"'+self.sub_text5+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'用车人数字段值“'+text1+'"与呈报时的值"'+self.sub_text5+'"不一致"'+u'”' 
        #判断用车开始时间、结束时间字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[4]/td/span[1]").text
            text1=text[1:]
            self.assertEqual(text1, self.sub_text12+'到'+self.sub_text13)
            print u'用车开始时间、结束时间字段值“'+text1+'"与呈报时的值"'+self.sub_text12+'到'+self.sub_text13+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'用车开始时间、结束时间字段值“'+text1+'"与呈报时的值"'+self.sub_text12+'到'+self.sub_text13+'"不一致"'+u'”' 
        #判断用车时长字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[4]/td/span[2]").text
            text1=text[1:]
            self.assertEqual(text1, self.sub_text14)
            print u'用车时长字段值“'+text1+'"与呈报时的值"'+self.sub_text14+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'用车时长字段值“'+text1+'"与呈报时的值"'+self.sub_text14+'"不一致"'+u'”' 
        #判断用车原因字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[5]/td").text
            text1=text[1:]
            self.assertEqual(text1, self.sub_text6)
            print u'用车原因字段值“'+text1+'"与呈报时的值"'+self.sub_text6+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'用车原因字段值“'+text1+'"与呈报时的值"'+self.sub_text6+'"不一致"'+u'”'
        #判断办事地点字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[6]/td[1]").text
            self.assertEqual(text, self.sub_text7)
            print u'办事地点字段值“'+text+'"与呈报时的值"'+self.sub_text7+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'办事地点字段值“'+text+'"与呈报时的值"'+self.sub_text7+'"不一致"'+u'”' 
        #判断用车科室负责人字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[6]/td[2]").text
            self.assertEqual(text, self.sub_text8)
            print u'用车科室负责人字段值“'+text+'"与呈报时的值"'+self.sub_text8+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'用车科室负责人字段值“'+text+'"与呈报时的值"'+self.sub_text8+'"不一致"'+u'”'                             
        #判断缓急字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[8]/td[1]/span").text
            self.assertEqual(text, self.sub_text19)
            print u'缓急字段值“'+text+'"与呈报时的值"'+self.sub_text19+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'缓急字段值“'+text+'"与呈报时的值"'+self.sub_text19+'"不一致"'+u'”'
        #判断密级字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='Content']/table/tbody/tr[8]/td[2]/span").text
            self.assertEqual(text, self.sub_text20)
            print u'密级字段值“'+text+'"与呈报时的值"'+self.sub_text20+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'密级字段值“'+text+'"与呈报时的值"'+self.sub_text20+'"不一致"'+u'”'
        #判断正文附件字段
        try:
            text=driver.find_element_by_xpath(".//*[@id='AttachmentDIV5']/a[2]").text
            self.assertEqual(text, self.sub_text17)
            print u'正文附件“'+text+'"与添加时的"'+self.sub_text17+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'正文附件“'+text+'"与添加时的"'+self.sub_text17+'"不一致"'+u'”' 
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
