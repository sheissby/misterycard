# -*-coding:utf-8-*-
import cv2
import os
import numpy as np

# 加载目标图片和源图片
template = cv2.imread('target.jpg')
source = cv2.imread('source.jpg')
# 获取目标图片宽度、高度
w, h, _ = template.shape


# 匹配图片，返回最佳匹配的坐标
def match(source, template):
    result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_loc


def draw(source, max_loc):
    # 画矩形(文件、起点坐标、对角线坐标、颜色、线宽)
    cv2.rectangle(source, max_loc, (max_loc[0] + h, max_loc[1] + w), (0, 0, 255), 2)
    cv2.imshow('Detected', source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    max_loc = match(source, template)
    draw(source, max_loc)
