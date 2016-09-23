# encoding: utf-8
import PIL.Image as PI
from Tkinter import *
import os
import tkFileDialog


class Combine():
    def __init__(self):
        self.images_path = []
        # self.images_path = ['1.gif', '2.gif']
        root.geometry("400x200+200+20")
        root.title('自动合并图片')
        Button(root, text='选择图片', command=self.openfile).pack()
        Button(root, text='合并图片', command=self.combine).pack()

    def openfile(self):
        filepath = tkFileDialog.askopenfilename(initialdir='E:/Python')
        self.images_path.append(filepath)

    def combine(self):
        new_width = 0
        new_height = 0
        # 计算合成后图片的高度（以最高的为准）和宽度
        for img_path in self.images_path:
            if os.path.exists(img_path):
                image = PI.open(img_path)
                width, height = image.size
                if height > new_height:
                    new_height = height
                new_width += width

        # 产生一张空白图
        new_img = PI.new('RGB', (new_width, new_height), (255, 255, 255))
        # 合并
        x = y = 0
        for img_path in self.images_path:
            if os.path.exists(img_path):
                img = PI.open(img_path)
                width, height = img.size
                new_img.paste(img, (x, y))
                x += width

        # output_dir = os.getcwd()
        output_name = (img.filename.split('.'))[0][:-1]
        save_path = output_name + '.jpg'
        new_img.save(save_path)
        self.images_path = []

if __name__ == '__main__':
    root = Tk()
    gui = Combine()
    # gui.combinepic()
    root.mainloop()
