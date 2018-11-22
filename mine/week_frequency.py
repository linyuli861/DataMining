# coding = utf-8
import csv
import pandas as pd
import seaborn as sns
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime


df = pd.read_csv("../modify_data/three_cleaning_data.csv", header=0, sep=",")
cols = df.columns  # return column name
# print(cols)  # print column name

week_days = df['week_day']
count_dict = defaultdict(int)
# accoding to month compute frequency
for item in week_days:
    count_dict[item] += 1
    # print(count_dict)
    week_frequency = sorted(count_dict.items(), key=lambda item: item[0])

print(week_frequency)  # print statistical data

x_values = []
y_values = []
a = len(week_frequency)
for i in range(a):
    x_values.append(week_frequency[i][0])
    y_values.append(week_frequency[i][1])

x_values = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
plt.scatter(x_values, y_values, c=y_values, edgecolors='blue', s=60)
plt.title("Day_Number of rides", fontsize=20)
plt.xlabel("Day", fontsize=20)
plt.ylabel("Number of rides", fontsize=20)
plt.tick_params(axis='both', labelsize=6)
plt.savefig("../graph/weekDay-numberOfRide-scatter.jpg")
plt.show()

l1 = plt.plot(x_values, y_values, "b--")
plt.plot(x_values, y_values, "bo-")
plt.title("Weekday_Number of rides", fontsize=20)
plt.xlabel("Weekday", fontsize=20)
plt.ylabel("Number of rides", fontsize=20)
plt.legend()
plt.savefig("../graph/weekDay-numberOfRide-plot.jpg")
plt.show()

plt.style.use("ggplot")
fig = plt.figure(figsize=(16, 24))
ax1 = fig.add_subplot(1, 1, 1)
fig.set_size_inches(18, 8)
sns.barplot(data=df, x=x_values, y=y_values, ax=ax1)
ax1.set(xlabel="day", ylabel="y_values", title="week-count")
plt.savefig("../graph/week-numberOfRide-barplot.jpg")
plt.show()

