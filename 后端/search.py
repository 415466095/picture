import re

file_list = [
    ["鸟", "鲸鱼", "猴子", "鲸鲨",''],
    ["鲸鱼","虎鲨","章鱼"],
    ["老虎","狮子"],
    ["鲨鱼","鸵鸟","椰子","猴子"],
]
def fuzzy_finder(key, data):
    """
    模糊查找器
    :param key: 关键字
    :param data: 数据
    :return: list
    """
    result=[]
    pattern = '.*%s.*'%(key)
    # 编译正则表达式
    regex = re.compile(pattern)
    i=0
    for cla in data:
        for item in cla:
            match = regex.search(item)
            if match:
                result.append(i)
        i+=1
    result = list(set(result))# 去重
    return result

# 搜索关键字
keys = "猴子"
result = fuzzy_finder(keys,file_list)
print(result)