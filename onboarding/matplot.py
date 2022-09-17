'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''
import matplotlib.pyplot as plt
import csv

fig, axs = plt.subplots(4)

x = []
linear = []
double = []
square = []
exponential = []

with open(r'strategy-onboarding\onboarding\test_data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(int(row[0]))
        linear.append(int(row[1]))
        double.append(int(row[2]))
        square.append(int(row[3]))
        exponential.append(int(row[4]))

axs[0].plot(x, linear)
axs[1].plot(x, double)
axs[2].plot(x, square)
axs[3].plot(x, exponential)

plt.xticks([0, 1000])

plt.show()
