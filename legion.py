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
        legionId = LegionInfo.get('Id')
        AttackLegionId= LegionInfo.get('AttackLegion').get('LegionId')
        DefendLegionId = LegionInfo.get('DefendLegion').get('LegionId')
        if Legionstatus == 3 and (AttackLegionId == u'688' or AttackLegionId == u'689'):

            # if AttackLegionId == u'688' or AttackLegionId == u'689':
            return legionId
    return -1

# 参战
def legionattack(legionId):
    url1 = 'http://s1.xiaomi.mysticalcard.com/legionattack.php?do=join&v=3339&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    url2 = 'http://s1.xiaomi.mysticalcard.com/legionattack.php?do=exit&v=3340&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.1&pvb=2015-09-25%2017%3A07%3A26&platformtype=1'
    data1 = '&Type=1&Id=' + str(legionId)
    data2 = '&Type=2&Id=' + str(legionId)
    jsonresponse = connection(url1, data1)
    jsonresponse = connection(url2, data2)



id = [['Am', '1592626', '279696', 'IggFdDB5eE6uERXL'],
      ['#Cm', '2014092692358474', '285154', 'IggFdDB5eE6uERXL'],
      ['Em', '2014121327096245', '288121', 'IggFdDB5eE6uERXL'],
      ['#Fm', '2015031960117052', '294557', 'IggFdDB5eE6uERXL'],

      ['jinxiaoxi', '2014011514924154', '289074', 'TqctVYyZJmA6JrGC'],
      ['jinxiaoxiaoxi', '2014021715652853', '265008', 'TqctVYyZJmA6JrGC'],
      ['jinxiaoxiaoxiaoxi', '2015010132895122', '289017', 'TqctVYyZJmA6JrGC'],
      ['jinxixi', '2015011837740716', '289647', 'TqctVYyZJmA6JrGC'],
      ['jinxiaoxixi', '2015013142224275', '290057', 'TqctVYyZJmA6JrGC'],
      ['hong', '2015052882084219', '296351', 'TqctVYyZJmA6JrGC'],
      ['cong', '2015052882088503', '296352', 'TqctVYyZJmA6JrGC'],
      ['feng', '2015052882090943', '296354', 'TqctVYyZJmA6JrGC'],
      ['yu', '2015052882090503', '296353', 'v1soiQ8I8RgIvg2p'],

      ['R0', '59079768', '289074', 'rgHAKkH6roUMGmeY'],
      ['Reao1st', '2014021515603023', '264491', '73gstGxATMy4UuUy'],
      ['Reao2nd', '2014040452624347', '289393', '73gstGxATMy4UuUy'],

      ['称霸候车亭','2015053082413554', '296380', 'Tzf013aAWWTkpUMF'],
      ['称霸便利店','2015060784933505', '296533', 'Tzf013aAWWTkpUMF'],
      ['称霸美食城','2015042572380319', '295655', 'Tzf013aAWWTkpUMF'],
      ['称霸茶餐厅','2015071912704523', '298101', 'Tzf013aAWWTkpUMF'],
      ['称霸扶桑省','2015080122554779', '298367', 'Tzf013aAWWTkpUMF'],
      ['称霸养老院','2015011537065337', '292571', 'Tzf013aAWWTkpUMF'],

      ['妙蛙种子', '2014052561883286', '278956', 'QcGtd5Hmsy3g7dS9'],
      ['绿毛虫', '2014061766465489', '278958', 'QcGtd5Hmsy3g7dS9'],
      ['大针蜂', '2014061866519659', '278984', 'QcGtd5Hmsy3g7dS9'],
      ['比比鸟', '2014061866519756', '278986', 'QcGtd5Hmsy3g7dS9'],
      ['超音蝠', '2014061866528941', '279006', 'QcGtd5Hmsy3g7dS9'],
      ['隆隆岩', '2014061866529032', '279007', 'QcGtd5Hmsy3g7dS9'],
      ['大岩蛇', '2014061866529097', '279009', 'QcGtd5Hmsy3g7dS9'],
      ['乘龙', '2014061866529223', '279045', 'QcGtd5Hmsy3g7dS9'],
      ['耿鬼', '2014061866529231', '279049', 'QcGtd5Hmsy3g7dS9'],
      ['烈焰马', '2014061866529288', '279053', 'QcGtd5Hmsy3g7dS9'],
      ['吸盘魔偶', '2014061866529337', '279054', 'QcGtd5Hmsy3g7dS9'],
      ['胖丁', '2014061866529346', '279080', 'QcGtd5Hmsy3g7dS9'],
      # ['阿柏蛇', '2014061866529379', '279081', 'QcGtd5Hmsy3g7dS9'],
      # ['椰蛋树', '2014061866529407', '279083', 'QcGtd5Hmsy3g7dS9'],
      # ['火爆猴', '2014061866529462', '279085', 'QcGtd5Hmsy3g7dS9'],
      # ['派拉斯', '2014061866529470', '279086', 'QcGtd5Hmsy3g7dS9'],
      # ['比雕', '2014061866529500', '279117', 'QcGtd5Hmsy3g7dS9'],
      # ['雷精灵', '2014061866529554', '279119', 'QcGtd5Hmsy3g7dS9'],
      # ['皮卡西', '2014061866529628', '279122', 'QcGtd5Hmsy3g7dS9'],
      # ['水精灵', '2014061866529641', '279131', 'QcGtd5Hmsy3g7dS9'],
      # ['火精灵', '2014061866529643', '279137', 'QcGtd5Hmsy3g7dS9'],
      # ['胡地', '2014061866529675', '279164', 'QcGtd5Hmsy3g7dS9'],
      # ['风速狗', '2014061866529735', '279165', 'QcGtd5Hmsy3g7dS9'],
      # ['喷火龙', '2014061866529744', '279166', 'QcGtd5Hmsy3g7dS9']
      ]

id1 = ['#Cm', '2014092692358474', '285154', 'IggFdDB5eE6uERXL']
# 先登录得到团战信息
con_log(*id1)
legionId = GetLegionInfo()
if legionId != -1:
    # 循环登录参战
    for id1 in id:
        con_log(*id1)
        legionattack(legionId)
else:
    print '今天没团战'
raw_input('The End')
