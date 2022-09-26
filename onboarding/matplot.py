'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('test_data.csv', sep=',', header=None)
plt.plot(df[1].to_numpy())
plt.plot(df[2].to_numpy())
plt.plot(df[3].to_numpy())
plt.plot(df[4].to_numpy())
plt.show()