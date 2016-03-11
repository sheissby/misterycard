# encoding:utf-8
import requests
import json
import time


header = {'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5'}


def connection(url, data):
    status = 0
    while status == 0:
        try:
            response = requests.post(url, data=data, headers=header)
            jsonresponse = json.loads(response.content)
            status = jsonresponse.get('status', 0)
            if status == 0:
                message = jsonresponse.get('message', 0)
                if message == '':
                    print '��¼ʧ��'
                    time.sleep(1)
                else:
                    return 1
        except requests.ConnectionError, e:
            print e
            status = 0
            time.sleep(1)
        except requests.HTTPError, e:
            print e
            status = 0
            time.sleep(1)
    return jsonresponse


def con(uid, sessionid):
    con_data = "Udid=64%3A09%3A80%3AD3%3AF3%3A0E&plat=ANDROID%5FXIAOMI&newguide=1&IDFA=" + '&uid=' + uid + '&sessionid=' + sessionid
    url = 'http://s1.xiaomi.mysticalcard.com/mpassport.php?do=plogin&v=3337&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
    jsonresponse = connection(url, con_data)
    return jsonresponse


def con_log(*id1):
    uid = id1[1]
    Muid = id1[2]
    sessionid = id1[3]
    y = con(uid, sessionid)
    ppsign = y.get('data', 0).get('uinfo', 0).get('ppsign', 0)
    sign = y.get('data', 0).get('uinfo', 0).get('sign', 0)
    times = '%d' % y.get('data', 0).get('uinfo', 0).get('time', 0)
    a = '&ppsign=' + ppsign
    b = '&sign=' + sign
    c = '&time=' + times
    d = '&MUid=' + Muid
    e = '&uin=' + uid
    f = '&nick=' + uid
    conlog_data = "access%5Ftoken=&plat=ANDROID%5FXIAOMI&newguide=1&Devicetoken=&Origin=xiaomi&IDFA=&Udid=64%3A09%3A80%3AD3%3AF3%3A0E" + d + e + f + c + b + a
    url = 'http://s1.xiaomi.mysticalcard.com/login.php?do=mpLogin&v=1521&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
    jsonresponse = connection(url, conlog_data)
    # print id1[0], 'con_log success!'

# 获得团战信息并解析
def GetLegionInfo():
    url = 'http://s1.xiaomi.mysticalcard.com/legionattack.php?do=info&v=9083&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data = ''
    jsonresponse = connection(url, data)
    for LegionInfo in jsonresponse.get('data').get('info'):
        Legionstatus = LegionInfo.get('Status')
        if Legionstatus == 3:  # 3表示参战时间
            legionId = LegionInfo.get('Id')
            AttackLegionId= LegionInfo.get('AttackLegion').get('LegionId')
            DefendLegionId = LegionInfo.get('DefendLegion').get('LegionId')
            if AttackLegionId == u'688' or AttackLegionId ==u'689':
                return legionId
            else:
                print '今天没团战'

# 参战
def legionattack(legionId):
    url1 = 'http://s1.xiaomi.mysticalcard.com/legionattack.php?do=join&v=3339&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    url2 = 'http://s1.xiaomi.mysticalcard.com/legionattack.php?do=exit&v=3340&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data1 = '&Type=1&Id=' + str(legionId)
    data2 = '&Type=2&Id=' + str(legionId)
    jsonresponse = connection(url1, data1)
    jsonresponse = connection(url2, data2)



