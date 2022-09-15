'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

import pandas as pd 
import matplotlib.pyplot as plt


data = pd.read_csv('test_data.csv')

data = data.astype(float)


plt.title('x function')
plt.plot(data.iloc[:,0], data.iloc[:,1])
plt.show()

plt.title('2x function')
plt.plot(data.iloc[:,0], data.iloc[:,2])
plt.show()

plt.title('quadratic')
plt.plot(data.iloc[:,0], data.iloc[:,3])
plt.show()

plt.title('exponential function')
plt.plot(data.iloc[:,0], data.iloc[:,4])

plt.show()


