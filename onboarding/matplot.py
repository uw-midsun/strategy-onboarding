'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\Mi Nâu\OneDrive - University of Waterloo\Máy tính\Midnight Sun\strategy-onboarding\onboarding\test_data.csv')

df.columns('x')

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['x', 'y1', 'y2', 'y3', 'y4']

df = pd.read_csv(r'C:\Users\Mi Nâu\OneDrive - University of Waterloo\Máy tính\Midnight Sun\strategy-onboarding\onboarding\test_data.csv',names = headers)

df.set_index('x').plot()

plt.show()