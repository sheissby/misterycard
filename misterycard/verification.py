# encoding:utf-8
from con_log import *


def verification():
    url = host + '/legion.php?do=GetLegions&v=7225&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data = 'Amount=10&Start=0'
    jsonresponse = connection(url, data)
    try:
        legionid = jsonresponse.get('data').get('MyInfo').get('LegionId')
        if legionid == '688':
            return 1
        else:
            print '此号不在圣域'
            return 0
    except Exception:
        print '获取军团错误'
        return 0