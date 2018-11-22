# coding = utf-8
import csv
import pandas as pd
import numpy as np


df = pd.read_csv("../data/metro-2018-3.csv", header=0, sep=",")
cols = df.columns  # return column name
print(cols)  # print column name
months = []
days = []
hours = []
seasons = []
start_time = df['start_time']
len = len(start_time)
for i in range(len):
    time = start_time[i]
    month = int(time[5:7])
    day = time[0:9]
    hour = time[11:13]
    if month > 9:
        season = 4
    elif month > 6:
        season = 3
    elif month > 3:
        season = 2
    else:
        season = 1
    months.append(month)
    days.append(day)
    hours.append(hour)
    seasons.append(season)

print(days)
