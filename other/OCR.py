# encoding: utf-8
import io
import requests
from PIL import ImageTk
from PIL import Image as PI
from pytesseract import *
from Tkinter import *
import tkFileDialog


class OCR():
    def __init__(self):
        self.images_path = []
        root.geometry("400x200+200+20")
        root.title('orc对比')
        Button(root, text='下一张', command=self.getimage).pack()
        Label(root).pack()


    def getimage(self):
        r = requests.get('http://www.ekingservice.com/getAuthCode/login').content
        img = io.BytesIO(r)
        image = PI.open(img)
        photoimage = ImageTk.PhotoImage(image)
        # image = PhotoImage('login.png')
        vcode = pytesseract.image_to_string(image)
        Label(root, image=photoimage).pack()


if __name__ == '__main__':
    root = Tk()
    gui = OCR()
    root.mainloop()
