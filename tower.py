# encoding:GBK
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
                    # print message
                    return message
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


# ���ÿ����Ϣ
def getlayerinfo(layer, map_id):
    item = []   # ��Ҫ�����ĸ��Ӽ���
    count = 0   # ������Ӻ�
    data = "Layer=" + ('%d' % layer) + '&MapStageId=' + ('%d' % map_id)
    print ('%d' % map_id), '��' + ('%d' % layer), '��'
    url = 'http://s1.xiaomi.mysticalcard.com/maze.php?do=Info&v=8995&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1'
    jsonresponse = connection(url, data)
    if jsonresponse == u'��һ���Թ���û������!':
        return
    elif jsonresponse == u'�Թ���δ����.':
        return
    else:
        items = jsonresponse.get('data', 0).get('Map', 0).get('Items', 0)  # ���и��ӵ���Ϣ
        for cords in items:                            # ѭ�����и��ӣ������Ҫ��������Ϣ
            cords = int(cords)
            if cords == 2 or cords == 3 or cords == 5:
                item.append(count)                       # ��Ӹ��Ӻŵ���������
            count += 1                           # ������Ҫ�����ĸ��Ӻ�
        return item


# ���й���
def fight(layer, map_id, item):
    for cord in item:
        fightdata = "Layer=" + ('%d' % layer) + "&ItemIndex=" + ('%d' % cord) + "&manual=0&OpenCardChip=1" + "&MapStageId=" + ('%d' % map_id)
        url = 'http://s1.xiaomi.mysticalcard.com/maze.php?do=Battle&v=8996&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=1'
        jsonresponse = connection(url, fightdata)
        if jsonresponse == u'�ж�������!ÿ10���ӿɻָ�1��!��Ҳ����ʹ�þ��깺���ж���Ŷ!':
            print ('out of power!')
            return 0


# ѭ��ˢ��
def play_tower(*id1):
    for map_id in [8, 7, 6]:
        for layer in range(1, 6):
            con_log(*id1)
            item = getlayerinfo(layer, map_id)
            if item:
                try:
                    fightresult = fight(layer, map_id, item)
                    if fightresult == 0:
                        return
                except Exception:
                    fightresult = fight(layer, map_id, item)
                    if fightresult == 0:
                        return



id = [
      ['������콢','2013042910219954', '132168', 'hk8URzaHObkJbp0r'], ['�����Ѳ��','2013050510338482', '138002', 'hk8URzaHObkJbp0r'],
      ['���������','2013051110431066', '144222', 'hk8URzaHObkJbp0r'], ['����Ż�����','2013072911496244', '213117', 'hk8URzaHObkJbp0r'],
      ['������ڽ�','2013072911496578', '213119', 'hk8URzaHObkJbp0r'], ['�����Ǳˮͧ','2013082111852712', '223399', 'hk8URzaHObkJbp0r'],
      ['�����޼ʵ���','2013110613340617', '244513', 'hk8URzaHObkJbp0r'], ['���轢�����ݶ�','2013112813880389', '249308', 'hk8URzaHObkJbp0r'],
      ['���轢�����ݶ�','2013112813880397', '249307', 'hk8URzaHObkJbp0r'], ['���轢�����ݶ�','2013112813880401', '249306', 'hk8URzaHObkJbp0r'],
      ['���轢�Ӷ��ݶ�','2013112813880408', '249303', 'hk8URzaHObkJbp0r'], ['���轢��һ�ݶ�','2013112813880415', '249301', 'hk8URzaHObkJbp0r'],
      ['���轢�����ݶ�','2013112813880453', '249274', 'hk8URzaHObkJbp0r'], ['�����ս�н�','2013112813880485', '249258', 'hk8URzaHObkJbp0r'],
      ['���轢�����ݶ�','2013112813892037', '249363', 'hk8URzaHObkJbp0r']
      ]
for id1 in id:
    print id1[0], 'start'
    play_tower(*id1)
    print id1[0], 'end'
raw_input('The End')
