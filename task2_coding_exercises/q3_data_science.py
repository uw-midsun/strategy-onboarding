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
import os

csv = "q3_test_data.csv"
data = pd.read_csv(csv,header=None)

cols = ["Col 1","Col 2","Col 3","Col 4"]
plt.figure(figsize=(10, 6))


for i, col in enumerate(cols):
    plt.figure(figsize=(12,8))
    plt.plot(data.iloc[:,i])
    plt.title(f"Col: {i+1}")
    plot_file = os.path.join("q3_plots", f"column{i+1}_plot.png")
    plt.tight_layout()
    plt.savefig(plot_file)


plt.show()