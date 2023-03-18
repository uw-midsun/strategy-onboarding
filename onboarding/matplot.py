import matplotlib.pyplot as plt
import pandas as pd

def main():
    df = pd.read_csv('test_data.csv')
    plt.plot(df.iloc[:,1])
    plt.plot(df.iloc[:,2])
    plt.plot(df.iloc[:,3])
    plt.plot(df.iloc[:,4])
    plt.show()
main()