# encoding: utf-8
import requests
import time
import json
import win32api
import win32con

# 获取停复牌信息
def get_suspension_info():
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?' \
          'type=FD&sty=SRB&st=0&sr=-1&p=1&ps=1000&js=var%20veuNVpqs={pages:(pc),data:[(x)]}&mkt=1&fd=' + date + '&rt=49093586'
    r = requests.get(url)
    html = r.content
    # 编辑返回值以便使用json
    data = html.split('=')[1]
    data = data.replace('pages', '"pages"')
    data = data.replace('data', '"data"')
    contents = json.loads(data)['data']
    return contents

def getFileinfo(filename):
    stockid_or_name = ''
    # 打开文件
    f = open(filename, 'r')
    for line in f:
        # 拼装内容
        if not stockid_or_name:
            stockid_or_name = line
        else:
            stockid_or_name = stockid_or_name + ',' + line
    f.close()
    stockid_or_name = stockid_or_name.replace('\n', '')    # 去掉'\n'
    stockid_or_name_as_list = stockid_or_name.split(',')   # 逗号分隔成list
    return stockid_or_name_as_list

def findinfo(stockid_or_name_as_list, suspension_info):
    # 在已抓取信息中循环查找
    for stockidorname in stockid_or_name_as_list:  # 关注股票list
        for suspension in suspension_info:   # 已抓取股票list
            suspension = suspension.split(',')
            if stockidorname == suspension[0].encode('utf-8') or stockidorname == suspension[1].encode('utf-8'):
                output = suspension[0] + ' ' + suspension[1] + ' ' + suspension[2] + ' ' + suspension[8] + ' ' \
                         + suspension[4] + ' ' + suspension[5]
                win32api.MessageBox(0, output, 'WYM', win32con.MB_OK)


if __name__ == '__main__':
    suspension_info = get_suspension_info()
    stockid_or_name_as_list = getFileinfo('stock.txt')
    findinfo(stockid_or_name_as_list, suspension_info)
