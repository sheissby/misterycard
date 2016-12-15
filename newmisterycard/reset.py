# encoding:utf-8
from Login import *


def reset_tower(id):
    if verification(id) == 1:
        for tower_id in [8, 7, 6]:
            url = host + '/maze.php?do=Reset&v=6389&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
            data = "MapStageId=" + ('%d' % tower_id)
            isreset = towerstatus(data)
            if isreset == 1:
                jsonresponse = connectionuntilsuccess(url, data)
            else:
                continue


def towerstatus(data):
    url = host + '/maze.php?do=Show&v=6389&phpp=ANDROID&phpl=ZH_CN&pvc=1.9.0&pvb=2016-08-02%2015%3A37%3A49&platformtype=1'
    jsonresponse = connectionuntilsuccess(url, data)
    whetherReset = jsonresponse['data']['FreeReset']
    return whetherReset

ids = Cmid()
for id in ids:
    reset_tower(id)
    time.sleep(1)
# raw_input('End')
