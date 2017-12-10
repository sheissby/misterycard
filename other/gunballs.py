# encoding: utf-8
import requests

url = 'http://wechat.leiting.com/weixin/gumballs/201610/gift/common/getGift.php'
param = 'type=1'
header = {
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          }
r = requests.post(url, data=param, headers=header)
print r.json()['message']