# encoding: utf-8
from con_log import *

# Cards=6651503
#       9760567
header = {'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': '_sid=27vjshsgsfpsglp14ts5hba4s5'}
id = ['#Cm', '2014092692358474', '285154', 'ZmeyMlMTIaQoo1vn']
con_log(id)
url = 'http://s1.xiaomi.mysticalcard.com/evolution.php?do=SetSkill&v=1522&phpp=ANDROID_XIAOMI&phpl=ZH_CN&pvc=1.7.0&pvb=2015-07-16%2017%3A02%3A55&platformtype=null'
data = 'UserCardId2=10600167&SkillId=411&UserCardId1=10595969'
r = requests.post(url,data, header)
res =json.loads(r.content)
print res