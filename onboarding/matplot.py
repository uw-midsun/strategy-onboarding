'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''
import matplotlib.pyplot as plt
import pandas as pd


linear_data = pd.read_csv("test_data.csv", header=None, usecols= [0,1])
linear2_data = pd.read_csv("test_data.csv", header=None, usecols= [0,2])
quadratic_data = pd.read_csv("test_data.csv", header=None, usecols= [0,3])
exp_data = pd.read_csv("test_data.csv", header=None, usecols= [0,4])



print("Data:  ")
plt.plot(linear_data[0], linear_data[1])
plt.plot(linear2_data[0], linear2_data[2])
plt.plot(quadratic_data[0], quadratic_data[3])
plt.plot(exp_data[0], exp_data[4])
plt.show()
