# encoding: utf-8
from Login import *


def getChip(id):
    login(id)
    url = host + '/cardchip.php?do=CompositeChip&v=7112&ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    # 6003:五星万能  6002:四星万能
    # data = 'ChipId=6002&IsSuper=0'
    flg, jsonresponse = connection(url, data)
    if flg != 1:
        print id[0], jsonresponse


def getLegionShop(id):
    url = host + '/legion.php?do=Shop&v=7123&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    data = ''
    flg, jsonresponse = connection(url, data)
    if flg == 1:
        cardsId = jsonresponse.get('data').get('CardIds')
        for cardId in cardsId:
            if cardId == u'296':
                print id[0], '今天商店有兔子'
            else:
                print '没兔子'
    else:
        print id[0], jsonresponse

ids = Cmid()

if __name__ == '__main__':
    for id in ids:
        login(id)
        # getChip(id)
        getLegionShop(id)
