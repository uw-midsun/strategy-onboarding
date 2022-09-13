'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

import pandas as pd
import matplotlib.pyplot as plt

x = []
lin = []
twox = []
sqr = []
exp = []

df = pd.read_csv(r'onboarding\test_data.csv')

print(df.shape)

df_list = df.values.tolist()

for entry in df_list:
    x.append(int(entry[0]))
    lin.append(int(entry[1]))
    twox.append(int(entry[2]))
    sqr.append(int(entry[3]))
    exp.append(int(entry[4]))

    
fig, axs = plt.subplots(2, 2)
fig.suptitle("Midsun Onboarding Test Data")

ax1 = plt.subplot(221)
ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax1.plot(x, lin)
ax1.set_ylim([0, 10000])

ax2 = plt.subplot(222)
ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax2.plot(x, twox)
ax2.set_ylim([0, 10000])

ax3 = plt.subplot(223)
ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax3.plot(x, sqr)
ax3.set_ylim([0, 100000])

ax4 = plt.subplot(224)
ax4.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax4.plot(x, exp)
ax4.set_ylim([0, 1000000])

plt.show()

