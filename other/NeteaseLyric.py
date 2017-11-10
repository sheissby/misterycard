# encoding: utf-8
from Crypto.Cipher import AES
import base64
import requests
import json
import codecs
import _winreg

# 第二个参数
second_param = "010001"
# 第三个参数
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
# 第四个参数
forth_param = "0CoJUm6Qyw8W8jud"


# 获取桌面路径
def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0]


# 加密过程
def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


# 获得歌词json数据
def get_json(url, id):
    # 获取参数，song_id为传入页数
    def get_params(id):
        iv = "0102030405060708"
        first_key = '0CoJUm6Qyw8W8jud'
        second_key = 16 * 'F'
        first_param = '{"id":"%s","lv":-1,"tv":-1,"csrf_token":""}' % id
        h_encText = AES_encrypt(first_param, first_key, iv)
        h_encText = AES_encrypt(h_encText, second_key, iv)
        return h_encText

    # 获取 encSecKey
    def get_encSecKey():
        encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
        return encSecKey

    data = {
         "params": get_params(id),
         "encSecKey": get_encSecKey()
    }
    response = requests.post(url, data=data)
    return json.loads(response.content)


# 将评论写入文本文件
def save_to_file(txt,filename):
    with codecs.open(filename,'a',encoding='utf-8') as f:
        f.writelines(txt)
    print("写入文件成功!")

if __name__ == "__main__":
    url = "http://music.163.com/weapi/song/lyric?csrf_token="
    song_id = raw_input("song ID:")
    json_text = get_json(url, song_id)
    lyric = json_text['lrc']['lyric']
    save_to_file(lyric, get_desktop()+'/test.lrc')
