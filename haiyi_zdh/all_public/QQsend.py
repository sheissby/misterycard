# -*- coding: utf-8 -*-  
# 需要先安装pywin32模块  
  
import win32gui  
import win32con  
import win32clipboard as w
import time,win32api
  
# 取剪贴板文本  
def getText():  
    w.OpenClipboard()  
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)  
    w.CloseClipboard()  
    return d  
  
# 设置剪贴板文本  
def setText(aString):  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)  
    w.CloseClipboard()  
def sendmsg(QQqunName,content):
    # QQ群发送消息   
    setText(content)  
    qqhd=win32gui.FindWindow(None,QQqunName)  
    if qqhd==0:
        print u'未找到“'+QQqunName+'”的QQ窗口，请检查该QQ窗口是否处于打开状态，并且须为单独的窗口'
    # 投递剪贴板消息到QQ窗体  
    win32gui.SendMessage(qqhd,258,22,2080193)  
    win32gui.SendMessage(qqhd,770,0,0)  
    # 模拟按下回车键  
    #win32gui.SendMessage(qqhd,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)  
    #win32gui.SendMessage(qqhd,win32con.WM_KEYUP,win32con.VK_RETURN,0)
    # 模拟按下Ctrl+enter
    time.sleep(1)
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(13,0,0,0)  #venter码是13
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
if __name__ == '__main__':
    QQqunName=u"阿黄" #qq名称  
    content=u"测试消息"
    sendmsg(QQqunName,content)