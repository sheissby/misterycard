# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
class zdh_bwcp_hq_rec(unittest.TestCase):
    def setUp(self):
        
        #用户登录------------------------------------------------------------------------------------------------------
        #调用登录函数
        login.login_normal(self)
        #错误信息被打印
        self.verificationErrors = []
        #接受警告
        self.accept_next_alert = True
        #获取当前时间的函数
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        
        #定义字段取值++++++++++++++++++++++++++++++++++++++++++++++++++++
        #定义公文标题+当前时间的函数
        self.sub_text='bwcp_hq_rec'+now
        #定义公文收件人、呈报人、联系方式
        self.sub_text2=u'符晓玲'
        self.sub_text3=u'冯学冠'
        self.sub_text4=u'2'
        self.sub_text12=u'输血科'
        self.sub_text14=u'黄植'
        self.sub_text15=u'谭壮华'
        self.sub_text16='bwcp_hq_rec_hq'+now
        #显示用例名称
        print u'-------------------------《办文呈批单会签撤回功能测试》------------------------------'
        
    def test_zdh_bwcp_hq_rec(self):
        
        #打开公文管理-公文呈报-办文呈批单------------------------------------------------------------------------------------
        #打开浏览器
        driver = self.driver  
        #点击公文管理模块      
        driver.find_element_by_id("nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd").click()
        time.sleep(1) 
        #点击公文呈报导航链接
        driver.find_element_by_id("nav-c0baf144-2241-471a-8947-db8511046075").click()
        #思考时间
        time.sleep(1)  
        #定位到办文呈批单的所属框架
        driver.switch_to_frame("diaConIf")   
        #点击办文呈批单链接
        driver.find_element_by_xpath("html/body/div[2]/div/table[1]/tbody/tr/td[2]/div/ul/li/table/tbody/tr/td[1]/a").click()
        time.sleep(1)   

        #公文内容中，配置字段，点击提交-------------------------------------------------------------------------------------
        #获取呈报页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)
        
        #输入呈批单属性、标题、印发份数、起文时间、印发日期字段+++++++++++++++++
        driver.find_element_by_id("080108").click()
        time.sleep(1)
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").clear()
        driver.find_element_by_id("2fff7b71-4436-4646-815b-a61f31b61574").send_keys(self.sub_text)
        driver.find_element_by_id("2ab2465a-d822-4b56-bd42-a4900a20f4e8").clear()
        driver.find_element_by_id("2ab2465a-d822-4b56-bd42-a4900a20f4e8").send_keys(self.sub_text4)
        js="$(\"input[id='fab70432-fe83-4754-a419-76d752f8e0fd']\").removeAttr('readonly');$(\"input[id='fab70432-fe83-4754-a419-76d752f8e0fd']\").attr('value','2016-08-01')"
        driver.execute_script(js)
        js="$(\"input[id='2da0c1a9-76d0-402d-a4f4-566472a6daf4']\").removeAttr('readonly');$(\"input[id='2da0c1a9-76d0-402d-a4f4-566472a6daf4']\").attr('value','2016-8-6')"
        driver.execute_script(js)
        time.sleep(1)

        #发放范围选择++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #点击机构选择按钮       
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[6]/td[1]/img").click()
        css1=driver.find_element_by_css_selector('.doc_content')
        #定位到机构选择页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        time.sleep(1)
        #定位到机构选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询机构
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text12)
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

        #收件人选择+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #点击收件人选择按钮       
        driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[8]/td[1]/img").click()
        #定位到人员选择页面的窗口
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

        #附件选择+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #定位到附件
        driver.find_element_by_id("tbFilePost_FileUpload").send_keys("")
        #模拟键盘操作
        win32api.keybd_event(13,0,0,0)
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(1)       
        #获取附件操作的上层和本层窗口
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
        time.sleep(1)
        driver.find_element_by_id("tbFilePost_uploadify").click()
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
      
        #点击提交按钮+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        driver.find_element_by_id("bt_Submit").click()
        time.sleep(4)
        print u'可正常提交公文'
        
        #杀掉火狐对插件不兼容的提示+++++++++++++++++++++++++++++++++++++++++++++++
