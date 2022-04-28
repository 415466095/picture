import base64
import io

from PIL import Image
from PIL import ImageStat
import cv2
import os
import np


# def brightness(im_file):
#     im = cv2.cvtColor(im_file, cv2.COLOR_BGR2GRAY)
#     stat = ImageStat.Stat(im)
#     return stat.rms[0]


score_list1 = []
score_list2 = []
mark = {}


# 　这个是无参考图像质量评价指标——亮度，保存在yyy.txt文档中；
def read_path(num):
    # 遍历该目录下的所有图片文件
    t=0
    for i in num:
        score_list1.append(i)
        # print(num[i])
        a = base64.b64decode(num[i])
        a = io.BytesIO(a)
        a = Image.open(a)
        # a = a.resize((224, 224))
        a = np.array(a)
        a = a * 255.0
        newa = Image.fromarray(np.uint8(a))
        # print('pp')
        newa = np.array(newa)
        # print(type(newa))
        hsv_image = cv2.cvtColor(newa, cv2.COLOR_BGR2HSV)
        lightness = hsv_image[:, :, 2].mean()
        # print(score_list1[t],lightness)
        score_list2.append(lightness)
        t = t+1
    mark = dict(zip(score_list1,score_list2))
    # for filename in os.listdir(file_pathname):
    #     # print(filename)
    #     img = Image.open(file_pathname + '/' + filename)
    #     img = img.convert("L")
    #     stat = ImageStat.Stat(img)
    #     cg = stat.rms[0]
    #     score_list1.append(filename)
    #     score_list2.append(cg)
    # mark = dict(zip(score_list1, score_list2))
    return mark
    # for i, (name, score) in enumerate(score_list):
    #     f = open('./yyy.txt', 'a')
    #     print("%d)" % (i + 1), "%s : Score = %0.5f" % (name, score))
    #     f.write("%d)" % (i + 1) + "%s : Score = %0.5f" % (name, score) + '\n')
    #     f.close()

    # print(cg)

# read_path("./dir")
