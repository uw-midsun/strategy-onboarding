'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

import pandas as pd
from matplotlib import pyplot as plt

# plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["num1", "num2", "num3", "num4", "num5"]
df = pd.read_csv("test_data.csv", names=columns)
print("Contents in csv file:\n", df)
plt.title("Test Data")
plt.plot(df.num1, df.num2, df.num3, df.num4, df.num5)
plt.show()
