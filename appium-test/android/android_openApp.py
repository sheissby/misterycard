# encoding: utf-8
from appium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException


def openApp():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0.1'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.eking.android.enterprise.test'
    desired_caps['appActivity'] = 'com.eking.ekinglink.activity.ACT_Welcome'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)

    try:
        driver.find_element_by_id('com.eking.android.enterprise.test:id/buttonDefaultNegative').click()
        time.sleep(0.5)
        print '取消升级'
    except NoSuchElementException, e:
        print e
    finally:
        pass

    return driver

openApp()