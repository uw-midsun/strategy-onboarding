import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/davidlu/Desktop/strategy-onboarding/onboarding/test_data.csv", header=None)
# df.plot()
fig, axs = plt.subplots(2,2)
axs[0][0].plot(df[0], df[1])
axs[0][1].plot(df[0], df[2])
axs[1][0].plot(df[0], df[3])
axs[1][1].plot(df[0], df[4].astype(float))


plt.show()
'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

