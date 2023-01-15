'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''
import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
a = []
b = []
c = []
d = []

with open(r'strategy-onboarding/onboarding/test_data.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        a.append(int(row[1]))
        b.append(int(row[2]))
        c.append(int(row[3]))
        d.append(int(row[4]))

figure, axis = plt.subplots(2, 2)

axis[0, 0].scatter(x, a, color = 'g',s = 5)
axis[0, 0].set_xlim([0, 1000])
axis[0, 0].set_xticks(np.arange(0, 1000, 200))

axis[0, 1].scatter(x, b, color = 'b',s = 5)
axis[0, 1].set_xlim([0, 1000])
axis[0, 1].set_xticks(np.arange(0, 1000, 200))

axis[1, 0].scatter(x, c, color = 'r',s = 5)
axis[1, 0].set_xlim([0, 1000])
axis[1, 0].set_xticks(np.arange(0, 1000, 200))

axis[1, 1].scatter(x, d, color = 'y',s = 5)
axis[1, 1].set_xlim([0, 1000])
axis[1, 1].set_xticks(np.arange(0, 1000, 200))

plt.show()
