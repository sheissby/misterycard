# encoding: utf-8
import json
import requests
import codecs

lyric_url = 'http://geci.me/api/lyric/'
singer_url = 'http://geci.me/api/artist/'

def getsinger(singerid):
    # pass
    url = ''.join([singer_url, singerid])
    r = requests.get(url)
    singer = json.loads(r.content)['result']['name']
    return singer


def getlyric(songname):
    url = ''.join([lyric_url, songname])
    r = requests.get(url)
    response = json.loads(r.content)
    a = []
    if response['count'] != 0:
        for lyric in response['result']:
            url = lyric['lrc']
            songname = lyric['song']
            songid = lyric['sid']
            singerid = lyric['artist_id']
            singer = getsinger(str(singerid))
            # [歌名， 歌曲id， 歌手， url]
            songinfo = [songname.encode('utf-8'), songid, singer.encode('utf-8'), url]
            a.append(songinfo)
        return a
    else:
        print '未找到歌词'


def display(lyrics):
    for i in range(len(lyrics)):
        print i, lyrics[i][0], lyrics[i][2]
        print lyrics[i][0], type(lyrics[i][0])
        print lyrics[i][2], type(lyrics[i][2])
    pass


def downloadlyric(num):
    url = lyrics[num][3]
    r = requests.get(url)
    with codecs.open(lyrics[num][0].decode('utf-8')+' - '+lyrics[num][2]+'.lyc', "wb") as code:
        code.write(r.content)
    pass


if __name__ == '__main__':
    songname = raw_input('请输入歌名：')
    lyrics = getlyric(songname)
    display(lyrics)
    num = input()
    downloadlyric(num)
