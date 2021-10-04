'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('./test_data.csv')

df["0"] = df["0"].fillna(df["0"].mean())
df["1"] = df["0.1"].fillna(df["0.1"].mean())
df["0.2"] = df["0.2"].fillna(df["0.2"].mean())
df["0.3"] = df["0.3"].fillna(df["0.3"].mean())

df["1"] = df["1"].astype(int)
df["1"] = df["1"].fillna(df["1"].mean())

df.plot(title = "All Test Data", xlabel = "x", ylabel = "y", figsize = (10, 10))

df["0"].plot(title = "Test Data 0", xlabel = "x", ylabel = "y", figsize = (10, 10))

df["0.1"].plot(title = "Test Data 0.1", xlabel = "x", ylabel = "y", figsize = (10, 10))

df["0.2"].plot(title = "Test Data 0.2", xlabel = "x", ylabel = "y", figsize = (10, 10))

df["0.3"].plot(title = "Test Data 0.3", xlabel = "x", ylabel = "y", figsize = (10, 10))

df["1"].plot(title = "Test Data 1", xlabel = "x", ylabel = "y", figsize = (10, 10))