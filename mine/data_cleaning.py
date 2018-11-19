# coding = utf-8
import csv
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from datetime import datetime


df = pd.read_csv("../data/metro-2018.csv", parse_dates=['start_time'], encoding="ISO-8859-1")
cols = df.columns  # return column name
print(cols)  # print column name
# print(df.shape)
print(df.info())
plt.style.use('ggplot')

# df['year'] = df['start_time'].dt.year
df['month'] = df['start_time'].dt.month
df['day'] = df['start_time'].dt.day
df['hour'] = df['start_time'].dt.hour
df["week_day"] = df['start_time'].dt.weekday_name
df['time'] = df['start_time'].dt.date
df['count'] = 1

# print(df['time'])
granded = df.groupby(df['day'], ).groups
# print(granded)
# print(df.shape)
# print(df.head())

# plt.style.use["ggplot"]
plt.style.use("ggplot")
fig = plt.figure(figsize=(16, 24))
# fig.suptitile("ShareBike Analysis", fontsize=16, fontweight="bold")
ax1 = fig.add_subplot(1, 2, 1)
sns.boxplot(data=df, y="count")
plt.title("box plot on count")
plt.ylabel("count")
plt.show()

ax2 = fig.add_subplot(1, 2, 2)
sns.boxplot(data=df, x="week_day", y="count")
ax2.set(ylabel="Count", xlabel="Week_day", title="box plot on count across week")
plt.show()


# fig, axes = plt.subplots(nrows=2,ncols=2)
# fig.set_size_inches(12, 10)
#
# sns.boxplot(data=df,y="count",orient="v",ax=axes[0][0])
# sns.boxplot(data=df,y="count",x="day",orient="v",ax=axes[0][1])
# sns.boxplot(data=df,y="count",x="hour",orient="v",ax=axes[1][0])
# sns.boxplot(data=df,y="count",x="week_day",orient="v",ax=axes[1][1])
#
# axes[0][0].set(ylabel='Count',title="Count")
# axes[0][1].set(xlabel='day', ylabel='Count',title="Day-Count")
# axes[1][0].set(xlabel='Hour Of The All', ylabel='Count',title="Hour-Count")
# axes[1][1].set(xlabel='Week Day', ylabel='Count',title="Week Day-Count")
# plt.show()