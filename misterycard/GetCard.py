# encoding:utf-8
from userinfo.con_log import *

def getCardUntilGet(id1, targetid):
    cardid = 0
    i = 0
    while cardid != targetid:
        con_log(*id1)
        # 每100次重新登录一次
        while i < 100:
            # 1：基础包；2：魔幻包；3：屌丝券；7：莉莉丝包
            data = 'SBshilianchou=0&Chip=1&GoodsId=7'
            url = host + '/shop.php?do=Buy&v=1878&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
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
    id = [
        ['Dsus4', '2013122514488598', '290176', 'LnQ6qpKCyY95nIrg']
          ]
    targetid = input('please enter targetid:')
    for id1 in id:
        getcard = getCardUntilGet(id1, targetid)
