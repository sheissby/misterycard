# encoding: utf-8
import base64
from Crypto.Cipher import AES
import win32clipboard as w
import win32con

def encrypt():
    # 密文
    password = 'baiyang000000000'
    # 秘钥
    key = raw_input("Enter key:")
    if key:
        # 秘钥补足16位
        lenth = 16
        keylenth = len(key)
        add = keylenth % lenth
        if add:
            key = key + ('\0' * (lenth - add))
        # 使用AES加密，密文转base64
        encryptor = AES.new(key, AES.MODE_CBC, b'0000000000000000')
        ciphertext = base64.b64encode(encryptor.encrypt(password))
        ciphertext = ciphertext.replace('/', '')
        # 截取特定位数
        ciphertext = ciphertext[0: 8]
        print ciphertext
        return ciphertext
    else: return encrypt()


def setText(ciphertext):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, ciphertext)
    w.CloseClipboard()

if __name__ == '__main__':
    setText(encrypt())
    raw_input()
