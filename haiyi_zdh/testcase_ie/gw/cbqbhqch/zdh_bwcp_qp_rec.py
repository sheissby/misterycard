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
from haiyi_zdh.public.ie import login
#调用关闭Plugin Container 冲突窗口
import closewindow

#案例
class zdh_bwcp_qp_rec(unittest.TestCase):
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
        self.sub_text='bwcp_qp_rec'+now
        #定义公文收件人、呈报人、联系方式
        self.sub_text2=u'符晓玲'
        self.sub_text3=u'冯学冠'
        self.sub_text4=u'2'
        self.sub_text12=u'输血科'
        self.sub_text13=u'丁娥'
        #显示用例名称
        print u'-------------------------《办文呈批单签批撤回功能测试》------------------------------'
        
    def test_zdh_bwcp_qp_rec(self):
        
        #打开公文管理-公文呈报-办文呈批单------------------------------------------------------------------------------------
        #打开浏览器
        driver = self.driver
        #赋窗口空值，获取当前窗口
        allhandlelist=[]
        nowhandle=driver.current_window_handle
        allhandlelist.append(nowhandle)
        #点击公文管理模块      
        driver.find_element_by_id("nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd").click()
        time.sleep(1)
        #点击公文呈报导航链接，设置思考时间
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[1]/a").click()
        time.sleep(1)
        
        #定位iframe框架+++++++++++++++++++++++++++
        #找div class="mainRight"
        frame=driver.find_element_by_css_selector('.mainRight')
        #遍历下方的iframe
        frames=frame.find_elements_by_tag_name('iframe')
        #取第1个iframe
        driver.switch_to_frame(frames[0])  
        #点击办文呈批单链接
        driver.find_element_by_xpath("html/body/div[2]/div/table[1]/tbody/tr/td[2]/div/ul/li/table/tbody/tr/td[1]/a").click()
        time.sleep(1)   

        #公文内容中，配置字段，点击提交-------------------------------------------------------------------------------------
        #获取呈报页面窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")

        #输入呈批单属性、标题、印发份数、起文时间、印发日期字段+++++++++++++++++
        driver.find_element_by_id("080108").click()        
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
        #双击机构选择按钮       
        double=driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[6]/td[1]/img")
        ActionChains(driver).double_click(double).perform()   
        time.sleep(1)     
        #获取添加页面的上层窗口和本层窗口
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))#与上层窗口作比较
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)
        #定位到机构选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询机构
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text12)
        #点击查询、双击添加、单击提交机构
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
        #定位到呈报页面的所属框架
        driver.switch_to_frame("_DialogFrame_0")
        time.sleep(1)

        #收件人选择+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #双击收件人选择按钮       
        double=driver.find_element_by_xpath(".//*[@id='doc_main']/div[2]/table/tbody/tr[8]/td[1]/img")
        ActionChains(driver).double_click(double).perform()   
        time.sleep(1)
        #获取添加页面的上层窗口和本层窗口        
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
            
        #点击提交按钮+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

        #查询处，输入字段，点击查询-------------------------------------------------------------------------------------------
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
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

        #查询结果中，点击标题链接，打开公文详情-----------------------------------------------------------------------------------
        driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]/label").click()
        time.sleep(1)

        #公文详情中，配置字段，点击提交意见----------------------------------------------------------------------------------------
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)   
        #定位到所属框架
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")

        #公文批复中的收件人选择+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #点击收件人选择按钮       
        driver.find_element_by_xpath(".//*[@id='SelectUser_imgBt']").click()
        #获取页面的上层和本层窗口
        driver.switch_to_window(nowhandle)
        allhandles=driver.window_handles
        allhandlelist=allhandlelist+list(set(allhandles).difference(set(allhandlelist)))#与上层窗口作比较
        driver.switch_to_window(allhandlelist[1])
        time.sleep(1)   
        #定位到人员选择页面名称字段查询所属框架
        driver.switch_to_frame("mainFrame")
        #输入查询人员
        driver.find_element_by_id("tb_Search").send_keys(self.sub_text13)
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
        #定位到所属框架
        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
        time.sleep(1)

