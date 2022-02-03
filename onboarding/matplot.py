import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

data = pd.read_csv("test_data.csv")

plt.plot(data.column_a, label = "x")
plt.plot(data.column_b, label = "x again")
plt.plot(data.column_c, label = "2x")
plt.plot(data.column_d, label = "x^2")
# I cant figure out why plotting column_e messes up the x lim and y lim shown on the plot!
# If I comment out the below line plotting column_e the plot works fine :/

#plt.plot(data.column_e, label = "2^x") 

# ^ uncomment this to see it breaks the plot

plt.xlim(0,50)
plt.ylim(0,50) # column_e seems to not listen to this restriction

plt.title("Matt's Graph", fontdict={'fontsize' : 15})
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()

plt.show()