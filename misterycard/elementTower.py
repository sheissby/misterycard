# encoding: utf-8
from con_log import *

class ElementTower(object):
    def __init__(self):
        self.cseat = 9
        self.target =[]

    def getTeamId(self, did):
        url = host + '/towerdup.php?do=GetTeamId&v=5656&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        data = 'did=' + str(did)
        flag = 0
        while flag == 0:
            try:
                jsonresponse = connection(url, data)
                flag = jsonresponse[0]
                tid = jsonresponse[1].get('data').get('tid')
            except:
                print 'get TeamId error'
        return tid

    def intower(self, did, tid):
        url  = host + '/towerdup.php?do=InTower&v=5657&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        # tid = 23191 & uids = 105009 & did = 4
        data = 'tid=' + str(tid) + '&uids=105009&did=' + did
        jsonresponse = connection(url, data)
        flag = jsonresponse[0]
        tid = jsonresponse[1].get('data').get('tid')

    def move(self, direction, tid, did):
        # 初始位置
        # did = 4 & tid = 23191 & nseat = 7 & type = 1 & cseat = 8
        if direction == 'up':
            nseat = self.cseat - 9
            data = 'did='+ str(did) + '&tid=' + str(tid) + '&nseat=' + str(nseat) + '&type=1&cseat=' + str(self.cseat)
        elif direction == 'down':
            nseat = self.cseat + 9
            data = 'did='+ str(did) + '&tid=' + str(tid) + '&nseat=' + str(nseat) + '&type=1&cseat=' + str(self.cseat)
        elif direction == 'left':
            print 'move left'
            nseat = self.cseat - 1
            data = 'did='+ str(did) + '&tid=' + str(tid) + '&nseat=' + str(nseat) + '&type=1&cseat=' + str(self.cseat)
            print data
        elif direction == 'right':
            print 'move right'
            nseat = self.cseat + 1
            data = 'did='+ str(did) + '&tid=' + str(tid) + '&nseat=' + str(nseat) + '&type=1&cseat=' + str(self.cseat)
            print data
        url = host + '/towerdup.php?do=Move&v=5661&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        jsonresponse = connection(url, data)
        print jsonresponse
        status = jsonresponse[1].get('status')
        print 'status'%s %status
        print nseat
        return nseat

    def fight(self, siteid):
        # tid=23191&siteid=8&did=4
        url = host + '/towerdup.php?do=Battle&v=5954&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        data = ''

    def revive(self, did, tid):
        # tid=23656&type=2&did=2
        url = host + '/towerdup.php?do=Revive&v=5958&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.8.1&pvb=2016-04-12%2009%3A53%3A52&platformtype=1'
        data = ''
        cseat = 8



if __name__ == '__main__':
    id = ['Am', '1592626', '279696', 'ZmeyMlMTIaQoo1vn']
    did = '2'
    con_log(*id)
    et = ElementTower()
    tid = et.getTeamId(did)

    # 进塔
    et.intower(did, tid)
    for i in range (1,10):
        print '='*20,i
        et.cseat = et.move('left', tid, did)
        time.sleep(1)
        et.cseat = et.move('right', tid, did)
        time.sleep(1)
