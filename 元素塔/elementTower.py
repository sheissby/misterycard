# encoding: utf-8
import re
from action import *
from process import *
import requests
import json
import time
from login import con_log
from login import connection
from datetime import datetime


def Do_ET():
    print "account_info format : "+"[ uid,Muid,session_id,name,uuid ] (a list of 5 param)"
    print "account_info sample : ['2016050102644564','305747','VGgBD3sdZQidpx41','king','109500']"
    mainid = input("please input your account_info :  ")
    if(type(mainid)!=list):
        print "baga ： this is not a list"
        raw_input('The End')
        return 0
    if(len(mainid)!=5):
        print "pig ： list length is not 5"
        raw_input('The End')
        return 0
    name = mainid[3]
    print u"choose the begin tower : 1.从水塔开始 2.从风塔开始 3.从火塔开始 4.只刷地塔"
    begin_tow = input("please input your choice number :  ")
    print name, 'start'
    for i in range(begin_tow,5):
        begin_time=datetime.now()
        tower_id=str(i)
        con_log(*mainid)
        #con_log(*id1)
        tower_info = map_info()
        tower_info.build_map(tower_id,*mainid)
        tower_info.init_map(tower_id,*mainid)
        print tower_info.WallRows,tower_info.WallCols,tower_info.grids
        while 1:
            compute = path_info()
            path=compute.campaign(tower_info)
            attack(path,tower_info,tower_id,*mainid)
            if (tower_info.finished!=0):
                print "tower "+tower_id+" is done"
                time.sleep(5)
                award=getaward(tower_id,tower_info.tid)
                print award
                break
        #con_log(*id1)
        con_log(*mainid)
        end_time=datetime.now()
        print u"元素塔"+tower_id+u"用时："+str((end_time-begin_time).seconds)
    print name, 'end'
    raw_input('The End')

Do_ET()        
