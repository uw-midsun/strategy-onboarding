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

# Read CSV file and drop NaN points
column_names = ["Column1", "Column2", "Column3", "Column4", "Column5"]
test_data = pd.read_csv("q3_test_data.csv", header=None,names=column_names).dropna()

# Extract column data
index = test_data["Column1"]
column2_data = test_data["Column2"]
column3_data = test_data["Column3"]
column4_data = test_data["Column4"]
column5_data = test_data["Column5"]

# Create 4 subplots
figs, axs = plt.subplots(4, figsize=(8, 10))
axs[0].plot(index, column2_data)
axs[1].plot(index, column3_data)
axs[2].plot(index, column4_data)
axs[3].plot(index, column5_data)
axs[3].set_yticks(column5_data[::200])

# Label subplots
plot = 1
for ax in axs:
    ax.set_title(f"Plot {plot}")    
    ax.set_xticks(index[::200])
    plot += 1

plt.tight_layout()
plt.show()