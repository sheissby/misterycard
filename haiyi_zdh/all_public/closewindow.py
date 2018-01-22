#coding=utf-8
from win32gui import *
import win32con
def close_window(title):
    #找到目标程序
    while 1:
        hwnd=FindWindow(None, title)
        if IsWindow(hwnd):#  and IsWindowEnabled(hwnd)and IsWindowVisible(hwnd):
            PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        else:break
if __name__ == '__main__':
    close_window(u'Plugin Container for Firefox')