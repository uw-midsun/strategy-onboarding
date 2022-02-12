'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("test_data.csv", header=None, names=["x", "y1", "y2", "y3", "y4"])

fig, plots = plt.subplots(2, 2)
plots[0, 0].plot(data["x"], data["y1"])
plots[0, 0].set_title('Plot 1')
plots[0, 1].plot(data["x"], data["y2"], 'tab:purple')
plots[0, 1].set_title('Plot 2')
plots[1, 0].plot(data["x"], data["y3"], 'tab:green')
plots[1, 0].set_title('Plot 3')

# couldn't really find  a nice way to format the axis labels for this one
plots[1,1].set_yscale("log")
plots[1,1].yaxis.set_major_locator(plt.MaxNLocator(1))
plots[1, 1].plot(data["x"], data["y4"], 'tab:red')
plots[1, 1].set_title('Plot 4')

plt.show()

