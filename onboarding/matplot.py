'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\sethi\\projects\\strategy-onboarding\\onboarding\\test_data.csv",header=None)

# Replace Blank values with DataFrame.replace() methods.
df = df.replace(' ', np.nan)                   # to get rid of empty values
nan_values = df[df.isna().any(axis=1)] 
fig, axs = plt.subplots(2,2)
axs[0][0].plot(df[0], df[1])
axs[0][1].plot(df[0], df[2])
axs[1][0].plot(df[0], df[3])
axs[1][1].plot(df[0], df[4].astype(float))


plt.show()


