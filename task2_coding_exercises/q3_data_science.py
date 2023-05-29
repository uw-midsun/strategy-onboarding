"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

# used to read data from csv
import pandas as pd 
# used to plot data read from pandas
import matplotlib.pyplot as plt 
used_data = pd.read_csv('q3_test_data.csv', header = None)

# set the axes of the graph (x, y)
x = used_data[0]
plt.plot(x, x)

for lines in range(1, 4):
    # same graph for 4
    plt.title('task 3 graph')
    plt.plot(x, used_data[lines])

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
