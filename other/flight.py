# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time


def flight():
    profile = FirefoxProfile(r"C:\Users\Evan\AppData\Roaming\Mozilla\Firefox\Profiles\dq18g4u7.default")
    browser = webdriver.Ie()
    browser.get("http://x.hna.net/BusinessPicks/Pages/Flight/")
    # browser.get("https://www.baidu.com")
    # search = browser.find_element_by_class_name("btn_blue_02").click()


if __name__ == "__main__":
    flight()
