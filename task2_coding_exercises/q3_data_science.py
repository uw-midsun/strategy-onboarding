"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists("q3_plots"):
    os.makedirs("q3_plots")

df = pd.read_csv('q3_test_data.csv')

for column in df.columns:
    if (column != "0"):
        plt.xlabel(df.columns[0])
        plt.ylabel(column)
        plt.plot(df["0"], df[column])
        plt.title("" + column + " vs " + df.columns[0])
        plt.savefig(os.path.join("q3_plots", column + "_plot.png"))
        plt.close()
