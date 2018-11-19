# coding = utf-8
import csv
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns

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
for i in range(0, 24):
    x_values.append(hour_frequency[i][0])
    y_values.append(hour_frequency[i][1])

plt.scatter(x_values, y_values, c=y_values, edgecolors='blue', s=60)
plt.title("Hour_Number of rides", fontsize=20)
plt.xlabel("Hour", fontsize=20)
plt.ylabel("Number of rides", fontsize=20)
plt.tick_params(axis='both', labelsize=14)
plt.savefig("../graph/hour-numberOfRide-scatter.jpg")
plt.show()

# plt.style.use["ggplot"]
plt.style.use("ggplot")
fig = plt.figure(figsize=(16, 24))
# fig.suptitile("ShareBike Analysis", fontsize=16, fontweight="bold")
ax2 = fig.add_subplot(1, 1, 1)
sns.boxplot(data=df, x=x_values, y=y_values)
ax2.set(ylabel="Count", xlabel="Week_day", title="box plot on count across week")
plt.show()

plt.style.use("ggplot")
fig = plt.figure(figsize=(16, 24))
ax1 = fig.add_subplot(1, 1, 1)
fig.set_size_inches(18, 8)
sns.barplot(data=df, x=x_values, y=y_values, ax=ax1)
ax1.set(xlabel="day", ylabel="y_values", title="hour-count")
plt.savefig("../graph/hour-numberOfRide-barplot.jpg")
plt.show()