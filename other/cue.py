# -*- coding: utf-8 -*-
import os
import codecs

filelist = []


def GetFilesAndPath(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for i in files:
            if i.split('.')[-1].lower() in ('ape', 'wav', 'flac'):
                filelist.append(i)
    return root, filelist


def writecue(path, files):
    # 根据文件夹名（“歌手 - 专辑”）提取歌手和专辑名
    performer = path.split('-')[0].split('\\')[-1].rstrip()
    title = path.split('-')[1].lstrip()
    filename = path + '\\' + title + '.cue'
    with codecs.open(filename, 'w', encoding='gbk') as f:
        f.write('PERFORMER "%s"\nTITLE "%s"\n' % (performer, title))
        for i in files:
            f.write('FILE "%s" WAVE\n' % i)
            f.write('  TRACK %s AUDIO\n' % str(files.index(i)+1))

            # 处理文件名中带.的情况
            filename = i.split('.')
            for j in range (i.count('.')):
                name = ''
                name = name + filename[j]
            f.write('    TITLE "%s"\n' % name)
            f.write('    INDEX 01 00:00:00\n')


if __name__ == '__main__':
    dir = input()
    if os.path.exists(dir):
        path, files = GetFilesAndPath(dir)
        writecue(path, files)
