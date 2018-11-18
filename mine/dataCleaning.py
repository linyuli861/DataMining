# coding = utf-8
import csv
import pandas as pd
import numpy as np
from collections import defaultdict
from datetime import datetime


df = pd.read_csv("../data/metro-2018.csv", header=0, sep=",")
cols = df.columns  # return column name
print(cols)  # print column name
months = []
days = []
hours = []
week_days = []
start_time = df['start_time']
start_stations = df['start_station']
len = len(start_time)
for i in range(len):
    time = start_time[i]
    month = int(time[5:7])
    day = time[0:10]
    hour = time[11:13]
    months.append(month)
    days.append(day)
    hours.append(hour)
    week_days.append(datetime.strptime(day, "%Y-%m-%d").weekday())

print(df.shape)
writer = csv.writer("../modify_data/cleaning.csv", delimiter=",")
for month in months:
    month.append(15)
    writer.writerow(month)

# monthly = df.resample("days", how=len)['trip_id']
#
# dataframe = pd.DataFrame({"day": days, "month": months, "hour": hours, "week_day": week_days})
# dataframe.to_csv("../modify_data/time.csv")

