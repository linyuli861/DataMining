# coding=utf-8
import pandas as pd  # 导入数据分析库pandas
from scipy.interpolate import lagrange  # 导入拉格朗日插值函数
import csv
from sklearn import preprocessing


# 指定文件名，然后使用 with open() as 打开
filename = "../data/metro-2018.csv"
outfile = "../data/output_2018.csv"
data = pd.read_csv(filename)  # 读入数据
row_indexs = (data['duration'] < 0) | (data['duration'] > 100)
data.loc[row_indexs, 'duration'] = None  # 过滤数据

# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5



data.to_csv(outfile)