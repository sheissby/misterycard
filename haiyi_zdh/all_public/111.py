#coding=utf-8
import unittest
import os ,time
#读取ZIP压缩包的文件列表
import zipfile
import os
                      
file = zipfile.ZipFile("F:\TJHKZDH2\img\wgxl.zip")
 
for name in file.namelist():
    print name

print u'解压操作 unzip'
for name in file.namelist(): 
    file.extract(name,os.getcwd()+"/zipfile_module") #解压到当前目录
 
#关闭压缩文件句柄
file.close()
 
print u'压缩操作 zip'
#获取当前目录树
fileLists=[]
for root,dirs,files in os.walk("zipfile_module"):
    for name in dirs:
        fileLists.append(os.path.join(root, name)) #目录入列表
        for name in files:
            fileLists.append(os.path.join(root,name)) #文件入列表
#创建压缩文件
file2=zipfile.ZipFile(os.getcwd()+"/zipfile_module2"+".zip",'w',zipfile.ZIP_DEFLATED) #zipfile.zlib.DEFLATED 亦可
#写入目录树
for name in fileLists:
    file2.write(name)
#关闭压缩文件
file2.close()
