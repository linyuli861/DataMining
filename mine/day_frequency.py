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

x_values = []
y_values = []
a = len(day_frequency)
for i in range(a):
    x_values.append(day_frequency[i][0])
    y_values.append(day_frequency[i][1])

plt.scatter(x_values, y_values, c=y_values, edgecolors='blue', s=60)
plt.title("Day_Number of rides", fontsize=20)
plt.xlabel("Day", fontsize=20)
plt.ylabel("Number of rides", fontsize=20)
plt.tick_params(axis='both', labelsize=6)
plt.show()

l1 = plt.plot(x_values, y_values, "b--")
plt.plot(x_values, y_values, "bo-")
plt.title("Day_Number of rides", fontsize=20)
plt.xlabel("Day", fontsize=20)
plt.ylabel("Number of rides", fontsize=20)
plt.legend()
plt.show()



