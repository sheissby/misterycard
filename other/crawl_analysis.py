# encoding: utf-8
from crawl_lagou import get_response as lg_get_response
from crawl_zhilian import get_response as zl_get_response


def clawl(spider, site):
    position_data = spider
    data = []
    for position in position_data:
        data.append(position)

    for level in ('min', 'avg', 'max'):
        salary = []
        sum = 0
        for info in data:
            salary.append(info['salary'][level])
        for i in salary:
            sum += i
        avg_salary = sum / len(salary)
        print('%s抓取%d个职位，平均%s薪资为%d' % (site, len(salary), level, avg_salary))


if __name__ == '__main__':
    clawl(lg_get_response(), '拉勾')
    clawl(zl_get_response(), '智联')
