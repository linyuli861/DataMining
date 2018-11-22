# coding = utf-8
import numpy as np
import pandas as pd
import time,datetime
import matplotlib.pyplot as plt


share_bike1 = pd.DataFrame(pd.read_csv("../data/metro-2018-1.csv"))
share_bike2 = pd.DataFrame(pd.read_csv("../data/metro-2018-2.csv"))
share_bike3 = pd.DataFrame(pd.read_csv("../data/metro-2018-3.csv"))
# 合并绿色出租车2018年1-9月数据
share_bike = share_bike1.append(share_bike2, ignore_index=False)
share_bike = share_bike.append(share_bike3, ignore_index=False)
print(share_bike.shape)
fp = open('../modify_data/three_months_data.csv', 'w')
share_bike.to_csv(fp)

# print(share_bike.head())
# share_bike['month'] = share_bike['start_time'].dt.month
# share_bike['day'] = share_bike['start_time'].dt.day
# share_bike['hour'] = share_bike['start_time'].dt.hour
# share_bike["week_day"] = share_bike['start_time'].dt.weekday_name
# share_bike['time'] = share_bike['start_time'].dt.date
# share_bike['count'] = 1