id = [['Am', '1592626', '279696', 'tbmXwubvxzvP4nHa'],
      ['#Cm', '2014092692358474', '285154', 'tbmXwubvxzvP4nHa'],
      ['Em', '2014121327096245', '288121', 'tbmXwubvxzvP4nHa'],
      ['#Fm', '2015031960117052', '294557', 'tbmXwubvxzvP4nHa'],

      ['jinxiaoxi', '2014011514924154', '289074', 'TqctVYyZJmA6JrGC'],
      ['jinxiaoxiaoxi', '2014021715652853', '265008', 'TqctVYyZJmA6JrGC'],
      ['jinxiaoxiaoxiaoxi', '2015010132895122', '289017', 'TqctVYyZJmA6JrGC'],
      ['jinxixi', '2015011837740716', '289647', 'TqctVYyZJmA6JrGC'],
      ['jinxiaoxixi', '2015013142224275', '290057', 'TqctVYyZJmA6JrGC'],
      ['hong', '2015052882084219', '296351', 'TqctVYyZJmA6JrGC'],
      ['cong', '2015052882088503', '296352', 'TqctVYyZJmA6JrGC'],
      ['feng', '2015052882090943', '296354', 'TqctVYyZJmA6JrGC'],
      ['yu', '2015052882090503', '296353', 'v1soiQ8I8RgIvg2p'],

      ['R1', '2014021515603023', '264491', 'ekyOlt6j4VLipThy'],
      ['R2', '2014040452624347', '289393', 'ekyOlt6j4VLipThy'],
      ['XiaoXiaoZhu', '59079768', '289074', 'lVMmfvcdVHKt1OeA'],
      ['妙蛙种子', '2014052561883286', '278956', 'd6YpW93AIdMBso3Z'],
      ['绿毛虫', '2014061766465489', '278958', 'd6YpW93AIdMBso3Z'],
      ['大针蜂', '2014061866519659', '278984', 'd6YpW93AIdMBso3Z'],
      ['比比鸟', '2014061866519756', '278986', 'd6YpW93AIdMBso3Z'],
      ['超音蝠', '2014061866528941', '279006', 'd6YpW93AIdMBso3Z'],
      ['隆隆岩', '2014061866529032', '279007', 'd6YpW93AIdMBso3Z'],
      ['大岩蛇', '2014061866529097', '279009', 'd6YpW93AIdMBso3Z'],
      ['乘龙', '2014061866529223', '279045', 'd6YpW93AIdMBso3Z'],
      ['耿鬼', '2014061866529231', '279049', 'd6YpW93AIdMBso3Z'],
      ['烈焰马', '2014061866529288', '279053', 'd6YpW93AIdMBso3Z'],
      ['吸盘魔偶', '2014061866529337', '279054', 'd6YpW93AIdMBso3Z'],
      ['胖丁', '2014061866529346', '279080', 'd6YpW93AIdMBso3Z'],
      ['阿柏蛇', '2014061866529379', '279081', 'd6YpW93AIdMBso3Z'],
      ['椰蛋树', '2014061866529407', '279083', 'd6YpW93AIdMBso3Z'],
      ['火爆猴', '2014061866529462', '279085', 'd6YpW93AIdMBso3Z'],
      ['派拉斯', '2014061866529470', '279086', 'd6YpW93AIdMBso3Z'],
      ['比雕', '2014061866529500', '279117', 'd6YpW93AIdMBso3Z'],
      ['雷精灵', '2014061866529554', '279119', 'd6YpW93AIdMBso3Z'],
      # ['皮卡西', '2014061866529628', '279122', 'd6YpW93AIdMBso3Z'],
      # ['水精灵', '2014061866529641', '279131', 'd6YpW93AIdMBso3Z'],
      # ['火精灵', '2014061866529643', '279137', 'd6YpW93AIdMBso3Z'],
      # ['胡地', '2014061866529675', '279164', 'd6YpW93AIdMBso3Z'],
      # ['风速狗', '2014061866529735', '279165', 'd6YpW93AIdMBso3Z'],
      # ['喷火龙', '2014061866529744', '279166', 'd6YpW93AIdMBso3Z']
      ]

id1 = ['#Cm', '2014092692358474', '285154', 'tbmXwubvxzvP4nHa']
# 先登录得到团战信息
con_log(*id1)
legionId = GetLegionInfo()
# 循环登录参战
for id1 in id:
    con_log(*id1)
    legionattack(legionId)
raw_input('The End')
