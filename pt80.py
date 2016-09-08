# encoding: utf-8
import csv
import re
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.pt80.net/forum-232-'

page_pattern = re.compile(r'[0-9]+')
id_pattern = re.compile(r'normalthread_[0-9]+')

res_data = []  # 爬取结果集合

def gettotalpages():
    """获取总页数"""
    try:
        r = requests.post('http://www.pt80.net/forum-232-1.html')
        soup = BeautifulSoup(r.text, 'html.parser')
        totalpage = soup.find('div', class_='pg').find('label').find('span').text
        totalpage = (page_pattern.search(totalpage)).group()
        # print type(totalpage)
        print '共 % s 页' % str(totalpage)
    except Exception:
        print '获取总页数失败'
        exit()
    return totalpage


def parse(totalpage):
    """获取标签、标题及链接"""
    for page in range(1, totalpage+1):
        print 'start crawl page', page
        url = base_url + '%s' % page + '.html'
        html = requests.post(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        tbodys = soup.find_all('tbody', attrs={'id': id_pattern})
        for tbody in tbodys:
            try:
                tag = tbody.find('th').find('em').text
            except Exception:
                tag = ''
            finally:
                info = tbody.find('th').find('a', attrs={'class': 's xst'})
                title = info.text
                source_url = info['href']
                try:
                    data = (tag.encode('gbk'), title.encode('gbk'), source_url.encode('gbk'))
                except Exception:
                    print tag, title, source_url
                res_data.append(data)
    return res_data


def save2cvs(res_data):
    csvfile = file('pt80.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerows(res_data)
    csvfile.close()


if __name__ == '__main__':
    totalpage = gettotalpages()
    res_data = parse(int(totalpage))
    save2cvs(res_data)
