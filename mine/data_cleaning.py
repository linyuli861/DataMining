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
# df.groupby(['start_time'], as_index=False)['start_time'].agg({'cnt': 'count'})

# print(df['time'])
granded = df.groupby(df['day'], ).groups
print(granded)
print(df.shape)
print(df.head())
