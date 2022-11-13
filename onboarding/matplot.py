'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''
import matplotlib.pyplot as plt
import pandas as pd


graph_data = pd.read_csv('test_data.csv', header=None,names=['x','x1','y','l','z'])

x = graph_data.x
y = graph_data.y
z = graph_data.z
l = graph_data.l
x1 = graph_data.x1
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(l,x1, color = 'm', )
ax1.plot(l,y,)
ax2.plot(l,z)
ax2.plot(l,x, color = 'm')

ax1.set_xlabel('X Values')
ax1.set_ylabel('Y Values')
ax2.set_xlabel('X Values')
ax2.set_ylabel('Y Values')
ax1.grid(True, color='k', linestyle=':')
ax2.grid(True, color='k', linestyle=':')

plt.show()


