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
data_df = pd.read_csv("task2_coding_exercises//q3_test_data.csv")
data_df.columns = ['X','Y1','Y2','Y3','Y4']

#FIGURE 1
fig1 = plt.figure(1)
plt.plot(data_df.X, data_df.Y1)
plt.show()
fig1.savefig("task2_coding_exercises/q3_plots/fig1.png")

#FIGURE 2
fig2 = plt.figure(2)
plt.plot(data_df.X, data_df.Y2)
plt.show()
fig2.savefig("task2_coding_exercises/q3_plots/fig2.png")

#FIGURE 3
fig3 = plt.figure(3)
plt.plot(data_df.X, data_df.Y3)
plt.show()
fig3.savefig("task2_coding_exercises/q3_plots/fig3.png")

#FIGURE 4
fig4 = plt.figure(4)
plt.plot(data_df.X, data_df.Y4)
plt.show()
fig4.savefig("task2_coding_exercises/q3_plots/fig4.png")
