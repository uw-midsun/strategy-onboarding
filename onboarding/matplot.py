'''
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
''' 
import csv
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('test_data.csv', sep=',', 
names=['c1', 'c2', 'c3', 'c4', 'c5'])


x = df.c1
y1 = df.c2
y2 = df.c3
y3 = df.c4
y4 = df.c5

figure, axis = plt.subplots(2, 2)

#Graph 1 (x1 x y1)
axis[0,0].plot(x, y1, color='r')
axis[0,0].set_title("Graph #1 - x vs y1")

#Graph 2 (x1 x y2)
axis[1,0].plot(x, y2, color='b')
axis[1,0].set_title("Graph #2 - x vs y2")

#Graph 3 (x1 x y3)
axis[0,1].plot(x, y3, color='g')
axis[0,1].set_title("Graph #2 - x vs y3")

plt.tight_layout() 
#Graph 4 (x1 x y1 x y2)
plt.yscale('log')
plt.ylabel('y4')
axis[1,1].plot(x, y4)
axis[1,1].set_title("Graph #4 - x vs y4")


plt.show()

#makes a graph combining all data
plt.figure()
plt.title("MegaGraph")
plt.yscale('log')
plt.tick_params(axis='y', bottom=False)
plt.ylabel('test')
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3, '--r')
plt.plot(x,y4)

plt.show()









