# encoding:utf-8
from Login import *

def getCardUntilGet(id1, targetid):
    cardid = 0
    i = 0
    while cardid != targetid:
        login(id)
        # 每100次重新登录一次
        while i < 100:
            # 1：基础包；2：魔幻包；3：屌丝券；7：莉莉丝包
            data = 'SBshilianchou=0&Chip=1&GoodsId=7'
            url = host + '/shop.php?do=Buy&v=1878&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
            flg, jsonresponse = connection(url, data)
            i += 1
            if flg == 1:
                cardid = jsonresponse.get('data', 0)
                print cardid
                if int(cardid) == targetid:
                    return
            else:
                print id1[0], jsonresponse


if __name__ == '__main__':
    ids = [

          ]
    targetid = input('please enter targetid:')
    for id in ids:
        getcard = getCardUntilGet(id, targetid)
