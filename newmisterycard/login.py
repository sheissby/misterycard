# encoding:utf-8
import requests
import json
import time
import ConfigParser
import sys
from id import *
from config import *

header = {"User-Agent": "Mozilla/5.0 (Android; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/22.0",
          "Content-Type": "application/x-www-form-urlencoded",
          "Cookie": "_sid=hr4oagbk53mg2n03eho66i4ro6"
          }

# 导入配置文件信息
curpath = sys.path[0]
initpath = curpath + '/init.conf'
config = ConfigParser.ConfigParser()
config.read(initpath)
threshold = config.get('threshold', 'threshold')
autofight = config.get('auto fight', 'autofight')
# ID = config.get('ID List', 'ID').replace('\n', '')
#
# id = ID.split(';')
# print id
# print type(id)

# 成功返回1和response信息，失败返回0和失败信息
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
                    print '登录失败'
                    time.sleep(1)
                else:
                    return 0, message
        except Exception:
            status = 0
            time.sleep(1)
    return 1, jsonresponse


# 循环直到成功才返回，只返回response
def connectionuntilsuccess(url, data):
    status = 0
    while status == 0:
        try:
            response = requests.post(url, data=data, headers=header)
            jsonresponse = json.loads(response.content)
            status = jsonresponse.get('status', 0)
            if 'returnObjs' in jsonresponse:
                return jsonresponse
            if status == 0:
                message = jsonresponse.get('message', 0)
                if message == '':
                    print '登录失败'
                    time.sleep(1)
        except Exception, e:
            print e
            status = 0
            time.sleep(1)
    return jsonresponse


def login(id):
    username = id[1]
    password = id[2]
    # 第一条报文
    url = loginurl
    data = '{"serviceName":"checkUserActivedJson",' \
           '"callPara":{"clientType":"android",' \
           '"releaseChannel":"androidChannel",' \
           '"locale":"CHS",' \
           '"userName":"'+ username+'",' \
           '"userPassword":"'+ password +'",' \
           '"gameName":"CARD-ANDROID-CHS",' \
           '"udid":"18:44:98:53:03:AA",' \
           '"idfa":""}}'
    code = 1
    while code != 0:
        jsonresponse = connectionuntilsuccess(url, data)
        code = int(jsonresponse['returnCode'])

    # 处理返回值
    returnObj = jsonresponse['returnObjs']
    source = str(returnObj['source'])
    timestamp = str(returnObj['timestamp'])
    GS_CHAT_IP = str(returnObj['GS_CHAT_IP'])
    userName = str(returnObj['userName'])
    U_ID = str(returnObj['U_ID'])
    G_TYPE = str(returnObj['G_TYPE'])
    GS_DESC = returnObj['GS_DESC'].encode('utf-8')
    friendCode = str(returnObj['friendCode'])
    key = str(returnObj['key'])
    GS_CHAT_PORT = str(returnObj['GS_CHAT_PORT'])
    GS_IP = str(returnObj['GS_IP'])
    GS_NAME = str(returnObj['GS_NAME'])

    # 第二条报文
    data = 'PP%5FuEmailState=0&Udid=44%3A37%3AE6%3A63%3AF0%3AA3&newguide=1&PP%5FG%5FTYPE=' + G_TYPE + \
           '&PP%5FGS%5FCHAT%5FPORT=' + GS_CHAT_PORT + '&Devicetoken=&PP%5FGS%5FNAME=' + GS_NAME + '&IDFA=&Origin=com' \
           '&PP%5FGS%5FPORT=80&ppgamename=CARD%2DANDROID%2DCHS&PP%5FfriendCode=' + friendCode + '&PP%5FGS%5FDESC=' + GS_DESC + \
           '&PP%5FGS%5FCHAT%5FIP=' + GS_CHAT_IP + '&PP%5FGS%5FIP=' + GS_IP + '&PP%5FuserName=' + userName + '&UserName=' + userName + \
           '&Password=' + U_ID + '&PP%5FU%5FID=' + U_ID + '&PP%5Fsource=' + source + '&PP%5Ftimestamp=' + timestamp + \
           '&time=' + timestamp + '&key=' + key + '&PP%5Fkey=' + key
    url = host + '/login.php?do=PassportLogin&v=1002&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    jsonresponse = connectionuntilsuccess(url, data)
    # print id[0], 'login success'


# 验证账号所在军团，在白名单返回1，不在返回0
def verification(id):
    login(id)
    if isverification.lower() != 'false':
        url = host + '/legion.php?do=GetLegions&v=1001&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
        data = 'Amount=10&Start=0'
        jsonresponse = connectionuntilsuccess(url, data)
        legionid = jsonresponse.get('data').get('MyInfo').get('LegionId')
        if legionid == '688':
            return 1
        else:
            print '请并更此账号所在军团'
            return 0
    else:
        return 1

def mapstage(id):
    if verification(id) == 1:
        mapid = 1
        flg = 0
        url = host + '/mapstage.php?do=Explore&v=1002&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
        data = "MapStageDetailId=" + str(mapid)
        while flg == 0:
            flg, jsonresponse = connection(url, data)
            # 探索成功
            if flg != 0:
                # 判断出现盗贼
                try:
                    jsonresponse = jsonresponse.get('data')
                except Exception:
                    print 'unknown error'
                if 'ThievesInfo' in jsonresponse:
                    try:
                        Type = jsonresponse.get('ThievesInfo', 0).get('Type', 0)
                        userthievesid = jsonresponse.get('ThievesInfo', 0).get('UserThievesId', 0)
                        if Type == 2:
                            print id[0], 'appear elite thief!!!'
                        if Type == 1:
                            print id[0], 'appear normal thief'
                        return userthievesid
                    except Exception:
                        print 'unknown error'
                        return 0
                # 未出现盗贼
                else:
                    flg = 0
            else:
                if jsonresponse == u'行动力不足!每10分钟可恢复1点!您也可以使用晶钻购买行动力哦!':
                    print id[0], 'out of power!'
                    return 0
                if jsonresponse == u'关卡尚未开启!':
                    print id[0], jsonresponse
                    return 0
                else:
                    # print id1[0], 'unknown error, continue exploring'
                    time.sleep(1)
                    flg = 0
    else:
        return 0
if __name__ == '__main__':
    ids = Amid()
    mapstage(id)