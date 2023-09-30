"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

# Your code here
import pandas as pd
import matplotlib.pyplot as plt
import os

# Assuming "q3_test_data.csv" is in the current working directory
data = pd.read_csv("q3_test_data.csv")

# Create the "q3_plots" folder if it doesn't exist
if not os.path.exists("q3_plots"):
    os.makedirs("q3_plots")

x_column = data.columns[0]

# Plot and save data
for column in data.columns:
    if column != x_column:
        plt.figure(figsize=(8, 6))
        plt.plot(data[x_column], data[column], marker='o', linestyle='-', label=column)
        plt.title(column + " vs " + x_column)
        plt.xlabel(x_column)
        plt.ylabel(column)
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join("q3_plots", column + "_plot.png"))
        plt.close()