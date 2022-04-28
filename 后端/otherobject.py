import base64
import io
import os
from PIL import Image
import cv2
import numpy as np
import math


# brenner梯度函数计算
def brenner(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    out = 0
    for x in range(0, shape[0] - 2):
        for y in range(0, shape[1]):
            out += (int(img[x + 2, y]) - int(img[x, y])) ** 2
    return out


# Laplacian梯度函数计算
def Laplacian(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    return cv2.Laplacian(img, cv2.CV_64F).var()


# SMD梯度函数计算
def SMD(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    out = 0
    for x in range(1, shape[0] - 1):
        for y in range(0, shape[1]):
            out += math.fabs(int(img[x, y]) - int(img[x, y - 1]))
            out += math.fabs(int(img[x, y] - int(img[x + 1, y])))
    return out


# SMD2梯度函数计算
def SMD2(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    out = 0
    for x in range(0, shape[0] - 1):
        for y in range(0, shape[1] - 1):
            out += math.fabs(int(img[x, y]) - int(img[x + 1, y])) * math.fabs(int(img[x, y] - int(img[x, y + 1])))
    return out


# 方差函数计算
def variance(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    out = 0
    u = np.mean(img)
    shape = np.shape(img)
    for x in range(0, shape[0]):
        for y in range(0, shape[1]):
            out += (img[x, y] - u) ** 2
    return out


# energy函数计算
def energy(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    out = 0
    for x in range(0, shape[0] - 1):
        for y in range(0, shape[1] - 1):
            out += ((int(img[x + 1, y]) - int(img[x, y])) ** 2) * ((int(img[x, y + 1] - int(img[x, y]))) ** 2)
    return out


# Vollath函数计算
def Vollath(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    u = np.mean(img)
    out = -shape[0] * shape[1] * (u ** 2)
    for x in range(0, shape[0] - 1):
        for y in range(0, shape[1]):
            out += int(img[x, y]) * int(img[x + 1, y])
    return out


# entropy函数计算
def entropy(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    out = 0
    count = np.shape(img)[0] * np.shape(img)[1]
    p = np.bincount(np.array(img).flatten())
    for i in range(0, len(p)):
        if p[i] != 0:
            out -= p[i] * math.log(p[i] / count) / count
    return out


final = {}
list1 = []
list2 = []


def make(fuc, imgs):
    # print(int(str(int(fuc(imgs)))[0]) + int(str(int(fuc(imgs)))[1]) * 0.1)
    # t=str(fuc(imgs))
    # print(int(str(fuc(imgs))[0]) + int(str(Laplacian(imgs))[1]) * 0.1)
    # return int(str(int(fuc(imgs)))[0]) + int(str(int(fuc(imgs)))[1]) * 0.1
    # print("数字为：",int(fuc(imgs)))
    # print("位数为：",len(str(int(fuc(imgs)))))
    return int(fuc(imgs))/ pow(10,len(str(int(fuc(imgs))))-1)

def mains(num):
    for i in num:
        # print(filename, ":")
        # img = cv2.imread(file_pathname + '/' + filename)
        list1.append(i)
        a = base64.b64decode(num[i])
        a = io.BytesIO(a)
        a = Image.open(a)
        a = np.array(a)
        a = a * 255.0
        newa = Image.fromarray(np.uint8(a))
        # print('pp')
        newa = np.array(newa)
        imgs = cv2.cvtColor(newa, cv2.COLOR_BGR2GRAY)
        sum = brenner(imgs) / pow(10, (len(str(brenner(imgs))) - 1))+make(Laplacian,imgs)+\
         make(SMD, imgs) + make(SMD2, imgs) + make(variance, imgs) + make(energy, imgs) + \
        make(Vollath, imgs) + entropy(imgs)
        list2.append(sum)

    final = dict(zip(list1, list2))
    # print(final)
    return final


# mains('./dir')

# if __name__ == '__main__':
#     #     # 读入原始图像
#     #     img1 = cv2.imread('/home/hadoop/文档/毕设/Access/neural-image-assessment-master/dir/1.jpg')
#     #     img2 = cv2.imread('/home/hadoop/文档/毕设/Access/neural-image-assessment-master/dir/3.png')
#     #     # 灰度化处理
#     #     img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#     #     img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#     print(main('./dir'))
