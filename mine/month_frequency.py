# coding = utf-8
import csv
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns


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

x_values = []
y_values = []
for i in range(0, 3):
    x_values.append(month_frequency[i][0])
    y_values.append(month_frequency[i][1])

plt.scatter(x_values, y_values, c=y_values, edgecolors='blue', s=60)
plt.title("Month_Number of rides", fontsize=20)
plt.xlabel("Month", fontsize=20)
plt.ylabel("Number of rides", fontsize=20)
plt.tick_params(axis='both', labelsize=14)
plt.show()


plt.style.use("ggplot")
fig = plt.figure(figsize=(16, 24))
ax1 = fig.add_subplot(1, 1, 1)
fig.set_size_inches(18, 8)
sns.barplot(data=df, x=x_values, y=y_values, ax=ax1)
ax1.set(xlabel="day", ylabel="y_values", title="month-count")
plt.savefig("../graph/month-numberOfRide-barplot.jpg")
plt.show()