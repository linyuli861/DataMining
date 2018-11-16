# 导入csv模块
import csv
from collections import Counter
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
# import plotly.plotly


# 指定文件名，然后使用 with open() as 打开
filename = "../data/metro-2018.csv"
with open(filename) as f:
    # 创建一个阅读器：将f传给csv.reader
    reader = csv.reader(f)
    # 使用csv的next函数，将reader传给next，将返回文件的下一行
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # 获取开始骑行的时间
    start_time = []
    end_time = []
    for row in reader:
        start_time.append(row[2])
        end_time.append(row[3])

    # 获取开始骑行时间中的hour
    len1 = len(start_time)
    s1 = []
    for i in range(len1):
        # print(start_time[i].replace("T", " "))
        # print(end_time[i].replace("T", " "))
        start = start_time[i]
        print(start[11: 13])
        s1.append(start[11:13])

    # 统计具体每个hour使用小黄车的人
    count_dict = defaultdict(int)
    for item in s1:
        count_dict[item] += 1
    print(count_dict)
    a = sorted(count_dict.items(), key=lambda item:item[0])
    print(a)

