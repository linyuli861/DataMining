# coding = utf-8
import csv
import pandas as pd
from collections import defaultdict

df = pd.read_csv("../modify_data/time.csv", header=0, sep=",")
cols = df.columns  # return column name
print(cols)  # print column name

hours = df['hour']
count_dict = defaultdict(int)
# accoding to hour compute frequency
for item in hours:
    count_dict[item] += 1
    # print(count_dict)
    hour_frequency = sorted(count_dict.items(), key=lambda item: item[0])
print("hour")
print(hour_frequency)
