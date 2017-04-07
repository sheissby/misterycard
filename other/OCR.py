# encoding: utf-8
import io
import requests
from PIL import Image as PI
from pytesseract import *



def getimage():
    r = requests.get('http://www.ekingservice.com/getAuthCode/login').content
    img = io.BytesIO(r)
    image = PI.open(img)
    image.save('OCR.jpg')
    vcode = pytesseract.image_to_string(image)
    print vcode


if __name__ == '__main__':
    getimage()
