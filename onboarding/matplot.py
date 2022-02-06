import matplotlib.pyplot as plt
import pandas as pd

'''
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

data = pd.read_csv("test_data.csv")

plt.plot(data.column_a, label = "x")
plt.plot(data.column_b, label = "x again")
plt.plot(data.column_c, label = "2x")
plt.plot(data.column_d, label = "x^2")

plt.xlim(0,50)
plt.ylim(0,50)

plt.title("Matt's Graph", fontdict={'fontsize' : 15})
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()

plt.show()