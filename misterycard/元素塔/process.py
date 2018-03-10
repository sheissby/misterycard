# encoding: utf-8
import re
from action import *
import requests
import json
import time
from login import con_log
from login import connection

##地图信息类
class map_info:
    WallRows=[]
    WallCols=[]
    #Monster=[]
    #Monster_Sort=[]
    grids=[]
    begin_pos=9
    kill_count=0
    monster_alive=14
    finished=0
    current_pos=9
    tid='0'
    
    ##建立房间
    def build_map(self,tower_id,*id):
        #print type(id[0]),id
        con_log(*id)
        y=build_room(tower_id)
        #print y        
        self.tid=str(y.get('data',0).get('tid',0))       

    ##刷新地图
    def init_map(self,tower_id,*id):
        '''
        con_log(*id)
        y=build_room(tower_id)
        #print y        
        tid=str(y.get('data',0).get('tid',0))
        '''
        uids=id[4]
        #print self.tid,tower_id,uids
        #init_tower(tower_id,self.tid,uids)
        z=init_tower(tower_id,self.tid,uids)
        #print z
        
        self.WallRows=z.get('data',0).get('WallRows',0)[:]
        self.WallCols=z.get('data',0).get('WallCols',0)[:]
        #Monster=z.get('data',0).get('Monster',0).keys()[:]
        self.grids=z.get('data',0).get('Grids',0)[:]
        print "grids:"
        print self.grids
        self.finished=z.get('data',0).get('IsFinish',0)

    ##查看地图通关状态
    def update_finished(self,finish_label):
        self.finished=finish_label
        self.monster_alive=self.monster_alive-1

    ##更新当前位置
    def update_pos(self,cord):
        self.current_pos=cord

    ##按自然顺序找寻下一个目标怪物作为备选，不一定是下一个攻击目标【实际攻击目标是离当前位置最近的怪物】
    def get_pathcord(self):
        target = -1
        for i in range(0,50):
            if self.grids[i] in range(5,9):
                target = i
        return self.current_pos,target

    ##判断坐标上面是否是怪物
    def check_monster(self,cord):
        if (self.grids[cord] in range(5,9)):
            return 1
        else :
            return 0

##记录每次攻击的行军路径【作为记录点和路径的数据结构存在，如果需要记录更多信息，可以在此类中添加元素】    
class path_to_v:
    length=0
    path=[]

##路径计算类
class path_info:
    ##利用迪克斯特拉算法求离当前位置最近的怪物，并记录路径
    def GetPath(self,a,b,mapinfo):
        dist=[]
        start_pos=a;
        print "start point:"+str(start_pos)
        for i in range(0,50):
            dist.append(path_to_v())
            dist[i].length=self.check_direct(a,i,mapinfo)
            if (a==i):
                dist[i].length=0
                #dist[i].path.append(i)
        S=[]
        for i in range(0,50):
            v=9
            min=100
            for j in range(0,50):
                if (dist[j].length<min and j not in S):
                    v=j;min=dist[j].length
                    #print v,min,dist[v].path
            S.append(v)
            if(v==b or mapinfo.check_monster(v)==1): dist[v].path.append(v);return dist[v]
            for j in range(0,50):
                if (dist[j].length>=min+self.check_direct(v,j,mapinfo) and j not in S):
                    dist[j].length=min+self.check_direct(v,j,mapinfo)
                    #del dist[j].path[:]
                    dist[j].path=dist[v].path[:];dist[j].path.append(v)

    ##调用计算路径函数，返回求得的下一次行军路径                
    def campaign(self,map_info):
        a,b=map_info.get_pathcord()
        print u'目标是'+str(a)+" to "+str(b)
        #del path[:]
        #del path_tmp[:]
        path_detail=self.GetPath(a,b,map_info)
        print u"path from a to b: ", path_detail.length, path_detail.path
        return path_detail.path

    ##4个方向是否可以进行移动的判断
    def check_direct(self,a,b,map_info):
        if (b==a+10 and map_info.WallCols[(a%10)*4+a/10]!=1):
            return 1
        if (b==a-10 and map_info.WallCols[(b%10)*4+b/10]!=1):
            return 1
        if (b==a+1 and (a%10)!=9 and map_info.WallRows[(a%10)+(a/10)*9]!=1):
            return 1
        if (b==a-1 and (b%10)!=9 and map_info.WallRows[(b%10)+(b/10)*9]!=1):
            return 1
        return 100

    ##预留的出界判断，未启用
    def check_valid(self,cord):
        if cord>49 or cord<0: return 0
        return 1

##攻击函数，实施下一次怪物攻击行动并根据攻击结果进行处理
def attack(path,mapinfo,tower_id,*id):
    if (len(path)<2):
        print u'路径有误'
        return -1
    ##进行位置移动
    for i in range (0,len(path)-2):
        move_check = move(str(path[i]),str(path[i+1]),tower_id,mapinfo.tid)
        #print move_check
        if (isinstance(move_check,unicode) or move_check.get('status',0)!=1):
            time.sleep(15)
            move_check = move(str(path[i]),str(path[i+1]),tower_id,mapinfo.tid)
            #print move_check
            
    print u"target： "+str(path[-1])+u" & tid："+mapinfo.tid
    ##移动到位，攻击身边怪物
    result = battle(str(path[-1]),tower_id,mapinfo.tid)
    #print result
    if (isinstance(result,unicode)):
        print result
        time.sleep(15)
        result = battle(str(path[-1]),tower_id,mapinfo.tid)
    time.sleep(15)

    ##根据输赢进行下一步处理方式
    if (result.get('data',0).get('Win',0)!=2):
        print "kill the monster at "+str(path[-1])
        mapinfo.init_map(tower_id,*id)
        mapinfo.update_pos(path[-1])
        #mapinfo.update_finished(result.get('data',0).get('IsFinish',0))
        print "finished is "+str(mapinfo.finished)
        #print "monster rest is "+str(mapinfo.monster_alive)
        print "position now："+str(mapinfo.current_pos)
        return mapinfo.current_pos
    else:
        print "attack failed"
        mapinfo.init_map(tower_id,*id)
        mapinfo.update_pos(9)
        retrieve(tower_id,mapinfo.tid)
        print "position now："+str(mapinfo.current_pos)
        return mapinfo.current_pos

'''--test function--
tower_info = map_info()
tower_info.build_map("1",*id)
tower_info.init_map("1",*id)
print tower_info.WallRows,tower_info.WallCols,tower_info.grids
compute = path_info()
path=compute.campaign(tower_info)
attack(path,tower_info,"1",*id)
path=compute.campaign(tower_info)
attack(path,tower_info,"1",*id)
'''


