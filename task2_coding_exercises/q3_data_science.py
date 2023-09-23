"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

# Your code here

import matplotlib.pyplot as plt
import pandas as pd

#read data
df = pd.read_csv('q3_test_data.csv', header = None)

#fill if value is missing
df.fillna(0)

for i in range(5):
    print(df[i])
    plt.plot(df[i])
    plt.show()
