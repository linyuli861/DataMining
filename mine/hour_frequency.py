# coding = utf-8
import csv
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt


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

x_values = []
y_values = []
for i in range(0, 23):
    x_values.append(hour_frequency[i][0])
    y_values.append(hour_frequency[i][1])

plt.scatter(x_values, y_values, c=y_values, edgecolors='blue', s=60)
plt.title("Hour_Number of rides", fontsize=20)
plt.xlabel("Hour", fontsize=20)
plt.ylabel("Number of rides", fontsize=20)
plt.tick_params(axis='both', labelsize=14)
plt.show()



