# coding = utf-8
import csv
import pandas as pd
from collections import defaultdict

df = pd.read_csv("../modify_data/time.csv", header=0, sep=",")
cols = df.columns  # return column name
print(cols)  # print column name

months = df['month']
count_dict = defaultdict(int)
# accoding to month compute frequency
for item in months:
    count_dict[item] += 1
    # print(count_dict)
    month_frequency = sorted(count_dict.items(), key=lambda item: item[0])
print("month_frequency")
print(month_frequency)
