# encoding: utf-8
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
base_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
          'User-Agent': 'Mozilla/5.0(Windows NT 6.3;WOW64;rv:52.0) Gecko / 20100101Firefox / 52.0',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'X-Requested-With': 'XMLHttpRequest',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
          }
cookie = {'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1489998933,1490166877,1490338286',
          '_ga': 'GA1.2.484959430.1486199222',
          'user_trace_token': '20170204170702-4a8ffeaa-eab9-11e6-9116-525400f775ce',
          'LGUID': '20170204170702-4a90036c-eab9-11e6-9116-525400f775ce',
          'index_location_city': '%E5%8C%97%E4%BA%AC',
          'JSESSIONID': '3CBBD0FC92A9DE5EE6502546E855ED42',
          'TG-TRACK-CODE': 'index_navigation',
          'SEARCH_ID': 'ccf59909591444f2a97be5f1dae28a1a',
          '_gat': '1',
          'LGSID': '20170324145125-4c896f10-105e-11e7-9566-5254005c3644',
          'PRE_UTM': '',
          'PRE_HOST': '',
          'PRE_SITE': 'https%3A%2F%2Fwww.lagou.com%2F',
          'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2Fceshi%2F%3FlabelWords%3Dlabel',
          'LGRID': '20170324145125-4c89707f-105e-11e7-9566-5254005c3644',
          'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1490338286'
          }
position_info = []


def get_response():
    for page in range(1,31):
        # print 'starting page %d' % page
        param = 'first=true&kd=%E6%B5%8B%E8%AF%95&pn=' + str(page)
        try:
            s = requests.session()
            r = s.post(url=base_url, data=param, headers=header, verify=False, cookies=cookie)
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
