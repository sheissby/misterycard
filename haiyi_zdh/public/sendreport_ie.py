#coding=utf-8
import unittest
import os ,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
#调用压缩脚本
import zipfile1

#定义发送邮件
def sentmail(file_new):
    #构造邮件实例
    msg = MIMEMultipart()

    #邮件主题内容+++++++++++++++++++++++++++++++++++
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    body = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg.attach(body)

    #定义发送、收件箱++++++++++++++++++++++++++++++++
    #发信邮箱
    msg['From']='gao-bin@hna.net'
    #收信邮箱
    strto=["liubo1@haihangyun.com","gao-bin@haihangyun.com","xlin-wang1@haihangyun.com"]
    msg['To'] = ";".join(strto)
    print msg['To']

    #定义发送的邮件标题、项目测试用例、报告和截图附件++++++++++++++++++++++++
    #定义标题
    msg['Subject']=u"海医OA自动化测试报告"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    #msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')  
  
    #构造测试用例附件，定义相对路径  
    att = MIMEText(open(os.getcwd().split('public')[0]+'\\testcase.xlsx', 'rb').read(), 'base64', 'gb2312')   
    att["Content-Type"] = 'application/octet-stream'   
    att["Content-Disposition"] = 'attachment; filename="医学院项目测试用例.xlsx"'   
    msg.attach(att)

##    #构造测试报告附件    
##    att2 = MIMEText(open(file_new, 'rb').read(), 'base64', 'gb2312')
##    att2["Content-Type"] = 'application/octet-stream'   
##    att2["Content-Disposition"] = 'attachment; filename="医学院项目(ie下)自动化测试报告.html"' 
##    msg.attach(att2)

    #构造报告与截图附件，定义相对路径 
    att3 = MIMEText(open(os.getcwd().split('public')[0]+'\\fj_zip\\fj_zip.zip', 'rb').read(), 'base64', 'gb2312')
    att3["Content-Type"] = 'application/octet-stream'   
    att3["Content-Disposition"] = 'attachment; filename="报告与截图附件.zip"' 
    msg.attach(att3)

##    #连接邮件服务器++++++++++++++++++++++++++++++++++++++++++++++++
##    #连接SMTP 服务器，此处用的QQ的SMTP 服务器
##    s = smtplib.SMTP_SSL('smtp.qq.com',465)    
##    #QQ邮箱的用户名、授权密码输入
##    s.login('1454579512@qq.com','vjdswnwbbbhjhgib')
##    s.sendmail(msg['From'],strto,msg.as_string())
##    s.quit()
##    print u'邮件发送成功 !'

    #连接邮件服务器++++++++++++++++++++++++++++++++++++++++++++++++
    smtp=smtplib.SMTP()
    smtp.connect('ismtp.hnair.com')
    smtp.login('gao-bin@hna.net','123666.a')
    smtp.sendmail(msg['From'],strto,msg.as_string())
    smtp.quit()   
    print u'邮件发送成功 !'

#查找测试报告，调用发邮件功能
def sendreport():
    
##    #进行错误截图和最新报告的整合++++++++++++++++++++++++++
##    #定义存放在img中的错误截图的路径
##    dir1=open(os.getcwd().split('public')[0]+'\\img'
##    #定义报告和错误截图存放到整合文件夹fj_zip下并压缩
##    zip_path=os.getcwd().split('public')[0]+'\\fj_zip\\fj_zip.zip'
##    zipfile1.zip_dir(dir1,dir2,zip_path)

    #定义报告的相对路径++++++++++++++++++++++++++++++++++++++++++++++++++
    result_dir =os.getcwd().split('public')[0]+'\\report\\ie'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
               os.path.isdir(result_dir+"\\"+fn) else 0)
    
    #打印最新的测试报告
    print u'最新测试生成的报告： '+lists[-1].decode('gbk').encode('utf-8')    
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    #打印最新生成的报告
    print file_new

    #进行错误截图和最新报告的整合++++++++++++++++++++++++++
    #定义存放在img中的错误截图的路径
    dir1=os.getcwd().split('public')[0]+'\\img'   
    #定义报告和错误截图存放到整合文件夹fj_zip下并压缩
    zip_path=os.getcwd().split('public')[0]+'\\fj_zip\\fj_zip.zip'
    zipfile1.zip_dir(dir1,file_new,zip_path)
    
    #调用发邮件模块
    sentmail(file_new)

#发送邮件
if __name__ == "__main__":
    sendreport()


