import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import data
data = pd.read_csv("test_data.csv", header=None)

plt.figure(1)
plt.plot(data[0])

plt.figure(2)
plt.plot(data[1])

plt.figure(3)
plt.plot(data[2])

plt.figure(4)
plt.yscale("log")
plt.plot(data[3])

plt.figure(5)
ax = plt.axes(xscale="linear", yscale="log")
ax.yaxis.set_major_locator(plt.MaxNLocator(10))
plt.plot(data[4])

plt.show()
