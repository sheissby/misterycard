# encoding: utf-8
import requests
from lxml import etree
from peewee import *

i = 1 # 记录条数
base_url = 'https://www.liepin.com/zhaopin/?pubTime=&ckid=8060c2f683231502&fromSearchBtn=2&compkind=&isAnalysis=&init=-1&searchType=1&dqs=010&industryType=&jobKind=&sortFlag=15&degradeFlag=0&industries=&salary=&compscale=&key=%e9%ab%98%e7%ba%a7%e6%b5%8b%e8%af%95%e5%b7%a5%e7%a8%8b%e5%b8%88&clean_condition=&headckid=8060c2f683231502'
db = MySQLDatabase(host='localhost', port=3305, user='root', passwd='', database='job')


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

    class Meta:
        database = db


def request(page):
    try:
        r = requests.get(url=base_url, params=page, timeout=10)
        if r.status_code == 200:
            return r.content
    except requests.HTTPError, e:
        print '请求错误：', e
    finally:
        pass


def parse(html):
    tree = etree.HTML(html)
    divs = tree.xpath('//div[@class="sojob-item-main clearfix"]')
    for div in divs:
        data = {}
        salary_json = {}
        position_name = div.xpath('div[@class="job-info"]/h3/a')[0].text
        position_name = position_name.encode('utf-8').strip()
        position_detail = div.xpath('div[@class="job-info"]/p[@class="condition clearfix"]')[0].attrib['title'].encode('utf-8').split('_')
        salary = position_detail[0]
        if '-' in salary:
            global i
            print '开始解析第%d条' % i
            salary = salary[:-3].strip()
            salary_json['max'] = int(salary.split('-')[1])*10000/12
            salary_json['min'] = int(salary.split('-')[0])*10000/12
            salary_json['avg'] = (salary_json['max'] + salary_json['min']) / 2
            workpositon = position_detail[1]
            education = position_detail[2]
            workExp = position_detail[3]
            updatetime = div.xpath('div[@class="job-info"]/p[@class="time-info clearfix"]/time')[0].text
            company = div.xpath('div[@class="company-info nohover"]/p[@class="company-name"]/a')[0].text
            try:
                company_field = div.xpath('div[@class="company-info nohover"]/p[@class="field-financing"]/span/a')[0].text
            except:
                company_field = \
                div.xpath('div[@class="company-info nohover"]/p[@class="field-financing"]/span')[0].text
            data['position_name'] = position_name
            data['workpositon'] = workpositon
            data['education'] = education
            data['workExp'] = workExp
            data['updatetime'] = updatetime
            data['company'] = company
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
                  workpositon=data['workpositon'],
                  education=data['education'],
                  workExp=data['workExp'],
                  updatetime=data['updatetime'],
                  company=data['company'],
                  company_field=data['company_field']
                  )
    db.close()


if __name__ == '__main__':
    for page in range(0, 10):  # curPage=0是第一页
        print '开始抓取第%d页' % (page+1)
        param = '&curPage=' + str(page)
        html = request(param)
        parse(html)
