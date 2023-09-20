"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

# Your code here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys as sys

"""path file to csv"""
df = pd.read_csv('C:\\Users\\yuisa\\OneDrive\\Documents\\Projects\\MidNightSunOnboarding\\strategy-onboarding\\task2_coding_exercises\\q3_test_data.csv')

"""reading each col"""
headers = ["0", "0.1", "0.2", "0.3", "1"] 

for i in headers:
    cleanDataSet = []
    
    """
    limit all numbers that exceed maximum number (cannot display really large numbers)
    """
    for point in df[i]:
        point = int(point)
        
        if point > sys.maxsize :
            cleanDataSet.append(sys.maxsize)
        else: 
            cleanDataSet.append(point)

    """control y ticks in plot"""
    steps = 10
    plt.yticks(range(1, max(cleanDataSet), int(max(cleanDataSet) / steps) ))
    plt.plot(cleanDataSet)
    plt.show()
