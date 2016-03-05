#coding=utf8
import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime

# 保存到本地Sqlite
# def saveToSqlite(lesson_info):
#     # 获取lesson_info字典中的信息
#     name = lesson_info['name']
#     link = lesson_info['link']
#     des = lesson_info['des']
#     number = lesson_info['number']
#     time = lesson_info['time']
#     degree = lesson_info['degree']
#
#     # 连接数据库并插入相应数据
#     con = sqlite3.connect("lesson.db")
#     cur = con.cursor()
#     sql = "insert into lesson_info values ('%s', '%s','%s','%s','%s','%s')" % (name, link, des, number, time, degree)
#     cur.execute(sql)
#     con.commit()

# 抓取主函数
def startGrab():
    TotalPage = 50
    # header = {'Accept-Encoding': 'gzip, deflate',
    #           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
    #           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #           'Cookie': 'showNav=#nav-tab|0|0; cy=23; cye=haikou; _hc.v=ef652ae9-e217-b776-a1e6-3a3da7c2929b.1455274430; ' \
    #                     '__utma=1.702117282.1455274430.1455274430.1455274430.1; __utmz=1.1455274430.1.1.utmcsr=(direct)|utmccn=' \
    #                     '(direct)|utmcmd=(none); JSESSIONID=5B485975DD93A791AC46752DA9C38FF1; ' \
    #                     'PHOENIX_ID=0a0302bc-15331af4517-41472; s_ViewType=10; aburl=1',
    #           'Host': 'www.dianping.com',
    #           'Cache-Control': 'max-age=0',
    #           'Connection': 'keep-alive'
    #           }
    for page in range(TotalPage):
        url = 'http://www.dianping.com/search/category/23/30/g132p'+str(page+1)
        print ">>>>>>>>>>>将要抓取", url

        # 可能因为超时等网络问题造成异常，需要捕获并重新抓取
        try:
            html = requests.post(url)
            print html
        except requests.HTTPError:
            print "重新抓取 ", url

        # 使用BeautifulSoup规范化网页并生成对象
        soup = BeautifulSoup(html.content, "html.parser")

        # print soup
        #
        # soft_data = soup.findAll('div', id="sortAndPageAfficheDiv")
        # print soft_data
        # for item in soft_data:
        #
        #     try:
        #         if (item.contents[1].find("a").text):
        #             a = item.contents[1]
        #             print a
        #             b = item.contents[2]
        #             print b
        #             c = item.contents[3]
        #             print c
        #             d = item.contents[4]
        #             print d
        #             name = item.contents[1].find("a").text
        #             link = item.contents[1].find("a").get("href")
        #             des = item.contents[1].find("p").text
        #             number = item.contents[1].find("em", {"class": "learn-number"}).text
        #             time = item.contents[1].find("dd", {"class": "mar-b8"}).contents[1].text
        #             degree = item.contents[1].find("dd", {"class": "zhongji"}).contents[1].text
        #             # lesson_info = {"name": name, "link": link, "des": des, "number": number, "time": time, "degree": degree}
        #             # saveToSqlite(lesson_info)
        #             print "课程名称: ", item.contents[1].find("a").text
        #             print "课程链接: ", item.contents[1].find("a").get("href")
        #             print "课程简介: ", item.contents[1].find("p").text
        #             print "学习人数: ", item.contents[1].find("em", {"class": "learn-number"}).text
        #             print "课程时间: ", item.contents[1].find("dd", {"class": "mar-b8"}).contents[1].text
        #             print "课程难度: ", item.contents[1].find("dd", {"class": "zhongji"}).contents[1].text
        #             print "-----------------------------------------------"
        #     except:
        #         pass


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    startGrab()
    endtime = datetime.datetime.now()
    print "执行时间: ", (endtime - starttime).seconds, "s"