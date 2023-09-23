"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

# Your code here

import matplotlib
import matplotlib.pyplot as plt

# 5 columns of data

# read data form a csv file
import pandas as pd
df = pd.read_csv('q3_test_data.csv')

# plot the data
plt.plot(df['x'], df['y'])

# add labels
plt.xlabel('x - axis')
plt.ylabel('y - axis')

# add title
plt.title('Graphs')

# show the plot
plt.show()


