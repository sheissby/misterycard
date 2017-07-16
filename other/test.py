# encoding: utf-8
from Crypto.Cipher import AES
import base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

key = '30fa5256c135c5cf36438bd1a469464e'
ciphertext = '11hi84k6vkeNotjz9PxDAMxb9LJbrAnfLXbU7qgMrAgAoLDCwoTXzX6LgmSqqeAPHdSSoWy/5Zfu/5p7p8p1N1qKzvXnRKwcflyZ/cXK+dapqmDlMI3f1so3e2DJ/d++NHP9RhNR3bkz3J3dgxQmFH2Y7RW6JuuBailLa6q16ts1l+FGCINaK1th2FAcWg4apByjSwlqACpSgg5ovFXTBfUKEkcAmKcgFFKGEc9LZKE7qUKMv0ObocNrP/iBmd8SvPnBy1ZBIM5dJIc+QgeDtaqgUoAaIYlX+vPpZ4khClGkK2yA+4OoOLP2MRziCsYcDrG8bkfEG0GAecex1tP7mwod8/OqBfGw=='
ciphertext = base64.b64decode(ciphertext)
text = AES.new(key, AES.MODE_CBC, b'0000000000000000')
text = unpad(text.decrypt(ciphertext))
print text
