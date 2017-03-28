# encoding: utf-8
import uuid
import time
import datetime


# 生成guid
def guid():
    print uuid.uuid4()


# 时间戳转换
def timestampTransfor():
    print datetime.datetime.now()
    print datetime.datetime.now().timetuple()
    print time.time()
    print time.mktime(datetime.datetime.now().timetuple())

