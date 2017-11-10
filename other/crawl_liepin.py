# encoding: utf-8
import requests
from lxml import etree

base_url = 'https://www.liepin.com/zhaopin/?pubTime=&ckid=8060c2f683231502&fromSearchBtn=2&compkind=&isAnalysis=&init=-1&searchType=1&dqs=010&industryType=&jobKind=&sortFlag=15&degradeFlag=0&industries=&salary=&compscale=&key=%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95&clean_condition=&headckid=8060c2f683231502'

position_info = []

def get_response():
    for page in range(0, 29):   # curPage=0是第一页
        # print 'starting page %d' % page
        param = '&curPage=' + str(page)
        try:
            r = requests.get(url=base_url, params=param, timeout=10)
            if r.status_code == 200:
                tree = etree.HTML(r.content)
                divs = tree.xpath('//div[@class="sojob-item-main clearfix"]')
                for div in divs:
                    data = {}
                    salary_json = {}
                    position_name = div.xpath('div[@class="job-info"]/h3/a')[0].text
                    position_name = position_name.encode('utf-8').strip()
                    position_detail = div.xpath('div[@class="job-info"]/p[@class="condition clearfix"]')[0].attrib['title'].encode('utf-8').split('_')
                    salary = position_detail[0]
                    workpositon = position_detail[1]
                    education = position_detail[2]
                    workExp = position_detail[3]
                    updatetime = div.xpath('div[@class="job-info"]/p[@class="time-info clearfix"]/time')[0].text
                    company = div.xpath('div[@class="company-info nohover"]/p[@class="company-name"]/a')[0].text
                    company_field = div.xpath('div[@class="company-info nohover"]/p[@class="field-financing"]/span/a')[0].text
                    tag = div.xpath('div[@class="company-info nohover"]/p[@class="temptation clearfix"]/span')
                    tags = [str(x) for x in tag]

                    if '-' in salary:
                        salary_json['max'] = int(str(salary[0:3]).split('-')[1])*10000/12
                        salary_json['min'] = int(str(salary[0:3]).split('-')[0])*10000/12
                        salary_json['avg'] = (salary_json['max'] + salary_json['min']) / 2
                        data['position_name'] = position_name
                        data['workpositon'] = workpositon
                        data['education'] = education
                        data['workExp'] = workExp
                        data['updatetime'] = updatetime
                        data['company'] = company
                        data['company_field'] = company_field
                        data['tags'] = tags
                        position_info.append(data)

            else:
                print '第%d页' % page + r.status_code
        except Exception, e:
            print 'error：', e
    return position_info


if __name__ == '__main__':
    position_info = get_response()