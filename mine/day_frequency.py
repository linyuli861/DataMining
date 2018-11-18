# coding = utf-8
import csv
import pandas as pd
import seaborn as sns
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime


df = pd.read_csv("../modify_data/time.csv", header=0, sep=",")
cols = df.columns  # return column name
# print(cols)  # print column name

days = df['day']
count_dict = defaultdict(int)
# accoding to month compute frequency
for item in days:
    count_dict[item] += 1
    # print(count_dict)
    day_frequency = sorted(count_dict.items(), key=lambda item: item[0])



print(day_frequency)  # print statistical data


