'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("test_data.csv", header=None)
a= df[0]
b= df[1]
c= df[2]
d= df[3]
e= df[4]



plt.plot(b,color="purple")
plt.plot(c,color="black")
plt.plot(d,color="red")
plt.plot(e,color="yellow")

plt.show()
