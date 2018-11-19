# coding = utf-8
import csv
import pandas as pd
import seaborn as sns
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


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
plt.savefig("../graph/day-numberOfRide-scatter.jpg")
plt.show()

l1 = plt.plot(x_values, y_values, "b--")
plt.plot(x_values, y_values, "bo-")
plt.title("Day_Number of rides", fontsize=20)
plt.xlabel("Day", fontsize=20)
plt.ylabel("Number of rides", fontsize=20)
plt.legend()
plt.savefig("../graph/day-numberOfRide-plot.jpg")
plt.show()

# plt.style.use["ggplot"]
plt.style.use("ggplot")
fig = plt.figure(figsize=(8, 12))
ax2 = fig.add_subplot(1, 1, 1)
fig.set_size_inches(8,6)
sns.barplot(data=df, x=x_values, y=y_values, ax=ax2)
ax2.set(xlabel="day", ylabel="y_values", title="day-count")
my_x_ticks = np.arange(x_values[0],x_values[-1])
plt.savefig("../graph/day-numberOfRide-barplot.jpg")
plt.show()

