#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
from selenium.webdriver.firefox.webdriver import FirefoxProfile

#登陆模块（函数）
def login_admin(self):
    #self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Ie()
    self.driver.implicitly_wait(30)
    driver = self.driver
    driver.get("http://10.70.73.68/WebUI/Login.aspx")
    #driver.get("http://10.2.57.150:8080/WebUI/Default.ashx")
    driver.maximize_window()
    driver.find_element_by_id("uname").clear()
    driver.find_element_by_id("uname").send_keys("oaadmin")
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys("123456")
    driver.find_element_by_id("btnLogin").click()
    try: self.assertEqual(u"系统管理", driver.find_element_by_link_text(u"系统管理").text)
    except AssertionError as e: self.verificationErrors.append(str(e))


def login_normal(self):
    #self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Ie()
    self.driver.implicitly_wait(30)
    driver = self.driver
    driver.get("http://10.70.73.68/WebUI/Login.aspx")
    #driver.get("http://10.2.57.150:8080/WebUI/Default.ashx")
    driver.maximize_window()
    driver.find_element_by_id("uname").clear()
    driver.find_element_by_id("uname").send_keys("200502")
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys("123.qwe")
    driver.find_element_by_id("btnLogin").click()
    try: self.assertEqual(u"冯学冠", driver.find_element_by_link_text(u"冯学冠").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
def login_normal2(self):
    #self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Ie()
    self.driver.implicitly_wait(30)
    driver = self.driver
    driver.get("http://10.70.73.68/WebUI/Login.aspx")
    #driver.get("http://10.2.57.150:8080/WebUI/Default.ashx")
    driver.maximize_window()
    driver.find_element_by_id("uname").clear()
    driver.find_element_by_id("uname").send_keys("200518")
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys("123.qwe")
    driver.find_element_by_id("btnLogin").click()
    try: self.assertEqual(u"符晓玲", driver.find_element_by_link_text(u"符晓玲").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
def login_normal3(self):
    #self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Ie()
    self.driver.implicitly_wait(30)
    driver = self.driver
    driver.get("http://10.70.73.68/WebUI/Login.aspx")
    #driver.get("http://10.2.57.150:8080/WebUI/Default.ashx")
    driver.maximize_window()
    driver.find_element_by_id("uname").clear()
    driver.find_element_by_id("uname").send_keys("3218")
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys("123.qwe")
    driver.find_element_by_id("btnLogin").click()
    try: self.assertEqual(u"黄植", driver.find_element_by_link_text(u"黄植").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
def login_normal4(self):
    #self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Ie()
    self.driver.implicitly_wait(30)
    driver = self.driver
    driver.get("http://10.70.73.68/WebUI/Login.aspx")
    #driver.get("http://10.2.57.150:8080/WebUI/Default.ashx")
    driver.maximize_window()
    driver.find_element_by_id("uname").clear()
    driver.find_element_by_id("uname").send_keys("200517")
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys("123.qwe")
    driver.find_element_by_id("btnLogin").click()
    try: self.assertEqual(u"吴忠旺", driver.find_element_by_link_text(u"吴忠旺").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
def login_normal5(self):
    #self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Ie()
    self.driver.implicitly_wait(30)
    driver = self.driver
    driver.get("http://10.70.73.68/WebUI/Login.aspx")
    #driver.get("http://10.2.57.150:8080/WebUI/Default.ashx")
    driver.maximize_window()
    driver.find_element_by_id("uname").clear()
    driver.find_element_by_id("uname").send_keys("200525")
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys("123.qwe")
    driver.find_element_by_id("btnLogin").click()
    try: self.assertEqual(u"谭壮华", driver.find_element_by_link_text(u"谭壮华").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
def login_normal6(self):
    #self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Ie()
    self.driver.implicitly_wait(30)
    driver = self.driver
    driver.get("http://10.70.73.68/WebUI/Login.aspx")
    #driver.get("http://10.2.57.150:8080/WebUI/Default.ashx")
    driver.maximize_window()
    driver.find_element_by_id("uname").clear()
    driver.find_element_by_id("uname").send_keys("2211")
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys("123.qwe")
    driver.find_element_by_id("btnLogin").click()
    try: self.assertEqual(u"丁娥", driver.find_element_by_link_text(u"丁娥").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
def login_normal7(self):
    #self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Ie()
    self.driver.implicitly_wait(30)
    driver = self.driver
    driver.get("http://10.70.73.68/WebUI/Login.aspx")
    #driver.get("http://10.2.57.150:8080/WebUI/Default.ashx")
    driver.maximize_window()
    driver.find_element_by_id("uname").clear()
    driver.find_element_by_id("uname").send_keys("2506")
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys("123.qwe")
    driver.find_element_by_id("btnLogin").click()
    try: self.assertEqual(u"马婧", driver.find_element_by_link_text(u"马婧").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
def login_normal8(self):
    #self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Ie()
    self.driver.implicitly_wait(30)
    driver = self.driver
    driver.get("http://10.70.73.68/WebUI/Login.aspx")
    #driver.get("http://10.2.57.150:8080/WebUI/Default.ashx")
    driver.maximize_window()
    driver.find_element_by_id("uname").clear()
    driver.find_element_by_id("uname").send_keys("2213")
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys("123.qwe")
    driver.find_element_by_id("btnLogin").click()
    try: self.assertEqual(u"黄娜", driver.find_element_by_link_text(u"黄娜").text)
    except AssertionError as e: self.verificationErrors.append(str(e))