##        #公文批复中的附件选择+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##        #定位到要双击的附件元素，并执行双击
##        double2=driver.find_element_by_id("tbFilePost_FileUpload")
##        ActionChains(driver).double_click(double2).perform()
##        time.sleep(1)       
##        #获取附件操作的本层窗口
##        driver.switch_to_window(allhandlelist[0])       
##        time.sleep(1)
##        #定位到页面的所属框架
##        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
##        time.sleep(1)
##        #找div class="fancybox-inner"，定位增加文件按钮的frame
##        frame=driver.find_element_by_css_selector('.fancybox-inner')
##        #遍历下方的iframe
##        frames=frame.find_elements_by_tag_name('iframe')
##        #取第1个iframe
##        driver.switch_to_frame(frames[0])
##        #单击增加文件按钮
##        driver.find_element_by_id("tbFilePost_uploadify").click()
##        time.sleep(1)
##        #调用auto工具保存的附件上传word文件
##        os.startfile(os.getcwd().split('testcase_Ie')[0]+'\uploadfile\Ie_gw_doc.exe')
##        time.sleep(4)
##        #点击添加
##        driver.find_element_by_id("tbFilePost_OK").click()
##        time.sleep(1)  
##        #获取页面窗口
##        driver.switch_to_window(allhandlelist[0])
##        time.sleep(1)
##        #定位到页面的所属框架
##        driver.switch_to_frame("_DialogFrame_diagSignMainBox")
##        time.sleep(1)

        #输入签批意见，单击提交意见
        driver.find_element_by_xpath(".//*[@id='tbConten']").send_keys(u'签批同意。')
        time.sleep(1)
        driver.find_element_by_id("btnIBSure").click()
        time.sleep(4)
        print u'可正常批复公文'

        #打开公文管理-公文跟踪-------------------------------------------------------------------------------------------------
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #单击公文管理模块
        driver.find_element_by_id("nav-98bce320-dc6e-4fb4-9fae-de494ab9acfd").click()
        time.sleep(1)
        #点击公文跟踪导航链接
        driver.find_element_by_xpath(".//*[@id='main']/div[1]/div/ul/li[4]/a").click()  
        time.sleep(1)
        
        #公文跟踪查询处，输入字段，点击查询-------------------------------------------------------------------------------------
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #定位到公文签批查询字段的所属框架
        driver.switch_to_frame("diaConIf")
        #选择本人经手的公文
        driver.find_element_by_id("rb_right").click()
        #输入标题、呈报时间
        driver.find_element_by_id("txbTitle").clear()
        driver.find_element_by_id("txbTitle").send_keys(self.sub_text)
        driver.find_element_by_id("ctrStartDate").clear()
        driver.find_element_by_id("ctrStartDate").send_keys(u'2016-01-01')
        driver.find_element_by_id("ctrEndDate").clear()
        driver.find_element_by_id("ctrEndDate").send_keys(u'12-31')      
        #定位和选择公文类型的下拉框
        ddlType=driver.find_element_by_id('ddlType')
        ddlType.find_element_by_xpath("//option[@value='100402']").click()
        time.sleep(1)
        ddlDetailType=driver.find_element_by_id('ddlDetailType')
        ddlDetailType.find_element_by_xpath("//option[@value='tb164']").click()
        time.sleep(1)
        
        #点击查询按钮
        driver.find_element_by_id("IB_search").click()
        time.sleep(1)
        
        #查询结果判断-------------------------------------------------------------------------------------------------------
        #标题字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]").text
            self.assertEqual(text, self.sub_text)
            print u'公文跟踪的结果列表里存在，标题“'+self.sub_text+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文跟踪的结果列表里不存在，标题“'+self.sub_text+u'”'
        #公文类型字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[6]").text
            self.assertEqual(text,u'办文呈批单')
            print u'公文跟踪的结果列表里标题“'+self.sub_text+u'”的公文类型是办文呈批单' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文跟踪的结果列表里标题“'+self.sub_text+u'”的公文类型不是办文呈批单'
        #当前节点字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[7]").text
            self.assertEqual(text, self.sub_text13)
            print u'公文跟踪的结果列表里的当前节点“'+text+'"与批复的接收人"'+self.sub_text13+'"一致"'+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文跟踪的结果列表里的当前节点“'+text+'"与批复的接收人"'+self.sub_text13+'"不一致"'+u'”'
        time.sleep(1)

        #点击公文撤回-----------------------------------------------------------------------------------------------------
        driver.find_element_by_xpath(".//*[@id='dgQuery_ctl02_btnWFReturn']/img").click()
        time.sleep(1)
        
        #撤回的确定、取消对话框判断+++++++++++++++++++++++++++++++++++++++++
        #接受告警信息,判断是否有取消按钮
        alert = driver.switch_to_alert()
        #点击取消按钮
        driver.find_element_by_xpath("html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
        time.sleep(1)
        print u'存在确定、取消对话框，撤回的取消功能正常'
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #定位到公文跟踪查询字段的所属框架
        driver.switch_to_frame("diaConIf")
        
        #取消撤回后重新查询该数据++++++++++++++++++++++++++++++++++++++++++++
        #输入标题
        driver.find_element_by_id("txbTitle").click()
        driver.find_element_by_id("txbTitle").clear()
        driver.find_element_by_id("txbTitle").send_keys(self.sub_text)
        time.sleep(1)
        #点击查询按钮
        driver.find_element_by_id("IB_search").click()
        time.sleep(1)

        #取消撤回后的查询结果判断+++++++++++++++++++++++++++++++++++++++++++++++
        #标题字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[3]").text
            self.assertEqual(text, self.sub_text)
            print u'公文跟踪的撤销-取消后的结果列表里存在，标题“'+self.sub_text+u'”' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文跟踪的撤销-取消后的结果列表里不存在，标题“'+self.sub_text+u'”'
        time.sleep(1)

        #进行撤回对话框的确定按钮的判断+++++++++++++++++++++++++++++++++++++++++
        #点击撤回按钮
        driver.find_element_by_xpath(".//*[@id='dgQuery_ctl02_btnWFReturn']/img").click()
        time.sleep(1) 
        #接受告警信息,判断是否有确定按钮
        alert = driver.switch_to_alert()
        #点击确定按钮
        driver.find_element_by_xpath("html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]").click()
        time.sleep(4)
        print u'存在确定、取消对话框，撤回的确定功能正常'   
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0])
        time.sleep(1)
        #定位到公文跟踪查询字段的所属框架
        driver.switch_to_frame("diaConIf")
        
        #确定撤回后重新查询该数据----------------------------------------------------------------------------------------------
        #输入标题
        driver.find_element_by_id("txbTitle").click()
        driver.find_element_by_id("txbTitle").clear()
        driver.find_element_by_id("txbTitle").send_keys(self.sub_text)
        time.sleep(1)
        #点击查询按钮
        driver.find_element_by_id("IB_search").click()
        time.sleep(1)
        
        #确定撤回后的查询结果判断----------------------------------------------------------------------------------------------
        #获取整体结果列表的ID
        table=driver.find_element_by_id("dgQuery")
        time.sleep(1)
        #列表标签多个行定义，包含标题行
        tr=table.find_elements_by_tag_name("tr")
        
        #进行撤回后查询结果判断，是否大于1行，
        if len(tr)>1:
            self.verificationErrors.append('del fail')
            print self.sub_text+u'公文跟踪的撤回页面，撤回数据失败'
        else :
            print self.sub_text+u'公文跟踪的撤回页面，撤回数据成功'
        time.sleep(1)

        #打开公文管理-公文签批-----------------------------------------------------------------------------------------------------
        #获取当前窗口
        driver.switch_to_window(allhandlelist[0]) 
        time.sleep(1)
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
        #输入标题
        driver.find_element_by_id("ctrTitle").send_keys(self.sub_text)
        #点击查询按钮
        driver.find_element_by_id("IB_search").click()
        time.sleep(1)

        #签批撤回后的查询结果判断---------------------------------------------------------------------------------------------
        #公文类型字段判断
        try:
            text=driver.find_element_by_xpath(".//*[@id='dgQuery']/tbody/tr[2]/td[2]").text
            self.assertEqual(text,u'办文呈批单')
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型是办文呈批单' 
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print u'公文签批的结果列表里标题“'+self.sub_text+u'”的公文类型不是办文呈批单'
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
