'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("test_data.csv") # converting values in the csv file to a datafranme

for i in range(len(df.columns)):
    plt.plot(df.iloc[:, i]) # extracting each column of the dataframe to the plot
    plt.show() # displaying the plot