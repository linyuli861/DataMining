# coding = utf-8
import pandas as pd
from matplotlib.pyplot import plot as plt

df = pd.read_csv("../modify_data/time.csv", header=0, sep=",")
cols = df.columns  # return column name
print(cols)  # print column name

# correlation = df[["day", "month", "hour", "week_day"]].corr()
# correlation

