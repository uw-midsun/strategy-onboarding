"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

# Your code here
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.transforms as mtransforms 


df = pd.read_csv('q3_test_data.csv')
df.ffill()
plt.plot(df['0.1'])
plt.savefig("plot_1.jpg")
plt.clf()
plt.plot(df['0.2'])
plt.savefig("plot_2.jpg")
plt.clf()
plt.plot(df['0.3'])
plt.savefig("plot_3.jpg")
plt.clf()
plt.plot(df['1'])
plt.yscale('log')
plt.savefig("plot_4.jpg")
plt.clf()