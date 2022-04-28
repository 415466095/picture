# 40-70==>1-5

value = [45.35, 68.83, 49.89, 52.42, 63.18, 57.66, 42.73]
# value2 = [1, 4, 2, 2, 3, 3, 2]
k = float(5 / (max(value) - min(value)))
t = "%.2f" % k
t = float(t)
transform_value = [round(t * (x - min(value)), 2) for x in value]
# transform_value1 = [x * 0.8 + transform_value[x] * 0.2 for (x, i) in value2]
print(transform_value)


# 二维标签列表，下面一共三张图
# list1 = [["猴子","蚂蚁"],["猴子","大海"],["大海","太空","猴子"]]
# # 输入1
# input1 = "猴子"
# # 输出1
# output1 = [1, 2, 3]
# # 输入2
# input2 = "大海"
# # 输出2
# output2 = [2, 3]
# # 输入3
# input3 = "城市"
# # 输出3
# output3 = []
