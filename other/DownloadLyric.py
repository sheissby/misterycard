# encoding: utf-8
import requests
from lxml import etree
import re

base_url = 'http://music.baidu.com/search/lrc?key='
pattern = re.compile(r'/[\S]+')
no_result = '抱歉，没有找到相关的音乐内容，我们正在努力地建设百度音乐的歌曲资源'


def search(param):
    r = requests.get(base_url + param)
    if r.status_code == 200:
        if no_result in r.content:
            print '未找到内容'
            exit()
        else:
            return r.content
    else:
        print '打开网页失败'
        exit()


def parse(html):
    lyrics = []
    i = 1
    tree = etree.HTML(html)
    lis = tree.xpath('//li[@class="clearfix bb"]')
    for li in lis:
        title = li.xpath('div[@class="song-content"]/span[@class="song-title"]/a')
        title = title[0].xpath('string(.)').replace('\n', '').replace('\t', '').replace(' ', '')
        artist = li.xpath('div[@class="song-content"]/span[@class="artist-title"]/span[@class="author_list"]')
        artist = artist[0].xpath('string(.)').replace('\n', '').replace('\t', '').replace(' ', '')
        try:
            album = li.xpath('div[@class="song-content"]/span[@class="album-title"]/a')[0]
        except IndexError:
            album = li.xpath('div[@class="song-content"]/span[@class="album-title"]')[0]
        album = album.xpath('string(.)').replace('\n', '').replace('\t', '').replace(' ', '')
        url = li.xpath('div[@class="lrc-content"]/span[@class="lyric-action"]/a/@class')
        # down-lrc-btn { 'href':'/data2/lrc/436087/436087.lrc' }
        url = re.search(pattern, url[0]).group().replace("'", '')
        url = 'http://music.baidu.com' + url
        info = {}
        info['id'] = i
        info['title'] = title.encode('utf-8')
        info['artist'] = artist.encode('utf-8')
        info['album'] = album
        info['url'] = url
        lyrics.append(info)
        i += 1

    for lyric in lyrics:
        print lyric['id'], lyric['title'], lyric['artist'], lyric['album']
    return lyrics


def download(number, lyrics):
    download_url = lyrics[number-1]['url']
    title = lyrics[number-1]['title']
    artist = lyrics[number-1]['artist']
    filename = title + '-' + artist + '.lrc'
    r = requests.get(download_url)
    with open(filename.decode('utf-8'), 'wb') as code:
        code.write(r.content)

if __name__ == '__main__':
    param = raw_input('输入歌名或歌手：').replace(' ', '+')
    html = search(param)
    lyrics = parse(html)
    number = input('序号：')
    download(number, lyrics)

