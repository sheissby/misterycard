# -*- coding: utf-8 -*-
import os
import stat
import shutil
 
def CleanDir(Dir):
    if os.path.isdir(Dir):
        paths = os.listdir(Dir)
        for path in paths:
            filePath = os.path.join(Dir, path)
            if os.path.isfile( filePath ):
                os.chmod(filePath, stat.S_IREAD | stat.S_IWRITE)
                try:
                    os.remove( filePath )
                except os.error:
                    autoRun.exception( "remove %s error." %filePath )#引入logging
            elif os.path.isdir( filePath ):
                CleanDir(filePath)
    return True
Dir = r"C:\Users\lenovo\AppData\Local\Temp"
if os.path.isdir(Dir):
    paths = os.listdir(Dir)
    for path in paths:
        filePath = os.path.join(Dir, path)
        if "tmp" in path and os.path.isdir( filePath ):
            print filePath
            CleanDir(filePath)
            shutil.rmtree(filePath,True)
