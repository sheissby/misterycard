#! /usr/bin/python
# coding:utf-8
"""
@author:Bingo.he
@file: upload_excel_data.py
@time: 2018/05/03
"""


import ConfigParser
import collections
import xlrd
import testlink
import os

count_success = 0
count_fail = 0


def get_projects_info():
    project_ids = []
    projects = tlc.getProjects()
    for project in projects:
        project_ids.append({project['name']: project['id']})
    return project_ids


def get_projects_id():
    project_ids = []
    projects = tlc.getProjects()
    for project in projects:
        project_ids.append(project['id'])
    return project_ids


def get_suites(suite_id):
    """
    获取用例集
    :return:
    """
    try:
        suites = tlc.getTestSuiteByID(suite_id)
        return suites
    except testlink.testlinkerrors.TLResponseError as e:
        # traceback.print_exc()
        print(str(e).split('\n')[1])
        print(str(e).split('\n')[0])
        return


def readExcel(file_path):
    """
    读取用例数据
    :return:
    """
    case_list = []
    try:
        book = xlrd.open_workbook(file_path)  # 打开excel
    except Exception as error:
        print(u'路径不在或者excel不正确 : ' + str(error))
        return error
    else:
        for sheet_count in range(0, book.nsheets):
            sheet = book.sheet_by_index(sheet_count)  # 取第一个sheet页
            rows = sheet.nrows  # 取这个sheet页的所有行数
            for i in range(rows):
                if i != 0:
                    case_list.append(sheet.row_values(i))  # 把每一条测试用例添加到case_list中
    return case_list


def check_excel_data(func):
    """
    参数有效性校验
    :param func:
    :return:
    """

    def _check(*args, **kw):
        global count_fail
        global count_success

        # 检测测试数据的有效性
        for k, v in kw.items():
            if v == "" and k not in ['summary', 'preconditions']:
                print("TestCase '{title}' Parameter '{k}' is null".format(title=kw['title'], k=k))
            if k in ['id'] and not get_suites(int(v)):
                print('ERROR! father_id is not auth')
        try:
            func(args[0], kw)
            count_success += 1
        except Exception as e:
            print(e)
            count_fail += 1
    return _check


def format_info(source_data):
    """
    转换Excel中文关键字
    :param source_data:
    :return:
    """
    switcher = {
        u"低": 1,
        u"中": 2,
        u"高": 3,
        u"自动化": 2,
        u"手工": 1
    }
    return switcher.get(source_data, "Param not defind")


@check_excel_data
def create_testcase(test_project_id, data):
    """
    :param test_project_id:
    :param data:
    :return:
    """
    # 设置优先级默认值及摘要默认值
    if data['importance'] not in [1, 2, 3]:
        data['importance'] = 3
    if data['automation'] == "":
        data['automation'] = "手工"

    # 初始化测试步骤及预期结果
    for i in range(0, len(data["step"])):
        tlc.appendStep(data["step"][i][0], data["step"][i][1], data["automation"])

    tlc.createTestCase(data["title"], int(data['id']), test_project_id, data["authorlogin"], data["summary"],
                       preconditions=data["preconditions"], importance=data['importance'], executiontype=data['automation'])


def excute_creat_testcase(test_project_id, test_file_name):
    # 对project_id 做有效性判断
    if test_project_id not in get_projects_id():
        print('ERROR! project_id is not auth')
        return


    # 获取用例
    test_cases = readExcel(os.path.join(test_file_name))
    # test_cases = readExcel(os.path.join('testCase', test_file_name))
    if not isinstance(test_cases, collections.Iterable):
        return

    # 格式化用例数据
    for test_case in test_cases:
        # 验证father_id有效性
        # if not get_suites(test_father_id):
        #     print('ERROR! father_id is not auth')
        #     return
        testCase_data = {
            "id": test_case[0],
            "title": test_case[1],
            "preconditions": test_case[2],
            "step": list(zip(test_case[3].split('\n'), test_case[4].split('\n'))),  # 以换行符作为测试步骤的分界
            "automation": format_info(test_case[5]),  # 1  手工, 2 自动
            "authorlogin": test_case[6],
            "importance": format_info(test_case[7]),
            "summary": test_case[8]
        }

        create_testcase(test_project_id, **testCase_data)
    print(u"本次操作共提交 {} 条数据，成功导入 {} 条，失败 {} 条".format(count_success + count_fail, count_success, count_fail))


if __name__ == "__main__":
    # 读取配置文件
    config = ConfigParser.ConfigParser()
    config.read('init.conf')
    host = config.get('conf','host')
    key = config.get('conf', 'key')
    project_id = config.get('conf', 'project_id')
    file_name = config.get('conf', 'file_name')

    url = host + "/testlink/lib/api/xmlrpc/v1/xmlrpc.php"  # 替换为testlink对应URL
    # key = "274f2e3aa32d575d2c3f8085b1c66f87"  # 这个key是错误的key，登陆testlink后点击上方个人账号进入个人中心，新页面点击 '生成新的秘钥'获取
    # file_name = "excel_to_testlink_demo.xlsx"
    # project_id = "1"  # 可以通过 print(get_projects_info())获取
    tlc = testlink.TestlinkAPIClient(url, key)

    # print("项目信息: ", get_projects_info())
    excute_creat_testcase(project_id, file_name)

