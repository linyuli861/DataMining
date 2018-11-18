import matplotlib
import numpy as np
import matplotlib.pyplot as plt


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y =[1060, 724, 361, 165, 199, 475, 1117, 2927, 4767, 4559, 4629, 5605, 6373, 6525, 6295, 6487, 7533, 8649, 7781, 6603, 4644, 3703, 2431, 1671]


plt.plot(x,y,label='Frist line',linewidth=3,color='b',marker='o',
markerfacecolor='blue',markersize=8)
# x = time_list
# y = message_list
plt.figure(figsize=(8, 6))
# plt.plot(x, y, "r", lable="times")
plt.xlabel("hour")
plt.ylabel("frequency")
plt.show()