##        os.system("taskkill /F /IM plugin-container.exe")
        
        #使用符晓玲（200518）登录-----------------------------------------------------------------
        #获取当前窗口，回到原窗口
        nowhandle=driver.current_window_handle
        driver.switch_to_window(nowhandle)
        time.sleep(1)    
        driver.quit()
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

        #查询处，输入字段，点击查询-------------------------------------------------------------------------------------------
        #获取当前窗口
        nowhandle=driver.current_window_handle
        #定位到公文签批查询字段的所属框架
        driver.switch_to_frame("diaConIf")
        #输入标题字段的值
        driver.find_element_by_id("ctrTitle").send_keys(self.sub_text)
        #点击查询按钮
        driver.find_element_by_id("IB_search").click()
        time.sleep(1)

        #查询结果判断---------------------------------------------------------------------------------------------
        #公文类型字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[2]").text
            self.assertEqual(text,u'办文呈批单')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型是办文呈批单' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型不是办文呈批单'
        time.sleep(1)
        #标题字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]").text
            self.assertEqual(text, self.sub_text)
            print u'公文签批的结果列表里存在，标题“'+self.sub_text+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里不存在，标题“'+self.sub_text+u'”'
        time.sleep(1)
        #签批状态字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            self.assertEqual(text, u'签批')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的签批状态是签批' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的签批状态不是签批'
        time.sleep(1)
        #发送人字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
            self.assertEqual(text, self.sub_text3)
            print u'公文签批的结果列表里的发送人“'+text+'"与呈报时的人员"'+self.sub_text3+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里的发送人“'+text+'"与呈报时的人员"'+self.sub_text3+'"不一致"'+u'”'
        time.sleep(1)

        #查询结果中，点击标题链接，打开公文详情--------------------------------------------------------------------------------------------
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()

        #公文详情中，点击发送/删除会签按钮，弹出发送会签分配页面----------------------------------------------------------------------------------------
        #获取所有窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])     
        #定位到所属框架
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        #点击发送/删除会签按钮       
        driver.find_element_by_id("IB_sendsplit").click()
        time.sleep(1)
        
        #会签分配页面，配置字段，点添加----------------------------------------------------------------------------------------------------
        #公文批复中的会签接收人选择+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #获取当前窗口，回到原窗口
        nowhandle=driver.current_window_handle
        driver.switch_to_window(nowhandle)
        time.sleep(1)
        #定位到会签分配页面所属框架
        driver.switch_to_frame("_DialogFrame_diagSendSplitBox")
        
        #点击收件人选择按钮       
        driver.find_element_by_id("SelectUser_imgBt").click()
        #定位到人员选择页面的窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[1])
        time.sleep(1)   
        #定位到人员选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入1个会签人员，点击查询、添加人员
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text14)
        driver.find_element_by_id("btn_Search").click()
        driver.find_element_by_id("ibtAddMsg").click()
        #输入另外1个会签人员，点击查询、添加人员
        driver.find_element_by_id("tb_Search").clear()
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text15)
        driver.find_element_by_id("btn_Search").click()
        driver.find_element_by_id("ibtAddMsg").click()
        #点击提交人员
        driver.find_element_by_id("ibtSubmit").click()
        time.sleep(4)
        #获取会签分配页面窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])
        #定位到会签分配页面所属框架
        driver.switch_to_frame("_DialogFrame_diagSendSplitBox")

        #会签分配页面，输入会签标题，点击确定按钮++++++++++++++++++++++++++++++++++++++++++
        driver.find_element_by_id("tbTitle").send_keys(self.sub_text16)
        driver.find_element_by_id("IB_add").click()
        time.sleep(1)
        #在会签提示对话框中点击确定按钮
        driver.find_element_by_xpath("html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]").click()
        time.sleep(6)
        print u'可进行会签分配'
        
        #关闭浏览器，使用黄植（3218）登录--------------------------------------------------------------------------------------
        driver.quit()
        time.sleep(1)
        login.login_normal3(self)

        #打开公文管理-公文签批-------------------------------------------------------------------------------------------------
        #重新打开浏览器
        driver = self.driver
        #定位且鼠标移到公文管理模块
        above=driver.find_element_by_xpath(".//*[@id='nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd']/a")
        ActionChains(driver).move_to_element(above).perform()
        #点击公文签批导航链接
        driver.find_element_by_xpath(".//*[@id='nav-70f461d6-02d9-4a0e-9c75-1b38aa29da02']/a").click()
        #思考时间
        time.sleep(1)
        
        #查询处，输入字段，点击查询-------------------------------------------------------------------------------------------
        #获取当前窗口
        nowhandle=driver.current_window_handle
        #定位到公文签批查询字段的所属框架
        driver.switch_to_frame("diaConIf")
        #输入标题字段的值
        driver.find_element_by_id("ctrTitle").send_keys(self.sub_text16)
        #点击查询按钮
        driver.find_element_by_id("IB_search").click()
        time.sleep(1)

        #查询结果判断---------------------------------------------------------------------------------------------------------
        #公文类型字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[2]").text
            self.assertEqual(text,u'办文呈批单会签件')
            print u'公文签批的会签结果列表里标题“'+self.sub_text16+u'”的公文类型是办文呈批单会签件' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的会签结果列表里标题“'+self.sub_text16+u'”的公文类型不是办文呈批单会签件'
        time.sleep(1)
        #标题字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]").text
            self.assertEqual(text, self.sub_text16)
            print u'公文签批的会签结果列表里存在，标题“'+self.sub_text16+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的会签结果列表里不存在，标题“'+self.sub_text16+u'”'
        time.sleep(1)
        #签批状态字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            self.assertEqual(text, u'会签签批')
            print u'公文签批的结果列表里标题“'+self.sub_text16+u'”的签批状态是会签签批' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text16+u'”的签批状态不是会签签批'
        time.sleep(1)
        #发送人字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
            self.assertEqual(text, self.sub_text2)
            print u'公文签批的结果列表里的发送人“'+text+'"与呈报时的人员"'+self.sub_text2+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里的发送人“'+text+'"与呈报时的人员"'+self.sub_text2+'"不一致"'+u'”'
        time.sleep(1)

        #使用符晓玲（200518）登录---------------------------------------------------------------------------
        #获取当前窗口，回到原窗口
        nowhandle=driver.current_window_handle
        driver.switch_to_window(nowhandle)
        time.sleep(1)    
        #关闭页面
        driver.quit()
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

        #查询处，输入字段，点击查询-------------------------------------------------------------------------------------------
        #获取当前窗口
        nowhandle=driver.current_window_handle
        #定位到公文签批查询字段的所属框架
        driver.switch_to_frame("diaConIf")
        #输入标题字段的值
        driver.find_element_by_id("ctrTitle").send_keys(self.sub_text)
        #点击查询按钮
        driver.find_element_by_id("IB_search").click()
        time.sleep(1)

        #查询结果判断---------------------------------------------------------------------------------------------
        #公文类型字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[2]").text
            self.assertEqual(text,u'办文呈批单')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型是办文呈批单' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型不是办文呈批单'
        time.sleep(1)
        #标题字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]").text
            self.assertEqual(text, self.sub_text)
            print u'公文签批的结果列表里存在，标题“'+self.sub_text+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里不存在，标题“'+self.sub_text+u'”'
        time.sleep(1)
        #签批状态字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[4]").text
            self.assertEqual(text, u'等待会签')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的签批状态是等待会签' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的签批状态不是等待会签'
        time.sleep(1)
        #发送人字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]").text
            self.assertEqual(text, self.sub_text3)
            print u'公文签批的结果列表里的发送人“'+text+'"与呈报时的人员"'+self.sub_text3+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里的发送人“'+text+'"与呈报时的人员"'+self.sub_text3+'"不一致"'+u'”'
        time.sleep(1)

        #查询结果中，点击标题链接，打开公文详情--------------------------------------------------------------------------------------------
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()

        #公文详情中，点击发送/删除会签按钮，弹出发送会签分配页面----------------------------------------------------------------------------------------
        #获取所有窗口
        allhandles=driver.window_handles
        driver.switch_to_window(allhandles[0])     
        #定位到所属框架
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        #点击发送/删除会签按钮       
        driver.find_element_by_id("IB_sendsplit").click()
        
        #会签分配页面，选择人员，删除----------------------------------------------------------------------------------------------------
        #获取分配页面的窗口
        nowhandle=driver.current_window_handle
        driver.switch_to_window(nowhandle)
        #定位到会签分配页面所属框架
        driver.switch_to_frame("_DialogFrame_diagSendSplitBox")
        time.sleep(1)
        
        #点击删除按钮       
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[5]/label/img").click()
        time.sleep(1)
        #在会签删除提示对话框中点击确定按钮
        driver.find_element_by_xpath("html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]").click()
        time.sleep(4)
        print u'可正常进行会签人员删除'

        #会签删除后，关闭浏览器，使用黄植（3218）登录--------------------------------------------------------------------------------------
        driver.quit()
        time.sleep(1)
        login.login_normal3(self)

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

        #查询处，输入字段，点击查询-------------------------------------------------------------------------------------------
        #获取当前窗口
        nowhandle=driver.current_window_handle
        #定位到公文签批查询字段的所属框架
        driver.switch_to_frame("diaConIf")
        #输入标题字段的值
        driver.find_element_by_id("ctrTitle").send_keys(self.sub_text16)
        #点击查询按钮
        driver.find_element_by_id("IB_search").click()
        time.sleep(1)
            
        #会签撤回后的查询结果判断----------------------------------------------------------------------------------------------
        #获取整体结果列表的ID
        table=driver.find_element_by_id("dgQuery")
        #列表标签多个行定义，包含标题行
        tr=table.find_elements_by_tag_name("tr")
        #进行删除后查询结果判断，是否大于1行，
        if len(tr)>1:
            self.verificationErrors.append('del fail')
            print self.sub_text+u'公文会签撤回数据失败，公文签批处存在该数据'
        else :
            print self.sub_text+u'公文会签撤回数据成功，公文签批处不存在该数据'
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
