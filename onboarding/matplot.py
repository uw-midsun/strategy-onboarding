import pandas as pd
import matplotlib.pyplot as plt

'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

data = pd.read_csv("test_data.csv", header = None)

plt.plot(data[1], data[2],data[3])

plt.title("My Graph 😀")
plt.xlabel('Index')
plt.ylabel('Value')
plt.savefig("graph")