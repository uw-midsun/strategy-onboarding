"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

# Your code here
import os
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt

df = pd.read_csv('strategy-onboarding\\task2_coding_exercises\q3_test_data.csv')

df.plot()
plt.show()