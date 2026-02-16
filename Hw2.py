#Generate 1000 random numbers between 0 and 10 and compute the histogram of this set with the width of the histogram set to be 1. Note there are functions in python that can turn a set of numbers into histograms, but do not use that. Instead, write your own program from scratch.

import numpy as np
import matplotlib.pyplot as plt


numbers = []
for i in range(1000):
    x = np.random.rand() * 10
    numbers.append(x)


hist = [0] * 10

for x in numbers:
    index = int(x)   
    if index == 10:  
        index = 9
    hist[index] = hist[index] + 1

for i in range(10):
    print("Bin","[",i,",",i+1,")", ":", hist[i])

bins = list(range(10))  

plt.bar(bins, hist, width=0.9, edgecolor='black')
plt.xticks(bins,["[0,1)","[1,2)","[2,3)","[3,4)","[4,5)","[5,6)", "[6,7)", "[7,8)","[8,9)","[9,10)"])
plt.ylabel("Count")
plt.title("Histogram of 1000 Random Numbers)")
plt.show()
