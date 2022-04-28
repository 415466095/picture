from evaluate_inception_resnet import run
from liangdu import read_path
from duibidu import duibidu
from otherobject import mains

evaluate_ranks = {}
lightings = []

# 设定：

# 亮度百分之10,对比度百分之15,其他客观15%
# 由于这些数值无量纲，按照一组中最高的那个为量纲取分

def evaluate_rank(num):
    for i,j in num.items():
        evaluate_ranks[i] = j*8
    return evaluate_ranks

def lighting(num):
    # 亮度百分之10 ,10分
    list1 = []
    dir1 = {}
    for i, j in num.items():
        list1.append(j)
        dir1[i] = j
    climax = max(list1)
    for i, j in num.items():
        if j != climax:
            j = (j/climax) * 5
            dir1[i] = j
        else:
            dir1[i] = 5
    return dir1

def duibidus(num):
    list1 = []
    dir1 = {}
    for i, j in num.items():
        list1.append(j)
        dir1[i] = j
    climax = max(list1)
    for i, j in dir1.items():
        if j != climax:
            j = (j / climax) * 10
            dir1[i] = j
        else:
            dir1[i] = 10
    return dir1
    # return duibidu("./dir")

def objectassessment(num):
    list1 = []
    dir1 = {}
    for i, j in num.items():
        list1.append(j)
        dir1[i] = j
    climax = max(list1)
    for i, j in dir1.items():
        if j != climax:
            j = (j / climax) * 5
            dir1[i] = j
        else:
            dir1[i] = 5
    return dir1
    # return mains("./dir")

def finalrank(a,b,c,d):
    tin = {}
    temp = dict()
    # dict_keys类似set； | 并集
    for key in a.keys() | b.keys() | c.keys() | d.keys():
        temp[key] = sum([e.get(key, 0) for e in (a, b, c, d)])
    return temp


# if __name__ == '__main__':
#     # print(evaluate_rank())
#     # print(lighting())
#     # print(duibidus())
#     # print(objectassessment())
#     print(finalrank(evaluate_rank(), lighting(), duibidus(), objectassessment()))


