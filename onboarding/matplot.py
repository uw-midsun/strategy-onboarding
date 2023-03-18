#
# - Graph all the data. This can be all the same plot, or four separate plots
#    Use Matplotlib, please!
# - Be careful of data points that don't exist
# - Will require reading from CSV, can experiment with pandas
#
# We put together some very simple data in `test_data.csv`. Read it and graph it using Matplotlib

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("test_data.csv") # read the data

for i in range(len(df.columns)):
    plt.plot(df.iloc[:, i]) # plotting the data
    plt.show() 
