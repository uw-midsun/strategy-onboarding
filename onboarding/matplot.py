'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading values from csv
# Here df stands for dataframe
df = pd.read_csv('test_data.csv', header=None)


#iterating thru df and generating graphs
for i in range(len(df.columns)):
    # Accessing values of ith column of df
    # Then removing row index by '.values'
    plt.plot(df[i].values)
    # Saving output of the as png file
    plt.savefig('Output'+str(i+1)+'.png')
    # Clear plot
    plt.clf()
