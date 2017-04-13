# encoding: utf-8
from crawl_lagou import get_response as lg_get_response
from crawl_zhilian import get_response as zl_get_response


def data(crawler, site):
    position_data = crawler
    data = []
    for position in position_data:
        data.append(position)

    salary = []
    sum = 0
    for info in data:
        salary.append(info['salary']['avg'])
    for i in salary:
        sum += i
    avg_salary = sum / len(salary)
    print '%s抓取%d个职位，平均薪资为%d' % (site, len(salary), avg_salary)


if __name__ == '__main__':
    data(lg_get_response, '拉勾')
    data(zl_get_response, '智联')
