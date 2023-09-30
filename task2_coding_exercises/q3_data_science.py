"""
We've put together some very simple data in "q3_test_data.csv". 
Read it and graph it using Matplotlib. This can be all the same plot or four separate plots.
Put the generated plots in the "q3_plots" folder for us to see when you make a pull request

- Be careful of data points that don't exist
- Will require reading from CSV so feel free to use pandas
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

path = os.path.abspath(__file__)

df = pd.read_csv("strategy-onboarding/task2_coding_exercises/q3_test_data.csv")

fig1 = plt.figure()
plt.plot(df.iloc[:, 0], df.iloc[:, 1])
plt.title("Figure 1")
fig2 = plt.figure()
plt.plot(df.iloc[:, 0], df.iloc[:, 2])
plt.title("Figure 2")
fig3 = plt.figure()
plt.plot(df.iloc[:, 0], df.iloc[:, 3])
plt.title("Figure 3")
fig4 = plt.figure()
plt.plot(df.iloc[:, 0], df.iloc[:, 4])
rg = [16 ** n for n in range(126)]
plt.yticks(rg)
plt.title("Figure 4")

fig1.savefig('strategy-onboarding/task2_coding_exercises/q3_plots/fig1.png')
fig2.savefig('strategy-onboarding/task2_coding_exercises/q3_plots/fig2.png')
fig3.savefig('strategy-onboarding/task2_coding_exercises/q3_plots/fig3.png')
fig4.savefig('strategy-onboarding/task2_coding_exercises/q3_plots/fig4.png')