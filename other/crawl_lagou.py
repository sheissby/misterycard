# encoding: utf-8
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
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
position_info = []


def get_response():
    for page in range(1,31):
        # print 'starting page %d' % page
        param = 'first=true&kd=%E6%B5%8B%E8%AF%95&pn=' + str(page)
        try:
            s = requests.session()
            r = s.post(url=base_url, data=param, headers=header, verify=False)
            if r.status_code == 200:
                res = json.loads(r.content)
                position_list = res['content']['positionResult']['result']
                for positioninfo in position_list:
                    data = {}
                    salary_json = {}
                    position = positioninfo['positionName']
                    company = positioninfo['companyShortName']
                    workyear = positioninfo['workYear']
                    id = positioninfo['positionId']
                    url = 'https://www.lagou.com/jobs/%d.html' % id
                    salary = positioninfo['salary']
                    if '-' in salary:
                        salary_json['min'] = int(str(salary).lower().replace('k', '').split('-')[0])*1000
                        salary_json['max'] = int(str(salary).lower().replace('k', '').split('-')[1])*1000
                        salary_json['avg'] = (salary_json['min'] + salary_json['max'])/2
                    else:
                        salary_json['min'] = salary_json['max'] = salary_json['avg'] = int(str(salary).lower().replace('k', ''))*1000

                    businessZones = positioninfo['businessZones']
                    if businessZones:
                        workplace = businessZones[0]
                    else:
                        workplace = '地点未知'
                    print position, workyear, salary, workplace, company, url
                    data['position'] = position
                    data['salary'] = salary_json
                    data['workplace'] = workplace
                    data['company'] = company
                    data['url'] = url
                    data['workyear'] = workyear
                    position_info.append(data)
            else:
                print '第%d页' % page + r.status_code
        except Exception, e:
            print 'error：', e
    return position_info


if __name__ == '__main__':
    position_info = get_response()
