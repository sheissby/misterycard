# encoding: utf-8
import csv
import json
import requests

ID = set()


def GetQuestion():
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    url = 'http://mlearning.pingan.com.cn/learn/app/clientapi/exam/getExamPaper.do'
    data = 'examId=1053992&umId=537EA626E4D0788AE054022128574717&sid=F425882BB9F140C99F478015ED2E11D9'
    r = requests.post(url, data=data, headers=header)
    decode_json = json.loads(r.content)
    examArrs = decode_json['body']['examArr']
    return examArrs


def parse(examArrs):
    res_data = []
    for examArr in examArrs:
        question = examArr['question'].encode('utf-8')
        question = question.replace('\u201c', '“').replace('\u201d', '”')
        if question in ID:
            continue
        else:
            ID.add(question)
            sectionArrs = examArr['sectionArr']
            for sectionArr in sectionArrs:
                iscorrect = sectionArr['isCorrect']
                if iscorrect == 'Y':
                    sectiontext = sectionArr['sectionText'].encode('utf-8')
                    sectiontext = sectiontext.replace('\u201c','“').replace('\u201d','”')
                    break
            res_data.append((question, sectiontext))
    return res_data


def save2cvs(res_data):
    csvfile = file('aaaaaaa.csv', 'ab+')
    writer = csv.writer(csvfile)
    for data in res_data:
        writer.writerow(data)
    csvfile.close()


if __name__ == '__main__':
    for i in range(1, 20):
        save2cvs(parse(GetQuestion()))





