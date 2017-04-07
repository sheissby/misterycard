# encoding: utf-8
from lxml import etree
import requests


def get_response():
    for page in range(1, 90):
        # print 'starting page %d' % page
        param = '&p=' + str(page)
        # try:
        r = requests.get(url=base_url, params=param)
        if r.status_code == 200:
            tree = etree.HTML(r.text)
            tables = tree.xpath('//table[@class="newlist"]')
            for table in tables:
                a = table.xpath('tr/td[@class="zwmc"]/div/a')
                if a:
                    position = a[0].xpath('string(.)')
                    url = a[0].xpath('@href')[0]
                    salary = table.xpath('tr/td[@class="zwyx"]/text()')[0]
                    company = table.xpath('tr/td[@class="gsmc"]/a[@target="_blank"]/text()')[0]
                    workplace = table.xpath('tr/td[@class="gzdd"]/text()')[0]
                    updatetime = table.xpath('tr/td[@class="gxsj"]/span/text()')[0]
                    if '-' in salary:
                        MaxSalary = str(salary).split('-')[-1]
                        if int(MaxSalary) > 10000:
                            print position, salary, company, workplace, url
                    elif salary == u'面议':
                        print position, salary, company, workplace, url
                    data = {position, salary, company, workplace, url}
                    position_info.append(data)
        else:
            print '第%d页' % page + r.status_code
        # except Exception, e:
        #     print 'error：', e
        #     print salary
    return position_info


if __name__ == '__main__':
    base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%8c%97%e4%ba%ac&kw=%e6%b5%8b%e8%af%95'
    position_info = []
    position_info = get_response()
