import base64
import io
from PIL import Image
from cv2 import cv2
import numpy as np
import cv2
import os


def contrast(img0):
    img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)  # 彩色转为灰度图片
    m, n = img1.shape
    # 图片矩阵向外扩展一个像素
    img1_ext = cv2.copyMakeBorder(img1, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
    rows_ext, cols_ext = img1_ext.shape
    b = 0.0
    for i in range(1, rows_ext - 1):
        for j in range(1, cols_ext - 1):
            b += ((img1_ext[i, j] - img1_ext[i, j + 1]) ** 2 + (img1_ext[i, j] - img1_ext[i, j - 1]) ** 2 +
                  (img1_ext[i, j] - img1_ext[i + 1, j]) ** 2 + (img1_ext[i, j] - img1_ext[i - 1, j]) ** 2)

    cg = b / (4 * (m - 2) * (n - 2) + 3 * (2 * (m - 2) + 2 * (n - 2)) + 2 * 4)  # 对应上面48的计算公式
    # print(cg)
    return cg


score_list1 = []
score_list2 = []
fins = {}


# 这个是无参考图像质量评价指标——对比度:
def duibidu(num):
    t = 0
    for i in num:
        print(i)
        # print(filename)
        # img = cv2.imread(file_pathname + '/' + filename)
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
        cg = contrast(newa)
        score_list2.append(cg)
        print(score_list1[t],":",cg)
        t = t+1
    # print(score_list1)
    fins = dict(zip(score_list1, score_list2))
    # for i, (name, score) in enumerate(score_list):
    #     f = open('./www.txt', 'a')
    #     print("%d)" % (i + 1), "%s : Score = %0.5f" % (name, score))
    #     f.write("%d)" % (i + 1) + "%s : Score = %0.5f" % (name, score) + '\n')
    #     f.close()
    # print(cg)
    return fins

# read_path("./dir")
