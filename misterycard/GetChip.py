# encoding: utf-8
from userinfo.con_log import *
from id import *

def getChip(id1):
    url = host + '/cardchip.php?do=CompositeChip&v=7112&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
    # 6003:五星万能  6002:四星万能
    # data = 'ChipId=6002&IsSuper=0'
    flg, jsonresponse = connection(url, data)
    if flg != '1':
        print id1[0], jsonresponse

id = Cmid()

if __name__ == '__main__':
    for id1 in id:
        con_log(*id1)
        getChip(id1)