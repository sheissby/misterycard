# -*- coding: utf-8 -*-
import os
import stat
import shutil

#删除某个文件夹下的所有文件
def CleanDir(Dir):
    if os.path.isdir(Dir):
        paths = os.listdir(Dir)
        for path in paths:
            filePath = os.path.join(Dir, path)
            if os.path.isfile( filePath ):
                os.chmod(filePath, stat.S_IREAD | stat.S_IWRITE)
                try:
                        os.remove( filePath )#删除该文件
                        print u'删除之前的错误截图，如下：'
                        print filePath#打印已删除的文件
                except os.error:
                    autoRun.exception( "remove %s error." %filePath )#报错信息
            elif os.path.isdir( filePath ):
                CleanDir(filePath)
    return True
def del_img(Dir):
    print Dir
##Dir = r"F:\TJHKZDH2" #需删除的文件所属文件夹的上层文件路径
##Dir = os.getcwd().split('TJHKZDH2')[0] #需删除的文件所属文件夹的上层文件路径
    if os.path.isdir(Dir):
        paths = os.listdir(Dir)
        for path in paths:
            filePath = os.path.join(Dir, path)
                    #删除img文件夹下的所有文件
            if "img" in path and os.path.isdir( filePath ):
                 CleanDir(filePath)
