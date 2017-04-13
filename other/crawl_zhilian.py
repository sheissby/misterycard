# encoding: utf-8
from lxml import etree
import requests

base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%8c%97%e4%ba%ac&kw=%e6%b5%8b%e8%af%95'
position_info = []


def get_response():
    for page in range(1, 90):
        # print 'starting page %d' % page
        param = '&p=' + str(page)
        try:
            r = requests.get(url=base_url, params=param, timeout=10)
            if r.status_code == 200:
                tree = etree.HTML(r.text)
                tables = tree.xpath('//table[@class="newlist"]')
                for table in tables:
                    data = {}
                    salary_json = {}
                    a = table.xpath('tr/td[@class="zwmc"]/div/a')
                    if a:
                        position = a[0].xpath('string(.)')
                        url = a[0].xpath('@href')[0]
                        salary = table.xpath('tr/td[@class="zwyx"]/text()')[0]
                        company = table.xpath('tr/td[@class="gsmc"]/a[@target="_blank"]/text()')[0]
                        workplace = table.xpath('tr/td[@class="gzdd"]/text()')[0]
                        updatetime = table.xpath('tr/td[@class="gxsj"]/span/text()')[0]
                        if '-' in salary:
                            salary_json['max'] = int(str(salary).split('-')[1])
                            salary_json['min'] = int(str(salary).split('-')[0])
                            salary_json['avg'] = (salary_json['max'] + salary_json['min'])/2
                            data['position'] = position
                            data['salary'] = salary_json
                            data['workplace'] = workplace
                            data['company'] = company
                            data['url'] = url
                            position_info.append(data)
                            if salary_json['max'] > 10000:
                                print position, salary, workplace, company, url
                        elif salary == u'面议':
                            print position, salary, workplace, company, url
            else:
                print '第%d页' % page + r.status_code
        except Exception, e:
            print 'error：', e
    return position_info


if __name__ == '__main__':
    position_info = get_response()
