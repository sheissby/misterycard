# encoding: utf-8
import json
import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from peewee import *
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
base_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'
header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
          'User-Agent': 'Mozilla/5.0(Windows NT 6.3;WOW64;rv:52.0) Gecko / 20100101Firefox / 52.0',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'X-Requested-With': 'XMLHttpRequest',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
          'Referer': 'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput='
          }
db = MySQLDatabase(host='localhost', port=3305, user='root', passwd='', database='job')
i = 1 # 记录条数

class origin(Model):
    position_name = CharField(50)
    salary_min = IntegerField()
    salary_max = IntegerField()
    workpositon = CharField(50)
    education = CharField(20)
    workExp = CharField(10)
    updatetime = CharField(50)
    company = CharField(50)
    company_field = CharField(500)
    url = CharField(500)

    class Meta:
        database = db


def request(page):
    try:
        s = requests.session()
        r = s.post(url=base_url, data=page, headers=header, verify=False)
        if r.status_code == 200:
            res = json.loads(r.content)
            return res
    except requests.HTTPError, e:
        print '请求错误：', e
    finally:
        pass


def parse(html):
        position_list = html['content']['positionResult']['result']
        for positioninfo in position_list:
            global i
            print '开始解析第%d条' % i
            data = {}
            salary_json = {}
            position_name = positioninfo['positionName']
            company = positioninfo['companyShortName']
            workExp = positioninfo['workYear']
            education = positioninfo['education']
            updatetime = positioninfo['createTime']
            company_field = positioninfo['industryField']
            id = positioninfo['positionId']
            url = 'https://www.lagou.com/jobs/%d.html' % id
            salary = positioninfo['salary']
            if '-' in salary:
                salary_json['min'] = int(str(salary).lower().replace('k', '').split('-')[0])*1000
                salary_json['max'] = int(str(salary).lower().replace('k', '').split('-')[1])*1000
                salary_json['avg'] = (salary_json['min'] + salary_json['max'])/2
            else:
                salary_json['min'] = salary_json['max'] = salary_json['avg'] = int(str(salary).lower().replace('k', ''))*1000

            workpositon = positioninfo['businessZones']
            if workpositon:
                workplace = workpositon[0]
            else:
                workplace = 'NULL'

            data['position_name'] = position_name
            data['salary'] = salary_json
            data['workplace'] = workplace
            data['company'] = company
            data['url'] = url
            data['workExp'] = workExp
            data['education'] = education
            data['updatetime'] = updatetime
            data['company_field'] = company_field
            data['salary'] = salary_json

            SavetoDB(data, i)
            i += 1


def SavetoDB(data, i):
    print '开始写入第%d条' % i
    db.connect()
    origin.create(position_name=data['position_name'],
                  salary_min=data['salary']['min'],
                  salary_max=data['salary']['max'],
                  workplace=data['workplace'],
                  education=data['education'],
                  workExp=data['workExp'],
                  updatetime=data['updatetime'],
                  company=data['company'],
                  company_field=data['company_field'],
                  url=data['url'],
                  )
    db.close()

if __name__ == '__main__':
    for page in range(0, 10):  # curPage=0是第一页
        print '开始抓取第%d页' % (page+1)
        param = 'first=true&kd=%e9%ab%98%e7%ba%a7%e6%b5%8b%e8%af%95%e5%b7%a5%e7%a8%8b%e5%b8%88&pn=' + str(page)
        html = request(param)
        parse(html)
        time.sleep(5)
