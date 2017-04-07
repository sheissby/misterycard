# encoding: utf-8
import uuid
import time
import datetime
import base64


# 生成guid
def guid():
    print uuid.uuid4()


# 时间戳转换
def timestampTransfor():
    # 当前时间
    print datetime.datetime.now()
    # unix时间戳
    print time.time()
    print time.mktime(datetime.datetime.now().timetuple())


