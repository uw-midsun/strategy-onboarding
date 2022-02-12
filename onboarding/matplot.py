'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''
from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd 

data = pd.read_csv('test_data.csv', header=None)

figure, axis = plt.subplots(2)
colour = ['peru', 'orchid', 'gold', 'darkcyan']
for x in range(0, 4):
    axis[0].scatter(data[0], data[x], c=colour[x - 1], label=colour[x - 1])
axis[1].scatter(data[0], data[4], c=colour[3], label=colour[3])

axis[0].set_title('Test Plot data sets 1-3')
axis[1].set_title('Test Plot data set 4')
axis[0].set(ylabel='y-axis')
axis[1].set(xlabel='x-axis', ylabel='y-axis')

plt.show()
